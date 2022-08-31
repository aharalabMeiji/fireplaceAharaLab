from ..utils import *

Sunken_Priest=[]


Sunken_Herald_of_Light=True  ####
Sunken_Disarming_Elemental=True  ####
Sunken_Drown=True  ####
Sunken_Whirlpool=True  ####
Sunken_Illuminate=True  ####
Sunken_Whispers_of_the_Deep=True  ####
Sunken_Handmaiden=True  ####
Sunken_Queensguard=True  ####
Sunken_Serpent_Wig=True  ####
Sunken_Blackwater_Behemoth=True  ####
Sunken_Switcheroo=True  ####
Sunken_Azsharan_Ritual=True  ####
Sunken_Priestess_Valishj=True  ####



if Sunken_Herald_of_Light:# 
	Sunken_Priest+=['TID_085']
class TID_085:# <6>[1658]
	""" Herald of Light
	[Battlecry:] If you've cast a Holy spell while holding this,restore #6 Health to all friendly characters. """
	class Hand:
		events = Play(CONTROLLER, SPELL+HOLY).on(Heal(FRIENDLY_CHARACTERS, 6))
	pass




if Sunken_Disarming_Elemental:# 
	Sunken_Priest+=['TID_700']
	Sunken_Priest+=['TID_700e']
class TID_700_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("TID_700_DredgeChoice.choose","%s chooses %r"%(card.controller.opponent.name, card))
		opponent = card.controller
		for c in opponent.deck[:3]:
			if card.id==c.id:
				opponent.deck.remove(c)
				opponent.deck.append(c)
				Buff(c,'TID_700e').trigger(card.controller.opponent)
				break
		pass
class TID_700_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.opponent.deck[:3]]
		TID_700_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TID_700:# <6>[1658]
	""" Disarming Elemental
	[Battlecry:] [Dredge] for your opponent. Set its Cost to (6). """
	play = TID_700_Dredge(CONTROLLER)
	pass

class TID_700e:# <6>[1658]
	""" Disarmed
	Costs (6). """
	cost = lambda self,i:6
	pass




if Sunken_Drown:# 
	Sunken_Priest+=['TID_920']
class TID_920:# <6>[1658]
	""" Drown
	Put an enemy minion on the bottom of your deck. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	def play(self):
		target=self.target
		target.zone=Zone.SETASIDE
		target.controller=self.controller
		target.zone = Zone.DECK
		self.controller.shiftdown_deck()## make the top card to botom
	pass




if Sunken_Whirlpool:# 
	Sunken_Priest+=['TSC_209']
class TSC_209:# <6>[1658]
	""" Whirlpool
	Destroy all minions and all copies of them <i>(wherever they are)</i>. """
	#
	pass




if Sunken_Illuminate:# 
	Sunken_Priest+=['TSC_210']
class TSC_210:# <6>[1658]
	""" Illuminate
	[Dredge]. If it's a spell,reduce its Cost by (3). """
	#
	pass




if Sunken_Whispers_of_the_Deep:# 
	Sunken_Priest+=['TSC_211']
class TSC_211:# <6>[1658]
	""" Whispers of the Deep
	[Silence] a friendly minion,then deal damage equal toits Attack randomly splitamong all enemy minions. """
	#
	pass




if Sunken_Handmaiden:# 
	Sunken_Priest+=['TSC_212']
class TSC_212:# <6>[1658]
	""" Handmaiden
	[Battlecry:] If you've castthree spells while holdingthis, draw 3 cards.@<i>({0} left!)</i>@<i>(Ready!)</i> """
	#
	pass




if Sunken_Queensguard:# 
	Sunken_Priest+=['TSC_213']

	Sunken_Priest+=['TSC_213e']
class TSC_213:# <6>[1658]
	""" Queensguard
	[Battlecry:] Gain +1/+1for each spell you've cast this turn. """
	#
	pass

class TSC_213e:# <6>[1658]
	""" Tides Call
	Increased stats. """
	#
	pass




if Sunken_Serpent_Wig:# 
	Sunken_Priest+=['TSC_215']

	Sunken_Priest+=['TSC_215e']
class TSC_215:# <6>[1658]
	""" Serpent Wig
	Give a minion +1/+2.If you played a Naga whileholding this, add a SerpentWig to your hand. """
	#
	pass

class TSC_215e:# <6>[1658]
	""" Snakes for Hair
	+1/+2. """
	#
	pass




if Sunken_Blackwater_Behemoth:# 
	Sunken_Priest+=['TSC_216']

	Sunken_Priest+=['TSC_216t']
class TSC_216:# <6>[1658]
	""" Blackwater Behemoth
	[Colossal +1][Lifesteal] """
	#
	pass

class TSC_216t:# <6>[1658]
	""" Behemoth's Lure
	At the end of your turn,force a random enemyminion to attack the__Blackwater Behemoth. """
	#
	pass




if Sunken_Switcheroo:# 
	Sunken_Priest+=['TSC_702']

	Sunken_Priest+=['TSC_702e']
class TSC_702:# <6>[1658]
	""" Switcheroo
	Draw 2 minions.Swap their Health. """
	#
	pass

class TSC_702e:# <6>[1658]
	""" Switcheroo'd
	Swapped Health. """
	#
	pass




if Sunken_Azsharan_Ritual:# 
	Sunken_Priest+=['TSC_775']

	Sunken_Priest+=['TSC_775t']
class TSC_775:# <6>[1658]
	""" Azsharan Ritual
	[Silence] a minion and summon a copy of it. Put a 'Sunken Ritual' on the bottom of your deck. """
	#
	pass

class TSC_775t:# <6>[1658]
	""" Sunken Ritual
	[Silence] a minion and summon 2 copies of it. """
	#
	pass




if Sunken_Priestess_Valishj:# 
	Sunken_Priest+=['TSC_828']
class TSC_828:# <6>[1658]
	""" Priestess Valishj
	[Battlecry:] Refresh an emptyMana Crystal for each spell___you've cast this turn.@ <i>(@)</i> """
	#
	pass

