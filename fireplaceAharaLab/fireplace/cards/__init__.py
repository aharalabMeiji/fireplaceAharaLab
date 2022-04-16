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
			"enrage", "update", "powered_up", "outcast", "awaken","trade", "honorable_kill",
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
		if not hasattr(card.scripts, "Deck"):
			card.scripts.Deck = type("Deck", (), {})

		if not hasattr(card.scripts.Hand, "events"):
			card.scripts.Hand.events = []
		if not hasattr(card.scripts.Deck, "events"):
			card.scripts.Deck.events = []

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
		log.info("Initializing card database")
		from .cardlist import All
		for cardIDlist in All:
			for id in cardIDlist:
				card = db[id]
				spellpowervalue = card.tags.get(GameTag.SPELLPOWER)
				if spellpowervalue is not None:
					setattr(card, 'spellpower', spellpowervalue)
				else:
					setattr(card, 'spellpower', 0)
				if card.tags.get(GameTag.CHOOSE_ONE) is not None:
					setattr(card, 'has_choose_one', True)
				self[id] = self.merge(id, card)
				#if card.multiple_classes and card.type==CardType.SPELL and card.card_class==CardClass.NEUTRAL:
				#	print ("%s"%(id))
				pass
		log.info("Merged %i cards", len(self))

	def BG_initialize(self):
		locale = 'jaJP'
		self.initialized = True
		log.info("Load card database")
		db, xml = cardxml.load(locale=locale)
		log.info("Initializing card database")
		from fireplace.cards import battlegrounds
		BG=[
			battlegrounds.BG_hero1.BG_Hero1,
			battlegrounds.BG_hero1.Bartenders,
			battlegrounds.BG_minion.BG_Minion,
			battlegrounds.BG_minion_beast.BG_Minion_Beast,
			battlegrounds.BG_minion_demon.BG_Minion_Demon,
			battlegrounds.BG_minion_dragon.BG_Minion_Dragon,
			battlegrounds.BG_minion_elemental.BG_Minion_Elemental,
			battlegrounds.BG_minion_mecha.BG_Minion_Mecha,
			battlegrounds.BG_minion_murloc.BG_Minion_Murloc,
			battlegrounds.BG_minion_pirate.BG_Minion_Pirate,
			battlegrounds.BG_minion_quilboar.BG_Minion_Quilboar,
			]
		for cardIDlist in BG:
			for id in cardIDlist:
				card = db[id]
				self[id] = self.merge(id, card)
				pass
			pass
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
				elif attr == 'has_choose_one':
					cards = [card for card in cards if hasattr(card,'has_choose_one')]
				elif attr == 'tech_level':
					cards = [card for card in cards if card.tags.get(GameTag.TECH_LEVEL)==value ]
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
