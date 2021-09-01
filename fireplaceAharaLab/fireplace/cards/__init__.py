import os
from pkg_resources import resource_filename
from hearthstone import cardxml
from hearthstone.enums import CardType,CardSet,CardClass
from ..logging import log
from ..utils import get_script_definition
from hearthstone.enums import GameTag


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


	def initialize(self, locale="jaJP"):#locale="enUS"):#
		log.info("Load card database")
		self.initialized = True
		db, xml = cardxml.load(locale=locale)
		exclude = [
			# bug or no implementation cards
			'SCH_199',## neutral-scholo, this card morphs w.r.t. the background when playing
			'SCH_259',## neutral-scholo, while this weapon is played, each turn begin allows me to compare the drawn card and other cards.
			'YOD_009',## this is a hero in galakrond
			#'DRG_050','DRG_242','DRG_099',## neutral-dragon/45 These are invoking cards for galakrond
			#'ULD_178',## neutral-uldum, this card allows us to add 2 of 4 enchantments when we use.
			#'DAL_800', ## change all cards in the friendly deck, and it might occur some troubles. 
			# 
			#'BT_730',
			'BAR_079',## neutral-barrens, too huge
			'SW_079',## neutral=Stormwind, choice a dormant
			]
		log.info("Initializing card database")
		for id, card in db.items():
			if not card.card_class in [ CardClass.HUNTER, CardClass.MAGE, CardClass.DREAM, CardClass.NEUTRAL]:#3,4,11,12
				if card.id in [
					'SCH_617e',#2
					"BT_212e",'SCH_352e','SCH_351e','SCH_351e2',#7
				   ]:
					pass
				else:
					continue
			## add attr spellpower
			spellpowervalue = card.tags.get(GameTag.SPELLPOWER)
			if spellpowervalue is not None:
				setattr(card, 'spellpower', spellpowervalue)
			else:
				setattr(card, 'spellpower', 0)
			yes = False
			#if card.card_set == CardSet.VANILLA:#1646
			#	yes = True
			if card.card_set == CardSet.CORE:#1637
				if 'CORE_' in card.id or 'CS3_' in card.id or card.id == 'GAME_005':
					yes = True
			elif card.card_set == CardSet.LEGACY: # 1635
				if card.id in [
					'CS2_122e','CS2_222o','EX1_399e','NEW1_033o',# core-neutral
					'HERO_05bp','HERO_05bp2',#steady shot
					'HERO_08bp','HERO_08bp2',# Fireblast(<4>[1635])
					'NEW1_031','NEW1_032','NEW1_033','NEW1_034',#Animal Companion
				   ]:
					yes = True
			elif card.card_set == CardSet.STORMWIND: # 1578:
				if 'SW_' in card.id:
					yes = True					
			elif card.card_set == CardSet.THE_BARRENS:#1525
				if 'BAR_' in card.id or 'WC_' in card.id:
					yes = True					
			elif card.card_set == CardSet.DARKMOON_FAIRE:#1466
				if 'DMF_' in card.id or 'YOP_' in card.id:
					yes = True
			elif card.card_set == CardSet.SCHOLOMANCE:# 1443
					yes = True
			elif card.card_set == CardSet.BLACK_TEMPLE:#1414
					yes = True
			elif card.card_set == CardSet.DALARAN:# 1130
				if card.id in ['DAL_086e']:
					yes = True
			elif card.card_set == CardSet.TROLL:# 1129
				if card.id in ['TRL_111e1']:
					yes = True
			elif card.card_set == CardSet.BOOMSDAY:# 1127
				if card.id in ['BOT_083e']:
					yes = True
			elif card.card_set == CardSet.GILNEAS:#1125
				if card.id in ['GIL_828e']:
					yes = True
			elif card.card_set == CardSet.ICECROWN:#1001
				if card.id in ['ICC_026t']:
					yes = True
			elif card.card_set == CardSet.KARA:#23
				if card.id in ['KAR_036e']:
					yes = True
			elif card.card_set == CardSet.HERO_SKINS:#17:
				yes = True
			elif card.card_set == CardSet.TGT:# 15
				if card.id in [
					'AT_132_DRUIDe',"AT_132_SHAMANa", "AT_132_SHAMANb", "AT_132_SHAMANc", "AT_132_SHAMANd","AT_132_ROGUEt",
					'AT_061e',
					]:
					yes = True
			elif card.card_set == CardSet.EXPERT1:# 3
				if card.id in ['CS2_188o','EX1_004e','EX1_014t','EX1_014te','EX1_046e','EX1_059e','EX1_093e',\
					'EX1_103e','EX1_110t','EX1_162o','EX1_187e','EX1_399e','EX1_509e','FP1_007t','EX1_116t','tt_004o','NEW1_018e','NEW1_026t','NEW1_027e',
					'EX1_531e','EX1_554t','EX1_611e','EX1_534t',
					'DREAM_01','DREAM_02','DREAM_03','DREAM_04','DREAM_05','DREAM_05e']:
					yes = True
			#elif card.card_set in [2,3,4,12,18,1004,1130,1158,1347,1403,1414,1443,1635]:
			#	if (not 'LOOT_' in card.id)  and (not card.id in exclude):#and (not 'CORE_' in card.id)
			#		yes = True
			elif card.id in ['OG_280']:#C'Thun CardSet.OG (21)
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
