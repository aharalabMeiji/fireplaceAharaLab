from ..utils import *

Alterac_Warlock=[]

Alterac_Seeds_of_Destruction=True
Alterac_Felfire_in_the_Hole=True
Alterac_Full_Blown_Evil=True
Alterac_Felwalker=True
Alterac_Grave_Defiler=True
Alterac_Sacrificial_Summoner=True
Alterac_Hollow_Abomination=True
Alterac_Dreadlich_Tamsin=True
Alterac_Tamsins_Phylactery=True
Alterac_Desecrated_Graveyard=True
Alterac_Impfestation=True
Alterac_Curse_of_Agony=True
Alterac_Spawn_of_Deathwing=True


if Alterac_Seeds_of_Destruction:# 
	Alterac_Warlock+=['AV_277']
class AV_277:# <9>[1626]
	""" Seeds of Destruction
	Shuffle four Rifts(AV_316t4) into your deck. They summon a 3/3 Dread Imp(AV_316t) when drawn. """
	play = Shuffle(CONTROLLER, 'AV_316t4')*4 
	pass

if Alterac_Felfire_in_the_Hole:# 
	Alterac_Warlock+=['AV_281']
class AV_281:# <9>[1626]
	""" Felfire in the Hole!
	Draw a spell and deal $2 damage to all enemies. If it's a Fel spell, deal $1 more. """
	def play(self):
		cards = [card for card in self.controller.deck if card.type==CardType.SPELL]
		if len(cards)>0:
			newcard = random.choice(cards)
			newcard.zone=Zone.HAND
			if newcard.type==CardType.SPELL and newcard.spell_school==SpellSchool.FEL:
				amount=3
			else:
				amount=2
			for enemy in self.controller.opponent.characters:
				Hit(enemy, amount).trigger(self)
	pass




if Alterac_Full_Blown_Evil:# ### OK ###
	Alterac_Warlock+=['AV_285']
class AV_285_Action1(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		SplitHit(controller, controller.opponent.field, 5).trigger(source)
		card =Give(controller, 'AV_285').trigger(source)
		if isinstance(card, list):
			card=card[0]
		if isinstance(card, list):
			card=card[0]
		Buff(card, 'AV_285e').trigger(source)
		pass
class AV_285_Action2(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		for card in controller.hand:
			if card.id=='AV_285':
				buffs = [buff.id for buff in card.buffs if buff.id=='AV_285e']
				if len(buffs)>0:
					card.destroy()
		pass
class AV_285:# <9>[1626]
	""" Full-Blown Evil (3) Fel
	Deal 5 damage randomly split among all enemy minions. Repeatable this turn. """
	play = AV_285_Action1(CONTROLLER)
		
	pass
@custom_card
class AV_285e:
	tags = {
		GameTag.CARDNAME: "Full-Blown Evil",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}
	events = OWN_TURN_END.on(AV_285_Action2(CONTROLLER))




if Alterac_Felwalker:# 
	Alterac_Warlock+=['AV_286']
	Alterac_Warlock+=['AV_286e2']
class AV_286:# <9>[1626]
	""" Felwalker(6/3/7) Demon
	[Taunt]. [Battlecry]: Cast the highest Cost Fel spell from your hand. """
	def play(self):
		controller = self.controller
		hand = controller.hand
		if hand!=[]:
			high=[]
			for card in hand:
				if card.type==CardType.SPELL and card.spell_school==SpellSchool.FEL:
					if high==[] or high[0].cost<card.cost:
						high=[card]
					elif high[0].cost==card.cost:
						high.append(card)
			if high != []:
				card = random.choice(high)
				controller.game.trigger(controller,[CastSpell(card)], event_args=None)
			pass
		pass
	pass
AV_286e2=buff(1,1)

if Alterac_Grave_Defiler:# 
	Alterac_Warlock+=['AV_308']
class AV_308:# <9>[1626]
	""" Grave Defiler
	[Battlecry:] Copy a Fel spell in your hand. """
	play = Give(CONTROLLER, ExactCopy(RANDOM(FRIENDLY_HAND + FEL)))
	pass

if Alterac_Sacrificial_Summoner:# 
	Alterac_Warlock+=['AV_312']
class AV_312:# <9>[1626]
	""" Sacrificial Summoner
	[Battlecry:] Destroy a friendly minion. Summon a minion from your deck that costs (1) more. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	#
	def play(self):
		if self.target!=None:
			cost = self.target.cost+1
			Destroy(self.target).trigger(self)
			cards=[card for card in self.controller.deck if card.type==CardType.MINION and card.cost==cost]
			if cards!=[]:
				Summon(self.controller, random.choice(cards)).trigger(self)
	pass

if Alterac_Hollow_Abomination:# 
	Alterac_Warlock+=['AV_313']
	Alterac_Warlock+=['AV_313e']
class AV_313:# <9>[1626]
	""" Hollow Abomination
	[Battlecry:] Deal 1 damage to all enemy minions. [Honorable Kill:] Gain the minion's Attack. """
	play = Hit(ENEMY_MINIONS, 1)
	#honorable_kill = Buff(SELF, 'AV_313e', atk=1)
	pass
class AV_313e:# <9>[1626]
	""" Consumed 	Increased attack. """
	pass

if Alterac_Dreadlich_Tamsin:# 
	Alterac_Warlock+=['AV_316']
	Alterac_Warlock+=['AV_316hp']
	Alterac_Warlock+=['AV_316t']
	Alterac_Warlock+=['AV_316t4']
class AV_316:# <9>[1626]
	""" Dreadlich Tamsin(6/*/5) Hero
	[Battlecry:] Deal 3 damage to all minions. Shuffle 3 Rifts(AV_316t4) into your deck. Draw 3 cards. """
	play = (
		Hit(ENEMY_MINIONS, 3),
		Shuffle(CONTROLLER, 'AV_316t4') * 3,
		Draw(CONTROLLER) * 3
		)
	pass
class AV_316hp:# <9>[1626]
	""" Chains of Dread
	[Hero Power] Shuffle a Rift(AV_316t4) into your deck. Draw a card. """
	activate=Shuffle(CONTROLLER, 'AV_316t4'), Draw(CONTROLLER)
	pass
class AV_316t:# <9>[1626]
	""" Dread Imp """
	pass
class AV_316t4:# <9>[1626]
	""" Fel Rift
	[Casts When Drawn] Summon a 3/3 Dread Imp(AV_316t). """
	#<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	play = Summon(CONTROLLER, 'AV_316t')
	pass

if Alterac_Tamsins_Phylactery:# 
	Alterac_Warlock+=['AV_317']
	Alterac_Warlock+=['AV_317e']
class AV_317_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		new_deathrattles = card.deathrattles
		ret = new_deathrattles[0]
		for minion in card.controller.field:
			minion.has_deathrattle=True
			minion.data.tags[GameTag.DEATHRATTLE]=True
			minion.data.scripts.deathrattle=tuple(ret)
			print("Copy [deathrattle] %s->%s"%(card, minion))
class AV_317:# <9>[1626]
	""" Tamsin's Phylactery
	[Discover] a friendly [Deathrattle] minion that died this game. Give your minions its [Deathrattle]. """
	#See SW_310
	def play(self):
		cards=[card.id for card in self.controller.death_log if card.has_deathrattle==True]
		if cards!=[]:
			AV_317_Choice(self.controller, RandomID(*cards)*3).trigger(self)
	pass
class AV_317e:# <9>[1626]
	""" Lich Perfume
	Copied [Deathrattle] from {0}. """
	tags={GameTag.DEATHRATTLE:1}#
	pass

if Alterac_Desecrated_Graveyard:# 
	Alterac_Warlock+=['AV_657']
	Alterac_Warlock+=['AV_657e']
	Alterac_Warlock+=['AV_657t']
class AV_657:# <9>[1626]
	""" Desecrated Graveyard
	At the end of your turn, destroy your lowest Attack minion to summon a 4/4 Shade. Lasts 3 turns. """
	events=[
		OWN_TURN_END.on(Destroy(RANDOM(LOWEST_ATK(FRIENDLY_MINIONS))), Summon(CONTROLLER, 'AV_657t')),
		OWN_TURN_BEGIN.on(SidequestCounter(CONTROLLER,3,[Destroy(SELF)]))
	]
	pass
class AV_657e:# <9>[1626]
	""" Sacrificing
	Sacrifice this at end of turn. """
	#
	pass
class AV_657t:# <9>[1626]
	""" Desecrated Shade """
	pass

if Alterac_Impfestation:# 
	Alterac_Warlock+=['ONY_033']
class ONY_033:# <9>[1626]
	""" Impfestation
	Summon a 3/3 Dread Imp(AV_316t) to attack each enemy minion. """
	#(Summoned Imp number = len of opponent's field)
	def play(self):
		amount = len(self.controller.opponent.field)
		for repeat in range(amount):
			newcard=Summon(CONTROLLER, 'AV_316t').trigger(self)
			newcard=newcard[0][0]
			if self.controller.opponent.field!=[]:
				target = random.choice(self.controller.opponent.field)
				RegularAttack(newcard, target).trigger(self)
	pass

if Alterac_Curse_of_Agony:# 
	Alterac_Warlock+=['ONY_034']
	Alterac_Warlock+=['ONY_034t']
class ONY_034:# <9>[1626]
	""" Curse of Agony
	Shuffle three Agonies into the opponent's deck. They deal Fatigue damage when drawn. """
	play = Shuffle(OPPONENT, 'ONY_034t')*3
	pass
class ONY_034t:# <9>[1626]
	""" Agony
	[Casts When Drawn] Take @ Fatigue damage. """
	#<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	# Fatigue damage -> see Fatigue(OPPONENT)
	play = Fatigue(OPPONENT)
	pass

if Alterac_Spawn_of_Deathwing:# 
	Alterac_Warlock+=['ONY_035']
class ONY_035:# <9>[1626]
	""" Spawn of Deathwing
	[Battlecry:] Destroy a random enemy minion. Discard a random card. """
	#random card means what? -> friendly hand cards
	play = Destroy(RANDOM(ENEMY_MINIONS)), Discard(RANDOM(FRIENDLY_HAND))
	pass

