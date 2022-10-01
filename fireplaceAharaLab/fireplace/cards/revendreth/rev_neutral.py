from ..utils import *

Rev_Neutral=[]

Rev_Soul_Seeker=True## new 24.4
Rev_Afterlife_Attendant=True## new 24.4
Rev_Tight_Lipped_Witness=True## new 24.4
Rev_Sylvanas_the_Accused=True## new 24.4
Rev_The_Jailer=True## new 24.4
Rev_Bog_Beast=True
Rev_Stoneborn_Accuser=True
Rev_Red_Herring=True
Rev_Masked_Reveler=True
Rev_Crooked_Cook=True
Rev_Insatiable_Devourer=True
Rev_Prince_Renathal=True
Rev_Famished_Fool=True
Rev_Dinner_Performer=True
Rev_Kaelthas_Sinstrider=True
Rev_Murloc_Holmes=True
Rev_Demolition_Renovator=True
Rev_Theotar_the_Mad_Duke=True
Rev_Sinrunner=True
Rev_Maze_Guide=True
Rev_Dredger_Staff=True
Rev_Roosting_Gargoyle=True
Rev_Party_Crasher=True
Rev_Stoneborn_General=True
Rev_Invitation_Courier=True
Rev_Forensic_Duster=True
Rev_Cosmic_Power=True
Rev_Murloc_Holmes=True
Rev_Investigate=True
Rev_Muck_Plumber=True
Rev_Sinstone_Totem=True
Rev_Anonymous_Informant=True
Rev_Sinfueled_Golem=True
Rev_Volatile_Skeleton=True
Rev_Scuttlebutt_Ghoul=True
Rev_Dispossessed_Soul=True
Rev_Sire_Denathrius=True
Rev_Creepy_Painting=True
Rev_Sketchy_Stranger=True
Rev_Steamcleaner=True
Rev_Priest_of_the_Deceased=True
Rev_Murlocula=True
Rev_Ashen_Elemental=True


if Rev_Soul_Seeker:# 
	Rev_Neutral+=['MAW_004']
class MAW_004_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		opponent=controller.opponent
		if len(opponent.deck)>0:
			mycard=source
			hiscard=random.choice(opponent.deck)
			mycard.zone=Zone.SETASIDE
			hiscard.zone=Zone.SETASIDE
			mycard.controller=opponent
			hiscard.controller=controller
			mycard.zone=Zone.DECK
			Summon(controller, hiscard).trigger(source)
		pass
class MAW_004:# <12>[1691]
	""" Soul Seeker
	<b>Battlecry:</b> Swap this with a random minion from your opponent's deck. """
	play = MAW_004_Action(CONTROLLER)
	pass





if Rev_Afterlife_Attendant:# 
	Rev_Neutral+=['MAW_031']
	Rev_Neutral+=['MAW_031e']
class MAW_031_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
class MAW_031:# <12>[1691]
	""" Afterlife Attendant
	Your <b>Infuse</b> cards also <b>Infuse</b> while in your deck. """
	#
	pass

class MAW_031e:# <12>[1691]
	""" Afterlife
	Your <b>Infuse</b> cards also <b>Infuse</b> in your deck. """
	#
	pass





if Rev_Tight_Lipped_Witness:# 
	Rev_Neutral+=['MAW_032']
class MAW_032:# <12>[1691]
	""" Tight-Lipped Witness
	<b>Secrets</b> can't be revealed. """
	#
	pass





if Rev_Sylvanas_the_Accused:# 
	Rev_Neutral+=['MAW_033']
	Rev_Neutral+=['MAW_033t']
class MAW_033:# <12>[1691]
	""" Sylvanas, the Accused
	<b>Battlecry:</b> Destroy an enemy minion. 
	<b>Infuse (@):</b> Take control of it instead. """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="7"/>
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Destroy(TARGET)
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'MAW_033t'))
	pass
class MAW_033t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		assert target.type==CardType.MINION
		assert target.zone==Zone.PLAY
		target.zone=Zone.SETASIDE
		target.controller=source.controller
		target.zone=Zone.PLAY
		pass
class MAW_033t:# <12>[1691]
	""" Sylvanas, the Accused
	<b>Infused</b> <b>Battlecry:</b> Take control of an enemy minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = MAW_033t_Action(TARGET)
	#
	pass





if Rev_The_Jailer:# 
	Rev_Neutral+=['MAW_034']
	Rev_Neutral+=['MAW_034e']
	Rev_Neutral+=['MAW_034e2']
class MAW_034:# <12>[1691]
	""" The Jailer
	<b>Battlecry:</b> Destroy your  deck. For the rest of the game, your minions are <b>Immune</b>. """
	#
	pass

class MAW_034e:# <12>[1691]
	""" Mawsworn
	Your minions are <b>Immune</b> """
	#
	pass

class MAW_034e2:# <12>[1691]
	""" Mawsworn
	Can't die. """
	#
	pass




if Rev_Bog_Beast:# 
	Rev_Neutral+=['REV_012']
	Rev_Neutral+=['REV_012t']
class REV_012:# <12>[1691]
	""" Bog Beast
	<b><b>Taunt</b></b>  <b>Deathrattle:</b> Summon a 2/4  Muckmare with <b>Taunt</b>. """
	#
	pass

class REV_012t:# <12>[1691]
	""" Muckmare
	<b>Taunt</b> """
	#
	pass



if Rev_Stoneborn_Accuser:# ### OK ###
	Rev_Neutral+=['REV_013']
	Rev_Neutral+=['REV_013t']
class REV_013:# <12>[1691]
	""" Stoneborn Accuser
	<b>Infuse (@):</b> Gain "<b>Battlecry:</b> Deal 5 damage." """
	#<Tag enumID="2456" name="INFUSE" type="Int" value="1"/>
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="5"/>
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_013t'))
	pass

class REV_013t:# <12>[1691]
	""" Stoneborn Accuser
	<b>Infused</b> <b>Battlecry:</b> Deal 5 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 5)
	pass





if Rev_Red_Herring:# 
	Rev_Neutral+=['REV_014']
class REV_014:# <12>[1691]
	""" Red Herring
	<b>Taunt</b> Your non-Red Herring minions have <b>Stealth</b>. """
	#
	pass





if Rev_Masked_Reveler:# 
	Rev_Neutral+=['REV_015']
	Rev_Neutral+=['REV_015t']
class REV_015:# <12>[1691]
	""" Masked Reveler
	<b>Rush</b> <b>Deathrattle:</b> Summon a 2/2 copy of another minion in your deck. """
	#
	pass

class REV_015t:# <12>[1691]
	""" Masked
	2/2. """
	#
	pass





if Rev_Crooked_Cook:# 
	Rev_Neutral+=['REV_016']
	Rev_Neutral+=['REV_016e']
class REV_016:# <12>[1691]
	""" Crooked Cook
	At the end of your turn,  if you dealt 3 or more  damage to the enemy  hero, draw a card. """
	#
	pass

class REV_016e:# <12>[1691]
	""" Suspicious Soup
	<b>Poisonous</b> """
	#
	pass





if Rev_Insatiable_Devourer:# ### OK ###
	Rev_Neutral+=['REV_017']
	Rev_Neutral+=['REV_017e']
	Rev_Neutral+=['REV_017t']
class REV_017:# <12>[1691]
	""" Insatiable Devourer
	<b>Battlecry:</b> Devour an enemy  minion and gain its stats.  _
	<b>Infuse (@):</b> And its neighbors. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = EatsMinion(SELF, TARGET, 1, 'REV_017e')#
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_017t'))
	pass
class REV_017e:# <12>[1691]
	""" Satiated
	Increased Stats """
	#
	pass
class REV_017t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		if target in controller.opponent.field:
			index = controller.opponent.field.index(target)
			EatsMinion(source, controller.opponent.field[index+1], 1, 'REV_017e').trigger(source)
			EatsMinion(source, target, 1, 'REV_017e').trigger(source)
			if index>0:
				EatsMinion(source, controller.opponent.field[index-1], 1, 'REV_017e').trigger(source)
		pass
class REV_017t:# <12>[1691]
	""" Insatiable Devourer
	<b>Infused</b> <b>Battlecry:</b> Devour an enemy minion and its neighbors to gain their stats. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play=REV_017t_Action(TARGET)
	pass





if Rev_Prince_Renathal:# 
	Rev_Neutral+=['REV_018']
class REV_018:# <12>[1691]
	""" Prince Renathal
	Your deck size and  starting Health are 40. """
	#
	pass





if Rev_Famished_Fool:# 
	Rev_Neutral+=['REV_019']
	Rev_Neutral+=['REV_019t']
class REV_019:# <12>[1691]
	""" Famished Fool
	<b>Battlecry:</b> Draw a card. <b>Infuse (@):</b> Draw 3 instead. """
	#
	pass

class REV_019t:# <12>[1691]
	""" Famished Fool
	<b>Infused</b> <b>Battlecry:</b> Draw 3 cards. """
	#
	pass





if Rev_Dinner_Performer:# 
	Rev_Neutral+=['REV_020']
class REV_020:# <12>[1691]
	""" Dinner Performer
	<b>Battlecry:</b> Summon a random minion from your deck that you can afford to play. """
	#
	pass





if Rev_Kaelthas_Sinstrider:# 
	Rev_Neutral+=['REV_021']
	Rev_Neutral+=['REV_021e']
class REV_021:# <12>[1691]
	""" Kael'thas Sinstrider
	Every third minion you play each turn costs (0). """
	#
	pass

class REV_021e:# <12>[1691]
	""" Sinstrider
	Costs (0). """
	#
	pass





if Rev_Murloc_Holmes:# 
	Rev_Neutral+=['REV_022']
class REV_022:# <12>[1691]
	""" Murloc Holmes
	<b>Battlecry:</b> Solve 3 Clues  about your opponent's cards  to get copies of them. """
	#
	pass





if Rev_Demolition_Renovator:# 
	Rev_Neutral+=['REV_023']
class REV_023:# <12>[1691]
	""" Demolition Renovator
	<b>Battlecry:</b> Destroy  an enemy location. """
	#
	pass





if Rev_Theotar_the_Mad_Duke:# 
	Rev_Neutral+=['REV_238']
class REV_238:# <12>[1691]
	""" Theotar, the Mad Duke
	<b>Battlecry:</b> <b>Discover</b> a card in each player's hand and swap them. """
	#
	pass





if Rev_Sinrunner:# 
	Rev_Neutral+=['REV_251']
class REV_251:# <12>[1691]
	""" Sinrunner
	<b>Deathrattle:</b> Destroy a random enemy minion. """
	#
	pass





if Rev_Maze_Guide:# 
	Rev_Neutral+=['REV_308']
class REV_308:# <12>[1691]
	""" Maze Guide
	<b>Battlecry</b>: Summon a random 2-Cost minion. """
	#
	pass





if Rev_Dredger_Staff:# 
	Rev_Neutral+=['REV_338']
	Rev_Neutral+=['REV_338e']
class REV_338:# <12>[1691]
	""" Dredger Staff
	<b>Battlecry:</b> Give minions  in your hand +1 Health. """
	#
	pass

class REV_338e:# <12>[1691]
	""" Carving Time
	+1 Health. """
	#
	pass





if Rev_Roosting_Gargoyle:# 
	Rev_Neutral+=['REV_351']
	Rev_Neutral+=['REV_351e']
class REV_351:# <12>[1691]
	""" Roosting Gargoyle
	<b>Battlecry:</b> Give a friendly Beast +2 Attack. """
	#
	pass

class REV_351e:# <12>[1691]
	""" Invigorated
	+2 Attack. """
	#
	pass





if Rev_Party_Crasher:# 
	Rev_Neutral+=['REV_370']
class REV_370:# <12>[1691]
	""" Party Crasher
	<b>Battlecry:</b> Choose an enemy minion. Throw a random minion from your hand at it. """
	#
	pass





if Rev_Stoneborn_General:# 
	Rev_Neutral+=['REV_375']
	Rev_Neutral+=['REV_375t']
class REV_375:# <12>[1691]
	""" Stoneborn General
	<b>Rush</b>  __<b>Deathrattle:</b> Summon an  ___8/8 Gravewing with <b>Rush</b>._ """
	#
	pass

class REV_375t:# <12>[1691]
	""" Gravewing
	<b>Rush</b> """
	#
	pass





if Rev_Invitation_Courier:# 
	Rev_Neutral+=['REV_377']
class REV_377:# <12>[1691]
	""" Invitation Courier
	After a card is added to your hand from another class, copy it. """
	#
	pass





if Rev_Forensic_Duster:# 
	Rev_Neutral+=['REV_378']
	Rev_Neutral+=['REV_378e']
	Rev_Neutral+=['REV_378e2']
class REV_378:# <12>[1691]
	""" Forensic Duster
	<b>Battlecry:</b> Your  opponent's minions  cost (1) more next turn. """
	#
	pass

class REV_378e:# <12>[1691]
	""" Dusting
	Your minions cost (1) more this turn. """
	#
	pass

class REV_378e2:# <12>[1691]
	""" Discovered!
	Costs (1) more. """
	#
	pass





if Rev_Murloc_Holmes:# 
	Rev_Neutral+=['REV_770']
	Rev_Neutral+=['REV_770hp']
class REV_770:# <12>[1691]
	""" Murloc Holmes	 """
	#
	pass

class REV_770hp:# <12>[1691]
	""" Accuse
	<b>Hero Power</b> Make an accusation! """
	#
	pass





if Rev_Investigate:# 
	Rev_Neutral+=['REV_771']
class REV_771:# <12>[1691]
	""" Investigate
	Search for clues. """
	#
	pass





if Rev_Muck_Plumber:# 
	Rev_Neutral+=['REV_837']
	Rev_Neutral+=['REV_837e']
class REV_837:# <12>[1691]
	""" Muck Plumber
	ALL minions cost (2) more. """
	#
	pass

class REV_837e:# <12>[1691]
	""" Yuck!
	Costs (2) more. """
	#
	pass





if Rev_Sinstone_Totem:# 
	Rev_Neutral+=['REV_839']
	Rev_Neutral+=['REV_839e']
class REV_839:# <12>[1691]
	""" Sinstone Totem
	At the end of your turn, gain +1 Health. """
	#
	pass

class REV_839e:# <12>[1691]
	""" Sinful Stones
	Increased Health. """
	#
	pass





if Rev_Anonymous_Informant:# 
	Rev_Neutral+=['REV_841']
	Rev_Neutral+=['REV_841e']
class REV_841:# <12>[1691]
	""" Anonymous Informant
	<b>Battlecry:</b> The next <b>Secret</b> you play costs (0). """
	#
	pass

class REV_841e:# <12>[1691]
	""" Informed
	Your next Secret costs (0). """
	#
	pass





if Rev_Sinfueled_Golem:# 
	Rev_Neutral+=['REV_843']
	Rev_Neutral+=['REV_843e']
	Rev_Neutral+=['REV_843t']
class REV_843_Action(TargetedAction):
	TARGET=ActionArg()
	ENTITY=ActionArg()
	def do(self, source, target, entity):
		controller=target
		source._sidequest_list1_.append(entity.atk)
		newcard=Infuse(CONTROLLER, 'REV_017t')
		if newcard!=None:
			amount=sum(source._sidequest_list1_)
			Buff(amount, 'REV_843e', atk=amount, max_health=amount).trigger(source)
		pass
class REV_843:# <12>[1691]
	""" Sinfueled Golem
	<b>Infuse (@):</b> Gain stats equal to the Attack of the minions that <b>Infused</b> this. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(REV_843_Action(CONTROLLER, Death.ENTITY))
	pass
class REV_843e:# <12>[1691]
	""" Animated
	Increased stats. """
	#
	pass
class REV_843t:# <12>[1691]
	""" Sinfueled Golem
	<b>Infused</b> """
	pass





if Rev_Volatile_Skeleton:# 
	Rev_Neutral+=['REV_845']
class REV_845:# <12>[1691]
	""" Volatile Skeleton
	<b>Deathrattle:</b> Deal 2 damage to a random enemy. """
	#
	pass





if Rev_Scuttlebutt_Ghoul:# 
	Rev_Neutral+=['REV_900']
class REV_900:# <12>[1691]
	""" Scuttlebutt Ghoul
	<b>Taunt</b> <b>Battlecry:</b> If you control a <b>Secret</b>, summon a copy of this. """
	#
	pass





if Rev_Dispossessed_Soul:# 
	Rev_Neutral+=['REV_901']
class REV_901:# <12>[1691]
	""" Dispossessed Soul
	<b>Battlecry:</b> If you control a location, <b>Discover</b> a copy of a card in your deck. """
	#
	pass





if Rev_Sire_Denathrius:# 
	Rev_Neutral+=['REV_906']
	Rev_Neutral+=['REV_906t']
class REV_906:# <12>[1691]
	""" Sire Denathrius
	<b><b>Lifesteal</b>.</b> <b>Battlecry:</b> Deal 5 damage amongst enemies. <b>Endlessly Infuse (1):</b> Deal 1 more. """
	#
	pass

class REV_906t:# <12>[1691]
	""" Sire Denathrius
	<b>Lifesteal</b>. <b>Battlecry:</b> Deal {1} damage amongst enemies. <b>Endlessly Infuse ({0}):</b> Deal 1 more. """
	#
	pass





if Rev_Creepy_Painting:# 
	Rev_Neutral+=['REV_916']
class REV_916:# <12>[1691]
	""" Creepy Painting
	After another minion dies, become a copy of it. """
	#
	pass





if Rev_Sketchy_Stranger:# 
	Rev_Neutral+=['REV_945']
class REV_945:# <12>[1691]
	""" Sketchy Stranger
	<b>Battlecry:</b> <b>Discover</b> a <b>Secret</b> from another class. """
	#
	pass





if Rev_Steamcleaner:# 
	Rev_Neutral+=['REV_946']
class REV_946:# <12>[1691]
	""" Steamcleaner
	<b>Battlecry:</b> Destroy ALL cards in both players' decks that didn't start there. """
	#
	pass





if Rev_Priest_of_the_Deceased:# 
	Rev_Neutral+=['REV_956']
	Rev_Neutral+=['REV_956t']
class REV_956:# <12>[1691]
	""" Priest of the Deceased
	<b>Taunt</b> <b>Infuse (@):</b> Gain +2/+2. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_013t'))
	pass
class REV_956t:# <12>[1691]
	""" Priest of the Deceased
	<b>Infused</b> <b>Taunt</b> """
	#
	pass





if Rev_Murlocula:# 
	Rev_Neutral+=['REV_957']
	Rev_Neutral+=['REV_957t']
class REV_957:# <12>[1691]
	""" Murlocula
	<b>Lifesteal</b> <b>Infuse (@):</b> This costs (0). """
	#
	pass

class REV_957t:# <12>[1691]
	""" Murlocula
	<b>Infused Lifesteal</b> """
	#
	pass

if Rev_Ashen_Elemental:# 
	Rev_Neutral+=['REV_960']
	Rev_Neutral+=['REV_960e']
class REV_960:# <12>[1691]
	""" Ashen Elemental
	<b>Battlecry:</b> Whenever your opponent draws a card next turn, they take 2 damage. """
	#
	pass

class REV_960e:# <12>[1691]
	""" Ashy
	Whenever your opponent draws a card next turn, they take 2 damage. """
	#
	pass

