import os
from pkg_resources import resource_filename
from hearthstone import cardxml
from hearthstone.enums import CardType,CardSet
from ..logging import log
from ..utils import get_script_definition


class CardDB(dict):
	def __init__(self):
		self.initialized = False

	@staticmethod
	def merge(id, card, cardscript=None):
		"""
		Find the xmlcard and the card definition of \a id
		Then return a merged class of the two
		"""
		if card is None:
			card = cardxml.CardXML(id)

		if cardscript is None:
			cardscript = get_script_definition(id)

		if cardscript:
			card.scripts = type(id, (cardscript, ), {})
		else:
			card.scripts = type(id, (), {})

		scriptnames = (
			"activate", "combo", "deathrattle", "draw", "inspire", "play",
			"enrage", "update", "powered_up", "outcast", "awaken"
		)

		for script in scriptnames:
			actions = getattr(card.scripts, script, None)
			if actions is None:
				# Set the action by default to avoid runtime hasattr() calls
				setattr(card.scripts, script, [])
			elif not callable(actions):
				if not hasattr(actions, "__iter__"):
					# Ensure the actions are always iterable
					setattr(card.scripts, script, (actions, ))

		for script in ("events", "secret"):
			events = getattr(card.scripts, script, None)
			if events is None:
				setattr(card.scripts, script, [])
			elif not hasattr(events, "__iter__"):
				setattr(card.scripts, script, [events])

		if not hasattr(card.scripts, "cost_mod"):
			card.scripts.cost_mod = None

		if not hasattr(card.scripts, "Hand"):
			card.scripts.Hand = type("Hand", (), {})

		if not hasattr(card.scripts.Hand, "events"):
			card.scripts.Hand.events = []

		if not hasattr(card.scripts.Hand.events, "__iter__"):
			card.scripts.Hand.events = [card.scripts.Hand.events]

		if not hasattr(card.scripts.Hand, "update"):
			card.scripts.Hand.update = ()

		if not hasattr(card.scripts.Hand.update, "__iter__"):
			card.scripts.Hand.update = (card.scripts.Hand.update, )

		# Set choose one cards
		if hasattr(cardscript, "choose"):
			card.choose_cards = cardscript.choose[:]
		else:
			card.choose_cards = []

		if hasattr(cardscript, "tags"):
			for tag, value in cardscript.tags.items():
				card.tags[tag] = value

		if hasattr(cardscript, "requirements"):
			card.powers.append({"requirements": cardscript.requirements})
		else:
			card.powers.append({"requirements": {}})

		if hasattr(cardscript, "entourage"):
			card.entourage = cardscript.entourage

		if hasattr(cardscript, "dormant"):
			card.dormant = cardscript.dormant
		else:
			card.dormant = 0


		return card

	def initialize(self, locale="jaJP"):
		log.info("Initializing card database")
		self.initialized = True
		db, xml = cardxml.load(locale=locale)
		exclude = [
			# bug cards
			'SCH_199',## neutral-scholo, this card morphs w.r.t. the background when playing
			'SCH_259',## neutral-scholo, while this weapon is played, each turn begin allows me to compare the drawn card and other cards.
			'YOD_009',## this is a hero in galakrond
			'DRG_050','DRG_242','DRG_099',## neutral-dragon/45 These are invoking cards for galakrond
			'ULD_178',## neutral-uldum, this card allows us to add 2 of 4 enchantments when we use.
			'DAL_800', ## change all cards in the friendly deck, and it might occur some troubles. 
			# no implementation
			#'BT_730',
			]
		nameList=[]
		#print("idList=[")
		for id, card in db.items():
			#if card.name in nameList:
			#	print("'%s',"%(card.id))
			from hearthstone.enums import GameTag
			## add attr spellpower
			spellpowervalue = card.tags.get(GameTag.SPELLPOWER)
			if spellpowervalue is not None:
				setattr(card, 'spellpower', spellpowervalue)
			else:
				setattr(card, 'spellpower', 0)
			yes = False
			#if card.card_set == CardSet.STORMWIND: # 1578:
			#	if 'SW_' in card.id:
			#		yes = True					
			#if card.card_set == CardSet.THE_BARRENS:#1525
			#	if 'BAR_' in card.id or 'WC_' in card.id:
			#		yes = True					
			if card.card_set == CardSet.DARKMOON_FAIRE:#1466
				if 'DMF_' in card.id or 'YOP_' in card.id:
					yes = True

			elif card.card_set in [2,3,4,12,17,18,1004,1130,1158,1347,1403,1414,1443,1635, CardSet.CORE]:
				if (not 'LOOT_' in card.id) and (not 'CORE_' in card.id) and (not card.id in exclude):
					yes = True
			elif card.id in ['OG_280']:#C'Thun
				yes = True
			if card.card_set == 15:
				if card.id in ['AT_132_DRUIDe',"AT_132_SHAMANa", "AT_132_SHAMANb", "AT_132_SHAMANc", "AT_132_SHAMANd","AT_132_ROGUEt",]:## cardset 15
					yes = True
			if yes:
				self[id] = self.merge(id, card)
			## end ###
		log.info("Merged %i cards", len(self))


	def filter(self, **kwargs):
		"""
		Returns a list of card IDs matching the given filters. Each filter, if not
		None, is matched against the registered card database.
		cards.
		Examples arguments:
		\a collectible: Whether the card is collectible or not.
		\a type: The type of the card (hearthstone.enums.CardType)
		\a race: The race (tribe) of the card (hearthstone.enums.Race)
		\a rarity: The rarity of the card (hearthstone.enums.Rarity)
		\a cost: The mana cost of the card
		"""
		if not self.initialized:
			self.initialize()

		cards = self.values()

		if "type" not in kwargs:
			kwargs["type"] = [CardType.SPELL, CardType.WEAPON, CardType.MINION]

		for attr, value in kwargs.items():
			if value is not None:
				# What? this doesn't work?
				# cards = __builtins__["filter"](lambda c: getattr(c, attr) == value, cards)

				if attr == "card_class":
					cards = [card for card in cards if value in card.classes]
				else:
					cards = [
						card for card in cards if (
							isinstance(value, list) and getattr(card, attr) in value) or
						getattr(card, attr) == value
					]

		return [card.id for card in cards]


# Here we import every card from every set and load the cardxml database.
# For every card, we will "merge" the class with its Python definition if
# it exists.
if "db" not in globals():
	db = CardDB()
	filter = db.filter
