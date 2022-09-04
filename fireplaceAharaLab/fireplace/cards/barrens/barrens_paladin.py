
from ..utils import *

Barrens_Paladin=[]

Barrens_Galloping_Savior=True  ###
Barrens_Soldiers_Caravan=True  ###
Barrens_Knight_of_Anointment=True  ###
Barrens_Sword_of_the_Fallen=True  ###
Barrens_Northwatch_Commander=True  ###
Barrens_Veteran_Warmedic=True  ###
Barrens_Cannonmaster_Smythe=True  ###OK
Barrens_Conviction_Rank_1=True  ###
Barrens_Invigorating_Sermon=True  ###
Barrens_Cariel_Roame=True  ###
Barrens_Seedcloud_Buckler=True  ###
Barrens_Judgment_of_Justice=True  ###
Barrens_Party_Up=True  ###

####################################################

if Barrens_Galloping_Savior:# 
	Barrens_Paladin+=['BAR_550']
	Barrens_Paladin+=['BAR_550t']
class BAR_550_Action(GameAction):
	previous_turn=0
	card_count=0
	def do(self, source):
		if Config.LOGINFO:
			Config.log("BAR_550_Action","After your opponent plays three cards in a turn")
		if self.previous_turn!=source.controller.game.turn:
			self.card_count=1
			self.previous_turn=source.controller.game.turn
		else:
			self.card_count += 1
			if self.card_count>=3:
				Summon(source.controller, 'BAR_550t').trigger(source)
		source.sidequest_list0
class BAR_550:# <5>[1525]
	""" Galloping Savior
	[Secret:] After your opponent plays three cards in a turn, summon a 3/4 Steed with [Taunt]. """
	secret = Play(OPPONENT).on(BAR_550_Action())
	pass
class BAR_550t:# <5>[1525]
	""" Holy Steed
	[Taunt] """
	#
	pass




if Barrens_Soldiers_Caravan:# 
	Barrens_Paladin+=['BAR_871']
class BAR_871:# <5>[1525]
	""" Soldier's Caravan
	At the start of your turn,summon two 1/1Silver Hand Recruits. """
	events = OWN_TURN_BEGIN.on(Summon(CONTROLLER, 'CS2_101t')*2)
	pass




if Barrens_Knight_of_Anointment:# 
	Barrens_Paladin+=['BAR_873']
class BAR_873:# <5>[1525]
	""" Knight of Anointment
	[Battlecry:] Draw aHoly spell. """
	def play(self):
		controller = self.controller
		cards=[card for card in controller.deck if card.type==CardType.SPELL and hasattr(card,'spell_school') and card.spell_school==SpellSchool.HOLY]
		if len(cards)>0:
			Give(controller, random.choice(cards)).trigger(self)
	pass




if Barrens_Sword_of_the_Fallen:# 
	Barrens_Paladin+=['BAR_875']
class BAR_875_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		controller = target
		cards = [card for card in controller.deck if card.type==CardType.SPELL and hasattr(card,'secret') and card.secret==True]
		if len(cards)>0:
			Summon(controller, random.choice(cards)).trigger(source)
class BAR_875:# <5>[1525]
	""" Sword of the Fallen
	After your hero attacks,cast a [Secret] from your deck. """
	events = Attack(FRIENDLY_HERO).after(BAR_875_Action(CONTROLLER))
	pass




if Barrens_Northwatch_Commander:# 
	Barrens_Paladin+=['BAR_876']
class BAR_876:# <5>[1525]
	""" Northwatch Commander
	[Battlecry:] If you control a [Secret], draw a minion. """
	play = Find(FRIENDLY_SECRETS) & Give(CONTROLLER, RANDOM(FRIENDLY_DECK + MINION))
	pass




if Barrens_Veteran_Warmedic:# 
	Barrens_Paladin+=['BAR_878']
	Barrens_Paladin+=['BAR_878t']
class BAR_878:# <5>[1525]
	""" Veteran Warmedic
	After you cast a Holy spell,summon a 2/2 Medic with [Lifesteal]. """
	events = Play(CONTROLLER, SPELL+HOLY).after(Summon(CONTROLLER, 'BAR_878t'))
	pass
class BAR_878t:# <5>[1525]
	""" Battlefield Medic
	[Lifesteal] """
	#
	pass




if Barrens_Cannonmaster_Smythe:#  ######## OK
	Barrens_Paladin+=['BAR_879']
	Barrens_Paladin+=['BAR_879e']
	Barrens_Paladin+=['BAR_879t']
class BAR_879:# <5>[1525]
	""" Cannonmaster Smythe
	[Battlecry:] Transform your [Secrets] into 3/3 Soldiers. They transform back when they die. """
	def play(self):
		for secret in self.controller.secrets:
			newcard=Summon(self.controller, 'BAR_879t').trigger(self)
			newcard=newcard[0][0]
			Buff(newcard, 'BAR_879e').trigger(self)
			newbuff=newcard.buffs[-1]
			newbuff.smallbox.append(secret.id)
			newbuff.script_data_text_0=secret.data.name
			Destroy(secret).trigger(self)
	pass
class BAR_879e_Deathrattle(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		for buff in source.buffs:
			if buff.id=='BAR_879e':
				secretId=buff.smallbox[0]
				#newcard=target.card()
				Summon(target,secretId).trigger(source)
class BAR_879e:# <5>[1525]
	""" Secrecy
	It's a secret...@{0} is inside! <i>(Only you can see this.)</i> """
	pass
class BAR_879t:# <5>[1525]
	""" Northwatch Soldier
	[Deathrattle:] Transform back into a [Secret]. """
	deathrattle = BAR_879e_Deathrattle(CONTROLLER)#
	pass




if Barrens_Conviction_Rank_1:# 
	Barrens_Paladin+=['BAR_880']
	Barrens_Paladin+=['BAR_880e']
	Barrens_Paladin+=['BAR_880t']
	Barrens_Paladin+=['BAR_880t2']
class BAR_880:# <5>[1525]
	""" Conviction (Rank 1)
	Give a random friendly minion +3 Attack.<i>(Upgrades when you have 5 Mana.)</i> """
	play = Buff(RANDOM(FRIENDLY_MINIONS), "BAR_880e")
	class Hand:
		events = GradeupByMana(CONTROLLER, 5).on(Destroy(SELF),Give(CONTROLLER, 'BAR_880t'))
	pass
class BAR_880e:# <5>[1525]
	""" Blessed 	+3 Attack. """
	tags = {GameTag.ATK:3, }
	pass
class BAR_880t:# <5>[1525]
	""" Conviction (Rank 2)
	Give two random friendlyminions +3 Attack.<i>(Upgrades when youhave 10 Mana.)</i> """
	play = Buff(RANDOM(FRIENDLY_MINIONS), "BAR_880e")*2
	class Hand:
		events = GradeupByMana(CONTROLLER, 10).on(Destroy(SELF),Give(CONTROLLER, 'BAR_880t2'))	
	pass
class BAR_880t2:# <5>[1525]
	""" Conviction (Rank 3)
	Give three random friendly minions +3_Attack. """
	play = Buff(RANDOM(FRIENDLY_MINIONS), "BAR_880e")*3
	pass




if Barrens_Invigorating_Sermon:# 
	Barrens_Paladin+=['BAR_881']
	Barrens_Paladin+=['BAR_881e']
class BAR_881:# <5>[1525]
	""" Invigorating Sermon
	Give +1/+1 to all minions in your hand, deck, and battlefield. """
	play = Buff(FRIENDLY_HAND, 'BAR_881e'), Buff(FRIENDLY_DECK, 'BAR_881e'), Buff(FRIENDLY_MINIONS, 'BAR_881e')
	pass
class BAR_881e:# <5>[1525]
	""" Holy Might 	+1/+1 """
	tags = {
		GameTag.ATK:1,
		GameTag.HEALTH:1
		}
	pass




if Barrens_Cariel_Roame:# 
	Barrens_Paladin+=['BAR_902']
	Barrens_Paladin+=['BAR_902e']
class BAR_902:# <5>[1525]
	""" Cariel Roame
	[Rush], [Divine Shield] Whenever this attacks,reduce the Cost of Holy______spells in your hand by (1).___ """
	Events = Attack(SELF).on(Buff(FRIENDLY_HAND + HOLY, 'BAR_902e'))
	pass
class BAR_902e:# <5>[1525]
	""" Light's Strength 	Costs (1) less. """
	tags = { GameTag.COST:-1, }
	pass




if Barrens_Seedcloud_Buckler:# ### OKOK ###
	Barrens_Paladin+=['WC_032']
class WC_032:# <5>[1525]
	""" Seedcloud Buckler   (weapon)
	[Deathrattle:] Give your_minions [Divine Shield]. """
	deathrattle = SetDivineShield(FRIENDLY_MINIONS, True)
	pass



if Barrens_Judgment_of_Justice:# 
	Barrens_Paladin+=['WC_033']
	Barrens_Paladin+=['WC_033e']
class WC_033:# <5>[1525]
	""" Judgment of Justice
	[Secret:] When an enemy minion attacks, set its Attack and Health to 1. """
	secret = Attack(ENEMY_MINIONS).on(Buff(Attack.ATTACKER, 'WC_033e'))
	pass
class WC_033e:# <5>[1525]
	""" Judged 	1/1. """
	atk = lambda self, i : 1
	max_health = lambda self, i : 1
	pass




if Barrens_Party_Up:# 
	Barrens_Paladin+=['WC_034','WC_034t','WC_034t2','WC_034t3','WC_034t4','WC_034t5','WC_034t6','WC_034t7','WC_034t8']
class WC_034:# <5>[1525]
	""" Party Up!
	Summon five 2/2 Adventurers with random bonus effects. """
	def play(self):
		cards = random.sample(['WC_034', 'WC_034t', 'WC_034t2', 'WC_034t3', 'WC_034t4', 'WC_034t5', 'WC_034t6', 'WC_034t7', 'WC_034t8'],5)
		for card in cards:
			newcard=Summon(self.controller, card).trigger(self)
			newcard=newcard[0][0]
			Buff(newcard, "WC_034e", atk=random.randint(1,3), max_health=random.randint(1,3))
	pass
class WC_034t:
	"""[Poisonous]"""
	pass
class WC_034t2:
	"""[Taunt]"""
	pass
class WC_034t3:
	"""[Divine Shield]"""
	pass
class WC_034t4:
	"""[Windfury]"""
	pass
class WC_034t5:
	""" [Spell Damage +1] """
	pass
class WC_034t6:
	""" [Stealth] """
	pass
class WC_034t7:
	""" [Lifesteal] """
	pass
class WC_034t8:
	""" [Rush] """
	pass
@custom_card
class WC_034e:# <5>[1525]
	""" Judged 	1/1. """
	tags={
		GameTag.CARDNAME:"Seedcloud Buckler",
		GameTag.CARDTYPE:CardType.ENCHANTMENT}
	pass

