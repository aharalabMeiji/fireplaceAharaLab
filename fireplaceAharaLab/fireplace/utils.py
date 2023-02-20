import os.path
import random
import copy
import time
from bisect import bisect
from importlib import import_module
from pkgutil import iter_modules
from typing import List
from xml.etree import ElementTree
from enum import IntEnum

from hearthstone.enums import CardClass, CardType


# Autogenerate the list of cardset modules
_cards_module = os.path.join(os.path.dirname(__file__), "cards")
CARD_SETS = [cs for _, cs, ispkg in iter_modules([_cards_module]) if ispkg]

class CardList(list):
	def __contains__(self, x):
		for item in self:
			if x is item:
				return True
		return False

	def __getitem__(self, key):
		ret = super().__getitem__(key)
		if isinstance(key, slice):
			return self.__class__(ret)
		return ret

	def __int__(self):
		# Used in Kettle to easily serialize CardList to json
		return len(self)

	def contains(self, x):
		"""
		True if list contains any instance of x
		"""
		for item in self:
			if x == item:
				return True
		return False

	def index(self, x):
		for i, item in enumerate(self):
			if x is item:
				return i
		raise ValueError

	def remove(self, x):
		for i, item in enumerate(self):
			if x is item:
				del self[i]
				return
		i=0
		#raise ValueError

	def exclude(self, *args, **kwargs):
		if args:
			return self.__class__(e for e in self for arg in args if e is not arg)
		else:
			return self.__class__(e for k, v in kwargs.items() for e in self if getattr(e, k) != v)

	def filter(self, **kwargs):
		return self.__class__(e for k, v in kwargs.items() for e in self if getattr(e, k, 0) == v)


def random_draft(card_class: CardClass, exclude=[], fixed_cards=[]):
	"""
	Return a deck of 30 random cards for the \a card_class
	"""
	from . import cards
	from .deck import Deck

	deck = fixed_cards
	collection = []
	# hero = card_class.default_hero

	for card in cards.db.keys():
		if card in exclude:
			continue
		cls = cards.db[card]
		if not cls.collectible:
			continue
		if cls.type == CardType.HERO:
			# Heroes are collectible...
			continue
		if cls.card_class and cls.card_class not in [card_class, CardClass.NEUTRAL]:
			# Play with more possibilities
			continue
		collection.append(cls)
	random.seed(int(time.time()*100))
	while len(deck) < Deck.MAX_CARDS:
		card = random.choice(collection)
		if deck.count(card.id) < card.max_count_in_deck:
			deck.append(card.id)

	return deck


def random_class():
	return CardClass(random.randint(2, 10))


def get_script_definition(id):
	"""
	Find and return the script definition for card \a id
	"""
	for cardset in CARD_SETS:
		module = import_module("fireplace.cards.%s" % (cardset))
		if hasattr(module, id):
			return getattr(module, id)


def entity_to_xml(entity):
	e = ElementTree.Element("Entity")
	for tag, value in entity.tags.items():
		if value and not isinstance(value, str):
			te = ElementTree.Element("Tag")
			te.attrib["enumID"] = str(int(tag))
			te.attrib["value"] = str(int(value))
			e.append(te)
	return e


def game_state_to_xml(game):
	tree = ElementTree.Element("HSGameState")
	tree.append(entity_to_xml(game))
	for player in game.players:
		tree.append(entity_to_xml(player))
	for entity in game:
		if entity.type in (CardType.GAME, CardType.PLAYER):
			# Serialized those above
			continue
		e = entity_to_xml(entity)
		e.attrib["CardID"] = entity.id
		tree.append(e)

	return ElementTree.tostring(tree)


def weighted_card_choice(source, weights: List[int], card_sets: List[str], count: int):
	"""
	Take a list of weights and a list of card pools and produce
	a random weighted sample without replacement.
	len(weights) == len(card_sets) (one weight per card set)
	"""

	chosen_cards = []

	# sum all the weights
	cum_weights = []
	totalweight = 0
	for i, w in enumerate(weights):
		totalweight += w * len(card_sets[i])
		cum_weights.append(totalweight)

	# for each card
	for i in range(count):
		# choose a set according to weighting
		chosen_set = bisect(cum_weights, random.random() * totalweight)

		# choose a random card from that set
		if chosen_set>= len(card_sets):
			continue
		chosen_card_index = random.randint(0, len(card_sets[chosen_set]) - 1)

		chosen_cards.append(card_sets[chosen_set].pop(chosen_card_index))
		totalweight -= weights[chosen_set]
		cum_weights[chosen_set:] = [x - weights[chosen_set] for x in cum_weights[chosen_set:]]

	return [source.controller.card(card, source=source) for card in chosen_cards]


def setup_game():
	from .game import Game
	from .player import Player

	deck1 = random_draft(CardClass.MAGE)
	deck2 = random_draft(CardClass.WARRIOR)
	player1 = Player("Player1", deck1, CardClass.MAGE.default_hero)
	player2 = Player("Player2", deck2, CardClass.WARRIOR.default_hero)

	game = Game(players=(player1, player2))
	game.start()

	return game


#def play_turn(game):
#	player = game.current_player
#
#	while True:
#		heropower = player.hero.power
#		if heropower.is_usable() and random.random() < 0.1:
#			if heropower.requires_target():
#				heropower.use(target=random.choice(heropower.targets))
#			else:
#				heropower.use()
#			continue
#
#		# iterate over our hand and play whatever is playable
#		for card in player.hand:
#			if card.is_playable() and random.random() < 0.5:
#				target = None
#				if card.must_choose_one:
#					card = random.choice(card.choose_cards)
#				if card.requires_target():
#					target = random.choice(card.targets)
#				print("Playing %r on %r" % (card, target))
#				card.play(target=target)
#
#				if player.choice:
#					choice = random.choice(player.choice.cards)
#					print("Choosing card %r" % (choice))
#					player.choice.choose(choice)
#
#				continue
#
#		# Randomly attack with whatever can attack
#		for character in player.characters:
#			if character.can_attack():
#				character.attack(random.choice(character.targets))
#
#		break
#
#	game.end_turn()
#	return game


#def play_full_game():
#	game = setup_game()
#
#	for player in game.players:
#		print("Can mulligan %r" % (player.choice.cards))
#		mull_count = random.randint(0, len(player.choice.cards))
#		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
#		player.choice.choose(*cards_to_mulligan)
#
#	while True:
#		play_turn(game)
#
#	return game


class ActionType(IntEnum):
	ATTACK=1
	PLAY=7
	POWER=3
	PASS=4
	TRADE=14
	LOCATION=15


	def __str__(self):
		if self==1:
			return "ATTACK"
		if self==7:
			return "PLAY"
		if self==3:
			return "PASS"
		if self==14:
			return "TRADE"
		else:
			return ""

def modify_description(card, text):
	new_text=copy.deepcopy(text)
	new_text=new_text.replace('\n','_')
	new_text=new_text.replace('[x]','')
	new_text=new_text.replace('[b]','[')
	new_text=new_text.replace('[/b]',']')
	new_text=new_text.replace('[','[')
	new_text=new_text.replace(']',']')
	if hasattr(card,'script_data_text_0'):
		if isinstance(card.script_data_text_0, str):
			new_text=new_text.replace('{0}',card.script_data_text_0)
		else:
			new_text=new_text.replace('{0}',str(card.script_data_text_0))
	if hasattr(card,'script_data_text_1'):
		new_text=new_text.replace('{1}',card.script_data_text_1)
	if hasattr(card,'script_data_text_2'):
		new_text=new_text.replace('{2}',card.script_data_text_2)
	if hasattr(card,'script_data_text_3'):
		new_text=new_text.replace('{3}',card.script_data_text_3)
	if hasattr(card,'script_data_num_1') and '@'in text:
		new_text=new_text.replace('@',str(card.script_data_num_1))
	length=len(new_text)
	for i in range(length-3):
		if i>=len(new_text):
			break
		if '|4('==new_text[i:i+3]:
			anchor0=i+3
			for c in range(anchor0,length):
				if new_text[c]==',':
					anchor1=c
					word0=new_text[anchor0:anchor1]
					break
			for c in range(anchor1+1,length):
				if new_text[c]==')':
					anchor2=c
					word1=new_text[anchor1+1,anchor2]
					break
			if new_text[i-3:i]=='(1 ':
				new_text=new_text[:i]+word0+new_text[anchor2+1]
			else:
				new_text=new_text[:i]+word1+new_text[anchor2+1]
	length=len(new_text)
	if hasattr(card,'controller'):
		player = card.controller
	else:
		player=None
	for i in range(length):
		if new_text[i]=='$':
			if i+1<length and new_text[i+1] in ['0','1','2','3','4','5','6','7','8','9']:
				catch_number = int(new_text[i+1])
				latter_text = new_text[i+2:]
				if i+2<length and text[i+2] in ['0','1','2','3','4','5','6','7','8','9']:
					catch_number *= 10
					catch_number += int(new_text[i+2])
					latter_text = new_text[i+3:]
				if player:
					if hasattr(card,'spell_school') and card.spell_school == SpellSchool.FIRE:
						catch_number += player.spellpower_fire
					elif hasattr(card,'spell_school') and card.spell_school == SpellSchool.NATURE:
						catch_number += player.spellpower_nature
					else :
						catch_number += player.spellpower
					for repeat in range(player.spellpower_double):
						catch_number *= 2
				new_text = new_text[:i] + "*" +str(catch_number) +"*" + latter_text
	return new_text
