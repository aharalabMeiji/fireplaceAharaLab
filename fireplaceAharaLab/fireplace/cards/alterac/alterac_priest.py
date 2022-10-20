from ..utils import *

Alterac_Priest=[]

Alterac_Xyrella_the_Devout=True
Alterac_Deliverance=True
Alterac_Shadow_Word_Devour=True
Alterac_Undying_Disciple=True
Alterac_Luminous_Geode=True
Alterac_Spirit_Guide=True
Alterac_Bless=True
Alterac_Gift_of_the_Naaru=True
Alterac_Najak_Hexxen=True
Alterac_Stormpike_Aid_Station=True
Alterac_Horn_of_Wrathion=True
Alterac_Lightmaw_Netherdrake=True
Alterac_Mida_Pure_Light=True


if Alterac_Xyrella_the_Devout:# 
	Alterac_Priest+=['AV_207']
	Alterac_Priest+=['AV_207p']
	Alterac_Priest+=['AV_207p2']
class AV_207:# <6>[1626]
	""" Xyrella, the Devout
	[Battlecry:] Trigger the [Deathrattle] of every friendly minion that died this game. """
	def play(self):
		cards = [card for card in self.controller.graveyard if card.type==CardType.MINION and card.has_deathrattle==True]
		for card in cards:
			for deathrattle in card.deathrattles:
				deathrattle.trigger(self)
	pass

class AV_207p:# <6>[1626]
	""" Holy Touch
	[Hero Power] Restore #5 Health. Flip each turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,  }
	activate = Heal(TARGET, 5), ChangeHeroPower(CONTROLLER, 'AV_207p2')
	pass

class AV_207p2:# <6>[1626]
	""" Void Spike
	[Hero Power] Deal $5 damage. Flip each turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,  }
	activate = Hit(TARGET, 5), ChangeHeroPower(CONTROLLER, 'AV_207p')
	pass

if Alterac_Deliverance:# 
	Alterac_Priest+=['AV_315']
	Alterac_Priest+=['AV_315e2']
class AV_315:# <6>[1626]
	""" Deliverance
	Deal $3 damage to a minion. [Honorable Kill:] Summon a new 3/3 copy of it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3).on(Honorable_kill(Hit.TARGET, Hit.AMOUNT, [Summon(CONTROLLER, Hit.TARGET).after(Buff(Summon.CARD, 'AV_315e2'))]))
	pass

class AV_315e2:# <6>[1626]
	""" Salvation	Attack and Health set to 3. """
	atk = lambda self,i: 3
	max_health = lambda self,i: 3
	pass

if Alterac_Shadow_Word_Devour:# 
	Alterac_Priest+=['AV_324']
	Alterac_Priest+=['AV_324e2']
	#Alterac_Priest+=['AV_324e2b']
	Alterac_Priest+=['AV_324e3']
	#Alterac_Priest+=['AV_324eb']
class AV_324:# <6>[1626]
	""" Shadow Word: Devour
	Choose a minion. It steals 1 Health from _ALL other minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	def play(self):#
		target = self.target
		amount = len(self.controller.field)+len(self.controller.opponent.field)-1
		for card in self.controller.field:
			if card != target:
				Buff(card, 'AV_324e3').trigger(self)
		for card in self.controller.opponent.field:
			Buff(card, 'AV_324e3').trigger(self)
		Buff(target, 'AV_324e2', max_health=amount).trigger(self)
	pass

class AV_324e2:# <6>[1626]
	""" Superior
	Increased Health. """
	pass
class AV_324e3:# <6>[1626]
	""" Inferior
	Reduced Health. """
	max_health = lambda self, i:i-1
	pass

if Alterac_Undying_Disciple:# 
	Alterac_Priest+=['AV_325']
class AV_325:# <6>[1626]
	""" Undying Disciple
	[Taunt] [Deathrattle:] Deal damage equal to this minion's Attack to all enemy minions. """
	deathrattle = Hit(ENEMY_MINIONS, ATK(SELF))
	pass

if Alterac_Luminous_Geode:# 
	Alterac_Priest+=['AV_326']
	Alterac_Priest+=['AV_326e']
class AV_326:# <6>[1626]
	""" Luminous Geode
	After a friendly minion is healed, give it +2 Attack. """
	events = Heal(FRIENDLY_MINIONS).on(Buff(Heal.TARGET, 'AV_326e'))
	pass
AV_326e=buff(2,0)

if Alterac_Spirit_Guide:# 
	Alterac_Priest+=['AV_328']
class AV_328:# <6>[1626]
	""" Spirit Guide
	[Taunt] [Deathrattle:] Draw a Holy spell and a Shadow spell. """
	deathrattle = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + HOLY)), Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SHADOW))
	pass

if Alterac_Bless:# 
	Alterac_Priest+=['AV_329']
	Alterac_Priest+=['AV_329e']
	Alterac_Priest+=['AV_329e2']
class AV_329:# <6>[1626]
	""" Bless
	Give a minion +2 Health, then set its Attack to be equal to its Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	def play(self):
		Buff(self.target, 'AV_329e2').trigger(self) #
		amount = self.target.health - self.target.atk
		Buff(self.target, 'AV_329e', atk=amount).trigger(self)
	pass
class AV_329e:# <6>[1626]
	""" Blessed
	+2 Health and this minion's Attack is equal to its Health. """
	pass
AV_329e2=buff(0,2)

if Alterac_Gift_of_the_Naaru:# 
	Alterac_Priest+=['AV_330']
class AV_330:# <6>[1626]
	""" Gift of the Naaru
	Restore #3 Health to all characters. If any are still damaged, draw a card. """
	def play(self):
		#all_characters = self.controller.field+self.controller.opponent.field+[self.controller.hero, self.controller.opponent.hero]
		all_characters=[card for card in self.controller.game.characters if card.type==CardType.MINION or card.type==CardType.HERO]
		for card in all_characters:
			Heal(card, 3).trigger(self)
		for card in all_characters:
			if hasattr(card, 'damaged') and card.damaged>0:
				Draw(self.controller).trigger(self)
				return
	pass

if Alterac_Najak_Hexxen:# 
	Alterac_Priest+=['AV_331']
	Alterac_Priest+=['AV_331e']
	Alterac_Priest+=['AV_331e2']
class AV_331_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target!=None:
			target.zone=Zone.SETASIDE
			target.controller=self.controller.opponent
			target.zone.Zone.PLAY
			#how about its buffs?
		pass

class AV_331:# <6>[1626]
	""" Najak Hexxen
	[Battlecry:] Take control of an enemy minion. [Deathrattle:] Give the minion back. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	def play(self):
		self.target.zone=Zone.SETASIDE
		self.target.controller=self.controller
		self.target.zone=Zone.PLAY
		#how about its buffs?
	deathrattle = AV_331_Action(TARGET)
	pass
class AV_331e:# <6>[1626]
	""" Dark Concoction
	Give this back when Najak is destroyed. """
	
	pass

class AV_331e2:# <6>[1626]
	""" Dark Concoction
	Took control of {0}. """
	#
	pass

if Alterac_Stormpike_Aid_Station:# 
	Alterac_Priest+=['AV_664']
	Alterac_Priest+=['AV_664e2']
class AV_664:# <6>[1626]
	""" Stormpike Aid Station
	At the end of your turn, give your minions +2 Health. Lasts 3 turns. """
	events = [
		OWN_TURN_END.on(Buff(FRIENDLY_MINIONS, 'AV_664e2')),
		OWN_TURN_END.on(SidequestCounter(SELF, 3, [Destroy(SELF)]))
		]
	pass
AV_664e2=buff(0,2)

if Alterac_Horn_of_Wrathion:# 
	Alterac_Priest+=['ONY_017']
class ONY_017:# <6>[1626]
	""" Horn of Wrathion
	Draw a minion. If it's a Dragon, summon two 2/1 Whelps(ONY_001t) with [Rush]. """
	def play(self):
		newcard=Draw(self.controller).trigger(self)
		newcard=newcard[0][0]
		if newcard.type==CardType.MINION and newcard.race==Race.DRAGON:
			Summon(self.controller, 'ONY_001t').trigger(self)
			Summon(self.controller, 'ONY_001t').trigger(self)
	pass

if Alterac_Lightmaw_Netherdrake:# 
	Alterac_Priest+=['ONY_026']
class ONY_026:# <6>[1626]
	""" Lightmaw Netherdrake
	[Battlecry:] If you're holding a Holy and a Shadow spell, deal 3 damage to all other minions. """
	def play(self):
		cards1=[card for card in self.controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.HOLY]
		cards2=[card for card in self.controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.SHADOW]
		if cards1!=[] and cards2!=[]:
			for card in self.controller.field+self.controller.opponent.field:
				if card!=self:
					Hit(card, 3).trigger(self)
	pass

if Alterac_Mida_Pure_Light:# 
	Alterac_Priest+=['ONY_028']
	Alterac_Priest+=['ONY_028t']
class ONY_028:# <6>[1626]
	""" Mi'da, Pure Light
	[Divine Shield], [Lifesteal] [Deathrattle:] Shuffle a Fragment into your deck that resummons Mi'da when drawn. """
	deathrattle = Shuffle(CONTROLLER, 'ONY_028t')
	pass

class ONY_028t:# <6>[1626]
	""" Fragment of Mi'da
	[Casts When Drawn] Summon Mi'da, Pure Light. """
	play = Summon(CONTROLLER, 'ONY_028')
	pass


