from ..utils import *

if Config.PATCH_VERSION >= Config.PATCH23_2_2:
	BG_Minion_Quilboar=[
		'BG20_100','BG20_100_G',#Razorfen Geomancer	1
		'BG20_301','BG20_301_G',#Sun-Bacon Relaxer	1
		'BG20_101','BG20_101_G',#Roadboar	2
		'BG20_102','BG20_102e','BG20_102_G','BG20_102_Ge',#Tough Tusk	2
		'BG20_201','BG20_201_G',#Bannerboar	3
		'BG20_103','BG20_103_G',#Bristleback Brute	3
		'BG21_037','BG21_037_G',#Gemsplitter	3
		'BG20_105','BG20_105_G',#Thorncaller	3
		'BG20_104','BG20_104_G',#Bonker	4
		'BG20_207','BG20_207e','BG20_207_G','BG20_207_Ge',#Dynamic Duo	4
		'BG20_106','BG20_106e','BG20_106_G',#Groundshaker	4
		'BG20_202','BG20_202_G',#Necrolyte	4
		'BG20_302','BG20_302e','BG20_302_G','BG20_302_Ge',#Aggem Thorncurse	5
		##'BG20_206','BG20_206_G',#Captain Flat Tusk	6
		'BG20_303','BG20_303_G',#Charlga	6
		]

	BG_PoolSet_Quilboar=[
		['BG20_100','BG20_301',],
		['BG20_101','BG20_102',],
		['BG20_201','BG20_103','BG21_037','BG20_105',],
		['BG20_104','BG20_207','BG20_106','BG20_202',],
		['BG20_302',],
		['BG20_303',],##'BG20_206',
		]
else:
	BG_Minion_Quilboar=[
		'BG20_100','BG20_100_G',#Razorfen Geomancer	1
		'BG20_301','BG20_301_G',#Sun-Bacon Relaxer	1
		'BG20_101','BG20_101_G',#Roadboar	2
		'BG20_102','BG20_102e','BG20_102_G','BG20_102_Ge',#Tough Tusk	2
		'BG20_201','BG20_201_G',#Bannerboar	3
		'BG20_103','BG20_103_G',#Bristleback Brute	3
		'BG21_037','BG21_037_G',#Gemsplitter	3
		'BG20_105','BG20_105_G',#Thorncaller	3
		'BG20_104','BG20_104_G',#Bonker	4
		'BG20_207','BG20_207e','BG20_207_G','BG20_207_Ge',#Dynamic Duo	4
		'BG20_106','BG20_106e','BG20_106_G',#Groundshaker	4
		'BG20_202','BG20_202_G',#Necrolyte	4
		'BG20_302','BG20_302e','BG20_302_G','BG20_302_Ge',#Aggem Thorncurse	5
		'BG20_206','BG20_206_G',#Captain Flat Tusk	6
		'BG20_303','BG20_303_G',#Charlga	6
		]

	BG_PoolSet_Quilboar=[
		['BG20_100','BG20_301',],
		['BG20_101','BG20_102',],
		['BG20_201','BG20_103','BG21_037','BG20_105',],
		['BG20_104','BG20_207','BG20_106','BG20_202',],
		['BG20_302',],
		['BG20_206','BG20_303',],
		]

BG_Quilboar_Gold={
	'BG20_100':'BG20_100_G',#Razorfen Geomancer	1
	'BG20_301':'BG20_301_G',#Sun-Bacon Relaxer	1
	'BG20_101':'BG20_101_G',#Roadboar	2
	'BG20_102':'BG20_102_G',#Tough Tusk	2
	'BG20_201':'BG20_201_G',#Bannerboar	3
	'BG20_103':'BG20_103_G',#Bristleback Brute	3
	'BG21_037':'BG21_037_G',#Gemsplitter	3
	'BG20_105':'BG20_105_G',#Thorncaller	3
	'BG20_104':'BG20_104_G',#Bonker	4
	'BG20_207':'BG20_207_G',#Dynamic Duo	4
	'BG20_106':'BG20_106_G',#Groundshaker	4
	'BG20_202':'BG20_202_G',#Necrolyte	4
	'BG20_302':'BG20_302_G',#Aggem Thorncurse	5
	'BG20_206':'BG20_206_G',#Captain Flat Tusk	6
	'BG20_303':'BG20_303_G',#Charlga	6	
	}

# BG20_GEM : blood gem

#Razorfen Geomancer	1　### OK ###
class BG20_100:# <12>[1453]
	""" Razorfen Geomancer
	[Battlecry:] Gain a[Blood Gem]. """
	play = Give(CONTROLLER, 'BG20_GEM')
	pass
class BG20_100_G:# <12>[1453]
	""" Razorfen Geomancer
	[Battlecry:] Gain 2[Blood Gems]. """
	play = Give(CONTROLLER, 'BG20_GEM') * 2
	pass



#Sun-Bacon Relaxer	1 ### OK ###
class BG20_301:# <12>[1453] コンガリ 
	""" Sun-Bacon Relaxer
	When you sell this, gain 2_[Blood Gems]. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BG20_GEM') * 2)
	pass
class BG20_301_G:# <12>[1453]
	""" Sun-Bacon Relaxer
	When you sell this, gain 4_[Blood Gems]. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BG20_GEM') * 4)
	pass




#Roadboar	2  ### OK ###
class BG20_101_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller=target.deepcopy_original
		Give(controller, card).trigger(controller)
class BG20_101:# <12>[1453]　
	""" Roadboar
	[Frenzy:] Gain a [Blood Gem]. """
	tags={GameTag.FRENZY:1, }
	#<ReferencedTag enumID="1637" name="FRENZY" type="Int" value="1"/>
	events = Damage(SELF).on(Frenzy(SELF,BG20_101_Action(CONTROLLER, 'BG20_GEM')))
	pass
class BG20_101_G:# <12>[1453]
	""" Roadboar
	[Frenzy:] Gain 2 [Blood Gems]. """
	tags={GameTag.FRENZY:1, }
	events = Damage(SELF).on(Frenzy(SELF,[BG20_101_Action(CONTROLLER, 'BG20_GEM'), BG20_101_Action(CONTROLLER, 'BG20_GEM')]))
	pass



#Tough Tusk	2 ### OK ###
class BG20_102:# <12>[1453]
	""" Tough Tusk
	After a [Blood Gem] is played on this, gain [Divine Shield] for the next combat. """
	events = ApplyGem(SELF).on(SetDivineShield(SELF), Buff(SELF,'BG20_102e'))
	pass
class BG20_102e:# <12>[1453]
	""" Toughened """
	events = BeginBar(CONTROLLER).on(SetDivineShield(OWNER, False),Destroy(SELF))
	pass
class BG20_102_G:# <12>[1453]
	""" Tough Tusk
	After a [Blood Gem] is played on this, gain[Divine Shield]. """
	events = ApplyGem(SELF).on(SetDivineShield(SELF),Buff(SELF,'BG20_102_Ge'))
	pass
class BG20_102_Ge:# <12>[1453]
	""" Real Tough
	[Divine Shield]. """
	events = BeginBar(CONTROLLER).on(SetDivineShield(OWNER, False),Destroy(SELF))
	pass



#Bannerboar	3  ### OK ###
class BG20_201:# <12>[1453]
	""" Bannerboar
	At the end of your turn, play a &lt;b&gt;Blood Gem&lt;/b&gt; on adjacent minions.
	"""
	events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT, 'BG20_GEM'))
	##At the end of your turn, play a [Blood Gem] on adjacent Quilboar. 
	##events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT + QUILBOAR, 'BG20_GEM'))
	pass
class BG20_201_G:# <12>[1453]
	""" Bannerboar
	At the end of your turn, play 2 &lt;b&gt;Blood Gems&lt;/b&gt; on adjacent minions.
	 """
	events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENTR, 'BG20_GEM'), ApplyGem(SELF_ADJACENT, 'BG20_GEM'))
	## At the end of your turn, play 2 [Blood Gems] on adjacent Quilboar.
	##events = OWN_TURN_END.on(ApplyGem(SELF_ADJACENT + QUILBOAR, 'BG20_GEM'), ApplyGem(SELF_ADJACENT + QUILBOAR, 'BG20_GEM'))
	pass



#Bristleback Brute	3   ### OK ###
class GB20_103_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if not target.gem_applied_thisturn:
			buff=target.buffs[-1]
			buff.atk+=3
			buff.max_health+=3
		pass
class BG20_103:# <12>[1453]
	""" Bristleback Brute
	The first [Blood Gem] played on this each turn gives an extra +3/+3. """
	events = ApplyGem(SELF).on(GB20_103_Action(SELF, 3))
	pass
class BG20_103_G:# <12>[1453]
	""" Bristleback Brute
	The first [Blood Gem] played on this each turn gives an extra +6/+6. """
	events = ApplyGem(SELF).on(GB20_103_Action(SELF, 6))
	pass



#Gemsplitter	3 ### OK ###
class BG21_037:# <12>[1453] 宝石割
	""" Gemsplitter
	After a friendly minion loses [Divine Shield], gain a_[Blood Gem]. """
	events = LoseDivineShield(FRIENDLY).on(Give(CONTROLLER, 'BG20_GEM'))
	pass
class BG21_037_G:# <12>[1453]
	""" Gemsplitter
	After a friendly minion loses [Divine Shield], gain 2_[Blood Gems]. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Give(CONTROLLER, 'BG20_GEM')*2)
	pass



#Thorncaller	3  ### OK ###
class GiveGemToOriginal(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		if target.deepcopy_original:
			Give(target.deepcopy_original,card).trigger(target.deepcopy_original)
class BG20_105:# <12>[1453] 荊使い
	""" Thorncaller
	[Battlecry and Deathrattle:] Gain a [Blood Gem]. """
	#<Tag enumID="217" name="DEATHRATTLE" type="Int" value="1"/>
	play = Give(CONTROLLER, 'BG20_GEM')
	deathrattle = GiveGemToOriginal(CONTROLLER, 'BG20_GEM')
	pass
class BG20_105_G:# <12>[1453]
	""" Thorncaller
	[Battlecry and Deathrattle:] Gain 2 [Blood Gems]. """
	play = Give(CONTROLLER, 'BG20_GEM')*2
	deathrattle = GiveGemToOriginal(CONTROLLER, 'BG20_GEM')*2
	pass



#Bonker	4  ### OK ###
class BG20_104:# <12>[1453]
	""" Bonker
	[Windfury]After this attacks, gain a [Blood Gem]. """
	events = Attack(SELF).after(GiveGemToOriginal(CONTROLLER, 'BG20_GEM'))
	pass
class BG20_104_G:# <12>[1453]
	""" Bonker
	[Mega-Windfury]After this attacks, gain a [Blood Gem]. """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>
	events = Attack(SELF).after(GiveGemToOriginal(CONTROLLER, 'BG20_GEM'))
	pass



#Dynamic Duo	4 ### OK ###
class BG20_207:# <12>[1453]
	""" Dynamic Duo
	[[Taunt].] After a [Blood Gem]is played on another Quilboar, gain +1/+1. """
	events = ApplyGem(FRIENDLY_MINIONS - SELF).on(Buff(SELF, 'BG20_207e'))
	pass
BG20_207e=buff(1,1)# <12>[1453]
""" Boar's Favor,+1/+1. """
class BG20_207_G:# <12>[1453]
	""" Dynamic Duo
	[[Taunt].] After a [Blood Gem]is played on anotherQuilboar, gain +2/+2. """
	events = ApplyGem(FRIENDLY_MINIONS - SELF).on(Buff(SELF, 'BG20_207_Ge'))
	pass
BG20_207_Ge=buff(2,2)# <12>[1453]
""" Boar's Favor,+2/+2. """



#Groundshaker	4  ## OK ###
class BG20_106:# <12>[1453]
	""" Groundshaker
	After a [Blood Gem] is played on this, give your other minions +2 Attack for next combat only. """
	events = ApplyGem(SELF).on(Buff(FRIENDLY_MINIONS - SELF, 'BG20_106e'))
	pass
class BG20_106e:# <12>[1453]
	""" Groundshook,	+@ Attack. """
	tags = {GameTag.ATK:2, }
	events = EndBattle(CONTROLLER).on(Destroy(SELF))
class BG20_106_G:# <12>[1453]
	""" Groundshaker
	After a [Blood Gem] is played on this, give your other minions +4 Attack for next combat only. """
	events = ApplyGem(SELF).on(
		Buff(FRIENDLY_MINIONS - SELF, 'BG20_106e'), 
		Buff(FRIENDLY_MINIONS - SELF, 'BG20_106e'))
	pass



#Necrolyte	4  ### OK ###
class BG20_202:# <12>[1453]
	""" Necrolyte
	[Battlecry:] Play 2 [BloodGems] on a friendly minion. It steals all [Blood Gems]from its neighbors. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,}
	play = ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		StealGem(TARGET, TARGET_ADJACENT)
	pass
class BG20_202_G:# <12>[1453]
	""" Necrolyte
	[Battlecry:] Play 4 [BloodGems] on a friendly minion.It steals all [Blood Gems]from its neighbors. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,}
	play = ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		ApplyGem(TARGET, 'BG20_GEM'),\
		StealGem(TARGET, TARGET_ADJACENT)
	pass



#Aggem Thorncurse	5  ### OK ###
class BG20_302_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		controller = target
		field = controller.field
		flag = [0] * len(field)
		ret = []
		while True:
			if sum(flag)==len(field):
				break
			c =random.choice(field)
			addOK=True
			for d in ret:
				if c.race == d.race:
					flag[field.index(c)]=1
					addOK=False
					continue
			if addOK:
				flag[field.index(c)]=1
				if c.race != Race.INVALID:
					ret.append(c)
			pass
		for c in ret:
			Buff(c,buff).trigger(source)
class BG20_302:# <12>[1453]　そーんかーす
	""" Aggem Thorncurse
	After a [Blood Gem] is played on this, give a friendly minion of each minion type +1/+1. """
	events = ApplyGem(SELF).on(BG20_302_Action(CONTROLLER, 'BG20_302e'))
	pass
BG20_302e=buff(1,1)# <12>[1453]
""" Thorncursed
+1/+1 """
class BG20_302_G:# <12>[1453]
	""" Aggem Thorncurse
	After a [Blood Gem] is played on this, give a friendly minion of each minion type +2/+2. """
	events = ApplyGem(SELF).on(BG20_302_Action(CONTROLLER, 'BG20_302_Ge'))
	pass
BG20_302_Ge=buff(2,2)# <12>[1453]
""" Thorncursed
+2/+2 """





#Captain Flat Tusk	6  ### OK ###
class BG20_206_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		if controller.spentmoney_in_this_turn>=4:
			for repeat in range(amount):
				Give(controller,'BG20_GEM').trigger(source)
			controller.spentmoney_in_this_turn -= 4
class BG20_206:# <12>[1453]
	""" Captain Flat Tusk
	After you spend 4 Gold, gain a [Blood Gem].<i>(@ Gold left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_206_Action(CONTROLLER, 1)),
		Rerole(CONTROLLER).on(BG20_206_Action(CONTROLLER, 1)),
		UpgradeTier(CONTROLLER).on(BG20_206_Action(CONTROLLER, 1)),
		]
	pass
class BG20_206_G:# <12>[1453]
	""" Captain Flat Tusk
	After you spend 4 Gold,gain 2 [Blood Gems].<i>(@ Gold left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_206_Action(CONTROLLER, 2)),
		Rerole(CONTROLLER).on(BG20_206_Action(CONTROLLER, 2)),
		UpgradeTier(CONTROLLER).on(BG20_206_Action(CONTROLLER, 2)),
		]
	pass


#Charlga	6 ### OK ###
class BG20_303:# <12>[1453] ちゃるが
	""" Charlga
	At the end of your turn, play a [Blood Gem] on all friendly minions. """
	events = OWN_TURN_END.on(ApplyGem(FRIENDLY_MINIONS, 'BG20_GEM'))
	pass

class BG20_303_G:# <12>[1453]
	""" Charlga
	At the end of your turn, play 2 [Blood Gems] on all friendly minions. """
	events = OWN_TURN_END.on(ApplyGem(FRIENDLY_MINIONS, 'BG20_GEM')*2)
	pass

