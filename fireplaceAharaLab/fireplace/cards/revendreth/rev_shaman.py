from ..utils import *

Rev_Shaman=[]

Rev_Totemic_Evidence=True
Rev_Framester=True
Rev_Torghast_Custodian=True
Rev_Criminal_Lineup=True
Rev_Baroness_Vashj=True
Rev_Muck_Pools=True
Rev_Gigantotem=True
Rev_Carving_Chisel=True
Rev_Convincing_Disguise=True
Rev_The_Stonewright=True
Rev_Muck_Pools=True
Rev_Primordial_Wave=True
Rev_Baroness_Vashj=True
Rev_Party_Favor_Totem=True
Rev_Crud_Caretaker=True
Rev_Relics_of_Old=True


class MorphCostup(TargetedAction):
	"""
	Morph minion target into a cost-up minion
	TARGET = ActionArg()
	AMOUNT = IntArg()
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if isinstance(target, list):
			for tgt in [tgt for tgt in target]:
				amount = max(tgt.cost+amount, 0)
				card = RandomMinion(cost=amount).evaluate(source)
				if isinstance(card, list):
					card=card[0]
				if tgt.id!='REV_925':
					Morph(target, card).trigger(card)
				else:
					Summon(source.controller, card).trigger(card)
		else:
			amount = max(target.cost+amount, 0)
			card = RandomMinion(cost=amount).evaluate(source)
			if isinstance(card, list):
				card=card[0]
			if target.id!='REV_925':
				Morph(target, card).trigger(card)
			else:
				Summon(source.controller, card).trigger(card)
	pass

ALL_BASIC_TOTEM = ["CS2_050", "CS2_051", "CS2_052", "NEW1_009"] ## hero.py

if Rev_Totemic_Evidence:# ###
	Rev_Shaman+=['MAW_003']
	Rev_Shaman+=['MAW_003t']
class MAW_003_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		Summon(self.controller, card).trigger(self)
	pass
class MAW_003:# <8>[1691]
	""" Totemic Evidence
	Choose a basic Totem and summon it. <b>Infuse (@ Totems):</b> Summon all 4 instead. """
	class Hand:
		events = Death(FRIENDLY+TOTEM).on(Infuse(CONTROLLER, 'MAW_003t'))
	class Deck:
		events = Death(FRIENDLY+TOTEM).on(Infuse(CONTROLLER, 'MAW_003t', 1))
	plat = MAW_003_Choice(CONTROLLER, RandomID(*ALL_BASIC_TOTEM)*3)
	pass
class MAW_003t:# <8>[1691]
	""" Totemic Evidence
	<b>Infused</b> Summon all 4 basic Totems. """
	play = Summon(CONTROLLER, ALL_BASIC_TOTEM)
	pass

if Rev_Framester:# ###
	Rev_Shaman+=['MAW_005']
	Rev_Shaman+=['MAW_005t']
class MAW_005:# <8>[1691]
	""" Framester
	<b>Battlecry:</b> Shuffle 3 'Framed' cards into the opponent's deck. When drawn, they <b>Overload</b> for (2). """
	play = Shuffle(OPPONENT, 'MAW_005t')*3
	pass
class MAW_005t:# <8>[1691]
	""" Framed
	<b>Casts When Drawn</b> <b>Overload:</b> (2) """
	#	<Tag enumID="215" name="OVERLOAD" type="Int" value="2"/>
	#	<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	play = SetAttr(CONTROLLER, 'overload', 2)## we need it for overload
	pass

if Rev_Torghast_Custodian:# ###
	Rev_Shaman+=['MAW_030']
class MAW_030:# <8>[1691]
	""" Torghast Custodian
	<b>Battlecry:</b> For each enemy minion, randomly gain <b>Rush</b>, <b>Divine Shield</b>, or <b>Windfury</b>. """
	def play(self):
		controller=self.controller
		amount=len(controller.opponent.field)
		cards=['rush','shield','wind']
		if amount<3:
			cards=random.sample(cards, amount)
		if 'rush' in cards:
			self.rush=True
		if 'shield' in cards:
			self.divine_shield=True
		if 'wind' in cards:
			self.windfury=1
	pass

#	Rev_Shaman+=['MAW_030e2']
#class MAW_030e2:# <8>[1691]
#	""" Crawling
#	<b>Rush</b>. """
#	#
#	pass
#
#	Rev_Shaman+=['MAW_030e3']
#class MAW_030e3:# <8>[1691]
#	""" Sweeping
#	<b>Divine Shield</b>. """
#	#
#	pass
#
#	Rev_Shaman+=['MAW_030e4']
#class MAW_030e4:# <8>[1691]
#	""" Formidable
#	<b>Windfury</b>. """
#	#
#	pass




if Rev_Criminal_Lineup:# 
	Rev_Shaman+=['REV_517']
class REV_517:# <8>[1691]
	""" Criminal Lineup
	Choose a friendly minion. Summon 3 copies of it. <b>Overload:</b> (2) """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	#
	play = Summon(CONTROLLER, Copy(TARGET)) * 3
	pass




#if Rev_Baroness_Vashj:# 
#	Rev_Shaman+=['REV_788']
#class REV_788:# <8>[1691]
#	""" Baroness Vashj
#	{0} {1} {2} {3} """
#	#
#	pass
#
#if Rev_Muck_Pools:# 
#	Rev_Shaman+=['REV_798']
#class REV_798:# <8>[1691]
#	""" Muck Pools
#	{0} {1} """
#	#
#	pass




if Rev_Gigantotem:# ###
	Rev_Shaman+=['REV_838']
class REV_838:# <8>[1691]
	""" Gigantotem
	Costs (1) less for each Totem you've summoned this game. """
	cost_mod=-Count(SUMMONED + FRIENDLY + TOTEM)
	pass




if Rev_Carving_Chisel:# ###
	Rev_Shaman+=['REV_917']
class REV_917:# <8>[1691]
	""" Carving Chisel
	After your hero attacks, summon a random basic Totem. """
	events = Attack(FRIENDLY_HERO).after(
		Summon(CONTROLLER, RandomID(*ALL_BASIC_TOTEM))
	)
	pass




if Rev_Convincing_Disguise:# ###
	Rev_Shaman+=['REV_920']
	Rev_Shaman+=['REV_920t']
class REV_920:# <8>[1691]
	""" Convincing Disguise
	Transform a friendly minion into one that costs (2) more. <b>Infuse (@):</b> Transform all friendly minions instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_920t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_920t', 1))
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	
	play = MorphCostup(TARGET, 2)
	pass
class REV_920t:# <8>[1691]
	""" Convincing Disguise
	<b>Infused</b> Transform all friendly minions into random ones that cost (2) more. """
	play = MorphCostup(FRIENDLY_MINIONS, 2)
	pass




if Rev_The_Stonewright:# ###
	Rev_Shaman+=['REV_921']
	Rev_Shaman+=['REV_921e']
class REV_921:# <8>[1691]
	""" The Stonewright
	<b>Battlecry:</b> For the rest of the game, your Totems have +2 Attack. """
	play = Buff(CONTROLLER, 'REV_921e')
	pass
class REV_921e:# <8>[1691]
	""" Living Stone
	Your Totems have +2 Attack. """
	update = Refresh(FRIENDLY_MINIONS + TOTEM, {GameTag.ATK:2, })
	pass




if Rev_Muck_Pools:# 
	Rev_Shaman+=['REV_923']
class REV_923:# <8>[1691]
	""" Muck Pools
	Transform a friendly minion into one that costs (1) more. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = MorphCostup(TARGET, 1)#
	pass




if Rev_Primordial_Wave:# ###
	Rev_Shaman+=['REV_924']
class REV_924:# <8>[1691]
	""" Primordial Wave
	Transform enemy minions  into ones that cost (1) less  and friendly minions into  ones that cost (1) more. """
	play = MorphCostup(FRIENDLY_MINIONS, 1), MorphCostup(ENEMY_MINIONS, -1)
	pass




if Rev_Baroness_Vashj:# ###
	Rev_Shaman+=['REV_925']
class REV_925:# <8>[1691]
	""" Baroness Vashj
	If this would transform into a minion, summon that minion instead. """
	## see MorphCostup
	pass




if Rev_Party_Favor_Totem:# ###
	Rev_Shaman+=['REV_935']
	Rev_Shaman+=['REV_935t']
class REV_935_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		Summon(controller, random.choice(ALL_BASIC_TOTEM)).trigger(source)
		pass
class REV_935:# <8>[1691]
	""" Party Favor Totem
	At the end of your turn,  summon a random basic  Totem. <b>Infuse (@):</b>  Summon two instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_935t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_935t', 1))
	play = OWN_TURN_END.on(REV_935_Action(CONTROLLER))
	pass
class REV_935t_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		Summon(controller, random.sample(ALL_BASIC_TOTEM, 2)).trigger(source)
		pass
class REV_935t:# <8>[1691]
	""" Party Favor Totem
	<b>Infused </b>At the end of your turn,  summon two random  basic Totems. """
	play = OWN_TURN_END.on(REV_935t_Action(CONTROLLER))
	pass




if Rev_Crud_Caretaker:# ###
	Rev_Shaman+=['REV_936']
	Rev_Shaman+=['REV_936t']
class REV_936:# <8>[1691]
	""" Crud Caretaker
	<b>Battlecry</b>: Summon a 3/5 Elemental with <b>Taunt</b>. """
	play = Summon(CONTROLLER, 'REV_936t')
	pass
class REV_936t:# <8>[1691]
	""" Untreated Filth
	<b>Taunt</b> """
	#
	pass


