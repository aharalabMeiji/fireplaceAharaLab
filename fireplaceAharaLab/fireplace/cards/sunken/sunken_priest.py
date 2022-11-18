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
	def play(self):
		for card in self.controller.field + self.controller.opponent.field:
			for c in reversed(self.controller.hand + self.controller.opponent.hand):
				if c.id==card.id:
					c.discard()## no Deathrattle
			for c in reversed(self.controller.deck + self.controller.opponent.deck):
				if c.id==card.id:
					c.discard()## no Deathrattle
		for card in reversed(self.controller.field + self.controller.opponent.field):
			if card!=self:
				Destroy(c).trigger(self)## with Deathrattle
		Deaths().trigger(self)
	pass




if Sunken_Illuminate:# 
	Sunken_Priest+=['TSC_210']
class TSC_210_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("DredgeChoice.choose","%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if c.type==CardType.SPELL:
					c.cost=max(c.cost-3,0)
				break
		pass
class TSC_210_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_210_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_210:# <6>[1658]
	""" Illuminate
	[Dredge]. If it's a spell,reduce its Cost by (3). """
	play = TSC_210_Dredge(CONTROLLER)
	pass




if Sunken_Whispers_of_the_Deep:# 
	Sunken_Priest+=['TSC_211']
class TSC_211:# <6>[1658]
	""" Whispers of the Deep
	[Silence] a friendly minion,then deal damage equal to its Attack randomly split
	among all enemy minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Silence(TARGET), SplitHit(CONTROLLER, ENEMY_MINIONS, ATK(Silence.TARGET))
	pass




if Sunken_Handmaiden:# 
	Sunken_Priest+=['TSC_212']
class TSC_212:# <6>[1658]
	""" Handmaiden
	[Battlecry:] If you've cast three spells while holding this, draw 3 cards.@<i>({0} left!)</i>@<i>(Ready!)</i> """
	class Hand:
		events = Play(CONTROLLER, SPELL).on(SidequestCounter(SELF, 3, [Draw(CONTROLLER),Draw(CONTROLLER),Draw(CONTROLLER),]))
	pass




if Sunken_Queensguard:# 
	Sunken_Priest+=['TSC_213']
	Sunken_Priest+=['TSC_213e']
class TSC_213:# <6>[1658]
	""" Queensguard
	[Battlecry:] Gain +1/+1 for each spell you've cast this turn. """
	def play(self):
		cards=[card for card in self.controller.play_this_turn if card.type==CardType.SPELL]
		amount=len(cards)
		if amount>0:
			Buff(self, 'TSC_213e', atk=amount, max_health=amount).trigger(self)
	pass
class TSC_213e:# <6>[1658]
	""" Tides Call 	Increased stats. """
	pass




if Sunken_Serpent_Wig:# 
	Sunken_Priest+=['TSC_215']
	Sunken_Priest+=['TSC_215e']
class TSC_215:# <6>[1658]
	""" Serpent Wig
	Give a minion +1/+2. If you played a Naga while holding this, add a Serpent Wig to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'TSC_215e')#
	class Hand:
		events = Play(CONTROLLER, NAGA).after(Give(CONTROLLER, 'TSC_215'))
	pass
TSC_215e=buff(1,2)




if Sunken_Blackwater_Behemoth:# 
	Sunken_Priest+=['TSC_216']
	Sunken_Priest+=['TSC_216t']
class TSC_216:# <6>[1658]
	""" Blackwater Behemoth
	[Colossal +1][Lifesteal] """
	play = Summon(CONTROLLER, 'TSC_216t')#
	pass

class TSC_216t:# <6>[1658]
	""" Behemoth's Lure
	At the end of your turn,force a random enemy minion to attack the__Blackwater Behemoth. """
	events = OWN_TURN_END.on(RegularAttack(RANDOM(ENEMY_MINIONS), FRIENDLY_MINIONS+ID('TSC_216')))
	pass




if Sunken_Switcheroo:# 
	Sunken_Priest+=['TSC_702']
	Sunken_Priest+=['TSC_702e']
class TSC_702:# <6>[1658]
	""" Switcheroo
	Draw 2 minions. Swap their Health. """
	def play(self):
		cards=[card for card in self.controller.deck if card.type==CardType.MINION]
		if len(cards)>=2:
			cards=random.sample(cards, 2)
			card1=Give(self.controller, cards[0]).trigger(self)#
			if card1[0]==[]:
				return
			card1=card1[0][0]
			card2=Give(self.controller, cards[1]).trigger(self)#
			if card2[0]==[]:
				return
			card2=card2[0][0]
			diff = card1.max_health-card2.max_health
			Buff(card1, 'TSC_702e', max_health=-diff).trigger(self)
			Buff(card2, 'TSC_702e', max_health=diff).trigger(self)
	pass
class TSC_702e:# <6>[1658]
	""" Switcheroo'd Swapped Health. """
	pass




if Sunken_Azsharan_Ritual:# 
	Sunken_Priest+=['TSC_775']
	Sunken_Priest+=['TSC_775t']
class TSC_775:# <6>[1658]
	""" Azsharan Ritual
	[Silence] a minion and summon a copy of it. Put a 'Sunken Ritual' on the bottom of your deck. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	play = Silence(TARGET), Summon(CONTROLLER, Copy(TARGET)), ShuffleBottom(CONTROLLER, 'TSC_775t')#
	pass
class TSC_775t:# <6>[1658]
	""" Sunken Ritual
	[Silence] a minion and summon 2 copies of it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	play = Silence(TARGET), Summon(CONTROLLER, Copy(TARGET)), Summon(CONTROLLER, Copy(TARGET))	
	pass




if Sunken_Priestess_Valishj:# 
	Sunken_Priest+=['TSC_828']
class TSC_828:# <6>[1658]	
	""" Priestess Valishj	
	[Battlecry:] Refresh an empty Mana Crystal for each spell___you've cast this turn.@ <i>(@)</i> """
	def play(self):
		cards=[card for card in self.controller.play_this_turn if card.type==CardType.SPELL]
		if len(cards)>0:
			RefreshMana(self.controller,len(cards)).trigger(self)
	pass

