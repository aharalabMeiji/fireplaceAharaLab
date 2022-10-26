from ..utils import *




from ..utils import *

Barrens_Neutral=[]
Barrens_Razormane_Raider=True## 24.0
Barrens_Gold_Road_Grunt=True## 24.0
Barrens_Peon=True## 24.0
Barrens_Oasis_Thrasher=True## 24.0
Barrens_Sunwell_Initiate=True## 24.0
Barrens_Deaths_Head_Cultist=True## 24.0
Barrens_Darkspear_Berserker=True## 24.0
Barrens_Primordial_Protector=True## 24.0
Barrens_Hog_Rancher=True## 24.0
Barrens_Ratchet_Privateer=True## 24.0
Barrens_Lushwater_Murcenary=True## 24.0
Barrens_Lushwater_Scout=True## 24.0
Barrens_Talented_Arcanist=True## 24.0
Barrens_Venomous_Scorpid=True## 24.0
Barrens_Injured_Marauder=True## 24.0
Barrens_Gruntled_Patron=True## 24.0
Barrens_Taurajo_Brave=True## 24.0
Barrens_Burning_Blade_Acolyte=True## 24.0
Barrens_Barrens_Blacksmith=True## 24.0
Barrens_Far_Watch_Post=True## 24.0
Barrens_Crossroads_Watch_Post=True## 24.0
Barrens_Morshan_Watch_Post=True## 24.0
Barrens_Kargal_Battlescar=True## 24.0
Barrens_Blademaster_Samuro=True## 24.0
Barrens_Kazakus_Golem_Shaper=False## 24.0
Barrens_Shadow_Hunter_Voljin=True## 24.0
Barrens_Southsea_Scoundrel=True## 24.0
Barrens_Barrens_Trapper=True## 24.0
Barrens_Horde_Operative=True## 24.0
Barrens_Mankrik=True## 24.0
Barrens_Toad_of_the_Wilds=True## 24.0
Barrens_Spirit_Healer=True## 24.0
Barrens_Hecklefang_Hyena=True## 24.0
Barrens_Drag_To_Move=True## 24.0
Barrens_Kindling_Elemental=True## 24.0
Barrens_Crossroads_Gossiper=True## 24.0
Barrens_Devouring_Ectoplasm=True## 24.0
Barrens_Meeting_Stone=False## 24.0 Adventurer with a random bonus の準備ができていない。
Barrens_Selfless_Sidekick=True## 24.0
Barrens_Mutanus_the_Devourer=True## 24.0
Barrens_Archdruid_Naralex=True## 24.0


###################################


###################################
if Barrens_Razormane_Raider:# 
	Barrens_Neutral+=['BAR_020']
class BAR_020:# <12>[1525] ##OK
	""" Razormane Raider
	[Frenzy:] Attack a random enemy. """
	events = Damage(SELF).on(Frenzy(SELF,Attack(SELF,RANDOM_ENEMY_CHARACTER)))
	pass


if Barrens_Gold_Road_Grunt:# 
	Barrens_Neutral+=['BAR_021']
class BAR_021:# <12>[1525] ##OK
	""" Gold Road Grunt
	[Taunt][Frenzy:] Gain Armor equalto the damage taken. """
	events = Damage(SELF).on(Frenzy(SELF,GainArmor(FRIENDLY_HERO,Damage.AMOUNT)))
	pass


if Barrens_Peon:# 
	Barrens_Neutral+=['BAR_022']
class BAR_022:# <12>[1525] ##OK
	""" Peon
	[Frenzy:] Add a randomspell from your classto your hand. """
	events = Damage(SELF).on(Frenzy(SELF,Give(CONTROLLER,RandomSpell(card_class=FRIENDLY_CLASS))))
	pass

if Barrens_Oasis_Thrasher:# 
	Barrens_Neutral+=['BAR_024']
class BAR_024:# <12>[1525]##OK
	""" Oasis Thrasher
	[Frenzy:] Deal 3 damage to the enemy hero. """
	events = Damage(SELF).on(Frenzy(SELF,Hit(ENEMY_HERO,3)))
	pass

if Barrens_Sunwell_Initiate:# 
	Barrens_Neutral+=['BAR_025']
class BAR_025:# <12>[1525] ##OK
	""" Sunwell Initiate
	[Frenzy:] Gain [Divine Shield]. """
	events = SELF_DAMAGE.on(Frenzy(SELF,SetTag(SELF, (GameTag.DIVINE_SHIELD,))))
	pass

if Barrens_Deaths_Head_Cultist:# 
	Barrens_Neutral+=['BAR_026']
class BAR_026:# <12>[1525] ##OK
	""" Death's Head Cultist
	[Taunt][Deathrattle:] Restore 4 Health to your hero. """
	deathrattle = Heal(FRIENDLY_HERO,4)
	pass

if Barrens_Darkspear_Berserker:# 
	Barrens_Neutral+=['BAR_027']
class BAR_027:# <12>[1525] ##OK
	""" Darkspear Berserker
	[Deathrattle:] Deal 5 damage to your hero. """
	deathrattle = Hit(FRIENDLY_HERO,5)
	pass




if Barrens_Primordial_Protector:# 
	Barrens_Neutral+=['BAR_042']
class BAR_042_Action(TargetedAction):
	def do(self, source, target):
		_highestCostCards=[]
		for _card in target.deck:
			if _card.type==CardType.SPELL:
				if len(_highestCostCards)==0:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost < _card.cost:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost == _card.cost:
					_highestCostCards.append(_card)
		if len(_highestCostCards)>0:
			_card = random.choice(_highestCostCards)##
			_cost = _card.cost
			if Config.LOGINFO:
				print("Highest cost spell is %r (cost %d)"%(_card, _cost))
				print("Summon a minion of cost %d"%( _cost))
			Give(target,_card).trigger(source)
			_highestMinions = []
			for _card2 in target.deck:
				if _card2.type==CardType.MINION and _card2.cost == _cost:
					_highestMinions.append(_card2)
			if(len(_highestMinions)>0):
				_card2 = random.choice(_highestMinions)##
				Summon(target,_card2).trigger(source)
			else:
				if Config.LOGINFO:
					print("no minion of cost %d"%( _cost))
		else:
			if Config.LOGINFO:
				print("no spell is in the deck"%())
class BAR_042:# <12>[1525] ##OK
	""" Primordial Protector
	[Battlecry:] Draw yourhighest Cost spell.Summon a random minionwith the same Cost. """
	play = BAR_042_Action(CONTROLLER) 
	pass




if Barrens_Hog_Rancher:# 
	Barrens_Neutral+=['BAR_060','BAR_060t']
class BAR_060:# <12>[1525] ##OK
	""" Hog Rancher
	[Battlecry:] Summon a2/1 Hog with [Rush]. """
	play = Summon(CONTROLLER, "BAR_060t")
	pass
class BAR_060t:# <12>[1525]
	""" Hog
	[Rush] """
	pass

if Barrens_Ratchet_Privateer:# 
	Barrens_Neutral+=['BAR_061','BAR_061e']
class BAR_061:# <12>[1525] ##OK
	""" Ratchet Privateer
	[Battlecry:] Give your weapon +1 Attack. """
	play = Find(FRIENDLY_WEAPON) & Buff(FRIENDLY_WEAPON, "BAR_061e")
	pass
BAR_061e=buff(atk=1)

if Barrens_Lushwater_Murcenary:# 
	Barrens_Neutral+=['BAR_062','BAR_062e']
class BAR_062:# <12>[1525] ##OK
	""" Lushwater Murcenary
	[Battlecry:] If you control a Murloc, gain +1/+1. """
	play = Find(FRIENDLY_MINIONS + MURLOC - SELF) & Buff(SELF, "BAR_062e")
	pass
BAR_062e = buff(atk=1,health=1)

if Barrens_Lushwater_Scout:# 
	Barrens_Neutral+=['BAR_063','BAR_063e']
class BAR_063:# <12>[1525] ##OK
	""" Lushwater Scout
	After you summon a Murloc, give it +1 Attack and [Rush]. """
	events = Summon(CONTROLLER,MURLOC).on(Buff(Summon.CARD,"BAR_063e"))
	pass
BAR_063e=buff(atk=1, rush=True)

if Barrens_Talented_Arcanist:# 
	Barrens_Neutral+=['BAR_064']
	#Barrens_Neutral+=['BAR_064e','BAR_064e2']
class BAR_064:# <12>[1525]###OK
	""" Talented Arcanist
	[Battlecry:] Your next spell_this turn has [Spell_Damage +2]. """
	play = SetAttr(SELF,'spellpower',2)
	events = [ OWN_SPELL_PLAY.after( SetAttr(SELF,'spellpower',0)),
		   OWN_TURN_END.on( SetAttr(SELF,'spellpower',0))
		   ]
	pass
#class BAR_064e:#<4> [1525]
#	update = Refresh(FRIENDLY_HAND, {GameTag.SPELLPOWER: 2})
#class BAR_064e2: #<4> [1525]

if Barrens_Venomous_Scorpid:# 
	Barrens_Neutral+=['BAR_065']
class BAR_065:# <12>[1525] ##OK
	""" Venomous Scorpid
	[Poisonous][Battlecry:] [Discover] a spell. """
	play = Discover(CONTROLLER, RandomSpell())
	pass

if Barrens_Injured_Marauder:# 
	Barrens_Neutral+=['BAR_069']
class BAR_069:# <12>[1525]
	""" Injured Marauder
	[Taunt][Battlecry:] Deal 6 damage to this minion. """
	play = Hit(SELF,6)
	pass

if Barrens_Gruntled_Patron:# ### OK 
	Barrens_Neutral+=['BAR_070']
class BAR_070:# <12>[1525] ##OK
	""" Gruntled Patron
	[Frenzy:] Summon another Gruntled Patron. """
	events = SELF_DAMAGE.on(Frenzy(SELF,Summon(CONTROLLER,Copy(SELF))))
	pass

if Barrens_Taurajo_Brave:# 
	Barrens_Neutral+=['BAR_071']
class BAR_071:#OK
	"""
	Taurajo Brave
	[Frenzy:] Destroy a random enemy minion.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Destroy(RANDOM(ENEMY_MINIONS))))
	pass


if Barrens_Burning_Blade_Acolyte:# 
	Barrens_Neutral+=['BAR_072','BAR_072t']
class BAR_072:#OK
	"""
	Burning Blade Acolyte
	[Deathrattle:] Summon a 5/8 Demonspawn with [Taunt].	"""
	deathrattle = Summon(CONTROLLER, "BAR_072t")
	pass
class BAR_072t:
	""" Demonspawn
	"""
	pass

if Barrens_Barrens_Blacksmith:# 
	Barrens_Neutral+=['BAR_073','BAR_073e']
class BAR_073:#OK
	"""
	Barrens Blacksmith
	[Frenzy:] Give your other minions +2/+2.	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Buff(FRIENDLY_MINIONS - SELF,"BAR_073e")))
	pass
BAR_073e=buff(atk=2,health=2)


if Barrens_Far_Watch_Post:# 
	Barrens_Neutral+=['BAR_074','BAR_074e']
class BAR_074:# <12>[1525] ##OK
	""" Far Watch Post
	Can't attack. After youropponent draws a card, it___costs (1) more <i>(up to 10)</i>.__ """
	update = Refresh(SELF, {GameTag.CANT_ATTACK: True})
	events = Draw(OPPONENT).on(Buff(Draw.CARD,"BAR_074e"))
	pass
class BAR_074e:# <12>[1525]
	tags = {GameTag.COST:+1}
	pass

if Barrens_Crossroads_Watch_Post:# 
	Barrens_Neutral+=['BAR_075','BAR_075e']
class BAR_075:#OK (2回やれば2つつく。)
	"""
	Crossroads Watch Post
	[x]Can't attack. Whenever your opponent casts a spell, give your minions +1/+1."""
	#<Tag enumID="227" name="CANT_ATTACK" type="Int" value="1"/>
	events = Play(OPPONENT,SPELL).on(Buff(FRIENDLY_MINIONS,"BAR_075e")) 
	pass
BAR_075e=buff(atk=1,health=1)

if Barrens_Morshan_Watch_Post:# 
	Barrens_Neutral+=['BAR_076','BAR_076t']
class BAR_076:#OK
	"""	Mor'shan Watch Post
	[x]Can't attack. After your opponent plays a minion, _summon a 2/2 Grunt."""
	#<Tag enumID="227" name="CANT_ATTACK" type="Int" value="1"/>
	events = Play(OPPONENT,MINION).on(Summon(CONTROLLER,"BAR_076t"))
	pass
class BAR_076t:
	"""Watchful Grunt
	vanilla	"""
	pass

if Barrens_Kargal_Battlescar:# 
	Barrens_Neutral+=['BAR_077','BAR_077t']
class BAR_077:#OK
	"""	Kargal Battlescar
	[x][Battlecry:] Summon a 5/5 Lookout for each Watch Post you've __summoned this game.	"""
	play = Summon(CONTROLLER,"BAR_077t") * CountSummon(SELF,["BAR_074","BAR_075","BAR_076"])
	pass
class BAR_077t:
	""" Lookout """

if Barrens_Blademaster_Samuro:# 
	Barrens_Neutral+=['BAR_078']
class BAR_078:#OK
	"""	Blademaster Samuro
	[x][Rush] [Frenzy:] Deal damage equal to this minion's Attack _to all enemy minions.	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Hit(ENEMY_MINIONS,Attr(SELF, GameTag.ATK))))
	pass

if Barrens_Kazakus_Golem_Shaper:# 
	Barrens_Neutral+=['BAR_079','BAR_079_m1','BAR_079_m2','BAR_079_m3']
	Barrens_Neutral+=['BAR_079t4','BAR_079t5','BAR_079t6','BAR_079t7','BAR_079t8','BAR_079t9']
	Barrens_Neutral+=["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
	Barrens_Neutral+=["BAR_079t10b","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
	Barrens_Neutral+=["bar_079t10c","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
	Barrens_Neutral+=['BAR_079t10e','BAR_079t10be','BAR_079t10ce']
class BAR_079_firstChoice(GenericChoice):
	secondChoice = ["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]# first choice
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		choiceCard = controller.hand[-1]
		choiceCardId = choiceCard.id
		choiceCard.zone = Zone.GRAVEYARD
		BAR_079_secondChoice(controller,RandomEntourage()*3).trigger(self)

class BAR_079:###OK
	"""
	Kazakus, Golem Shaper
	[Battlecry:] If your deck has no 4-Cost cards, build a custom Golem.
	First, choose one of 'cost 1, cost 5, cost 10'
	Next, choose one of 'rush, taunt, divine shield, life steal,  stealth, poisonous'

	"""
	entourage = ["BAR_079_m1","BAR_079_m2","BAR_079_m3"]# first choice
	powered_up = -Find(FRIENDLY_DECK + (COST==4))
	def play(self):
		controller = self.controller
		if self.powered_up:
			#GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
			GenericChoiceBattlecry(controller,RandomID("BAR_079_m1","BAR_079_m2","BAR_079_m3")*3).trigger(self)
	pass


class BAR_079_m1:
	""" Lesser Golem
	{0}{1} """
	#
	entourage = ["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]# second choice
	def play(self):
		controller = self.controller
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
		pass
	pass

class BAR_079_m2:
	""" Greater Golem
	{0}{1} """
	entourage = ["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]# second choice
	def play(self):
		controller = self.controller
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
		pass
	pass

class BAR_079_m3:
	""" Superior Golem
	{0}{1} """
	entourage = ["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]# second choice
	def play(self):
		controller = self.controller
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
		pass
	pass

class BAR_079t4:
	""" Swifthistle
	[Rush] """
	def play(self):
		controller = self.controller
		choice1 = controller.hand[-2].id
		if choice1 == 'BAR_079_m1':
			self.entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
		elif choice1 == 'BAR_079_m2':
			self.entourage = ["BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
		elif choice1 == 'BAR_079_m3':
			self.entourage = ["bar_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
	pass

class BAR_079t5:
	""" Earthroot
	[Taunt] """
	def play(self):
		controller = self.controller
		choice1 = controller.hand[-2].id
		if choice1 == 'BAR_079_m1':
			self.entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
		elif choice1 == 'BAR_079_m2':
			self.entourage = ["BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
		elif choice1 == 'BAR_079_m3':
			self.entourage = ["bar_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
	pass

class BAR_079t6:
	""" Sungrass
	[Divine Shield] """
	def play(self):
		controller = self.controller
		choice1 = controller.hand[-2].id
		if choice1 == 'BAR_079_m1':
			self.entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
		elif choice1 == 'BAR_079_m2':
			self.entourage = ["BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
		elif choice1 == 'BAR_079_m3':
			self.entourage = ["bar_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
	pass

class BAR_079t7:
	""" Liferoot
	[Lifesteal] """
	def play(self):
		controller = self.controller
		choice1 = controller.hand[-2].id
		if choice1 == 'BAR_079_m1':
			self.entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
		elif choice1 == 'BAR_079_m2':
			self.entourage = ["BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
		elif choice1 == 'BAR_079_m3':
			self.entourage = ["bar_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
	pass

class BAR_079t8:
	""" Fadeleaf
	[Stealth] """
	def play(self):
		controller = self.controller
		choice1 = controller.hand[-2].id
		if choice1 == 'BAR_079_m1':
			self.entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
		elif choice1 == 'BAR_079_m2':
			self.entourage = ["BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
		elif choice1 == 'BAR_079_m3':
			self.entourage = ["bar_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
	pass

class BAR_079t9:
	""" Grave Moss
	[Poisonous] """
	def play(self):
		controller = self.controller
		choice1 = controller.hand[-2].id
		if choice1 == 'BAR_079_m1':
			self.entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12"]
		elif choice1 == 'BAR_079_m2':
			self.entourage = ["BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b"]
		elif choice1 == 'BAR_079_m3':
			self.entourage = ["bar_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
		GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
	pass

def BAR_079Buff(card, buffId):
	if buffId=='BAR_079t4':
		card.rush=True
		card.script_data_text_0='[急襲]'
	elif buffId=='BAR_079t5':
		card.taunt=True
		card.script_data_text_0='[挑発]'
	elif buffId=='BAR_079t6':
		card.devine_shield=True
		card.script_data_text_0='[聖なる盾]'
	elif buffId=='BAR_079t7':
		card.lifesteal=True
		card.script_data_text_0='[生命奪取]'
	elif buffId=='BAR_079t8':
		card.stealth=True
		card.script_data_text_0='[隠れ身]'
	elif buffId=='BAR_079t9':
		card.poisonous=True
		card.script_data_text_0='[猛毒]'

def adjust_text(text):
	return text.replace('\n','').replace('[x]','').replace('[','[').replace(']',']')

class BAR_079t10:
	""" Wildvine
	[Battlecry:] Give your other minions +1/+1. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Buff(FRIENDLY_MINIONS-SELF,"BAR_079t10e"),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass
BAR_079t10e=buff(1,1)

class BAR_079t10b:###OK
	""" Wildvine
	[Battlecry:] Give your other minions +2/+2. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Buff(FRIENDLY_MINIONS-SELF,"BAR_079t10be"),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass
BAR_079t10be=buff(2,2)

class bar_079t10c:
	""" Wildvine
	[Battlecry:] Give your other minions +4/+4. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Buff(FRIENDLY_MINIONS-SELF,"BAR_079t10ce"),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass
BAR_079t10ce=buff(4,4)

class BAR_079t11:###OK
	""" Gromsblood
	[Battlecry:] Summon a copy of this. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Summon(CONTROLLER, ExactCopy(SELF)),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	#play = Summon(CONTROLLER, Copy(SELF))   
	pass

class BAR_079t12:
	""" Icecap
	[Battlecry:] [Freeze] a random enemy minion. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Freeze(RANDOM(ENEMY_MINIONS)),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t12b:###OK
	""" Icecap
	[Battlecry:] [Freeze] two random enemy minions. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Freeze(RANDOM(ENEMY_MINIONS)),Freeze(RANDOM(ENEMY_MINIONS))))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t12c:
	""" Icecap
	[Battlecry:] [Freeze] all enemy minions. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Freeze(ENEMY_MINIONS),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t13:###OK
	""" Firebloom
	[Battlecry:] Deal 3 damage to a random enemy minion. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Hit(RANDOM(ENEMY_MINIONS),3),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t13b:
	""" Firebloom
	[Battlecry:] Deal 3 damage to two random enemy minions. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Hit(RANDOM(ENEMY_MINIONS),3),Hit(RANDOM(ENEMY_MINIONS),3)))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t13c:
	""" Firebloom
	[Battlecry:] Deal 3 damage to all enemy minions. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Hit(ENEMY_MINIONS,3),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t14:
	""" Mageroyal
	[Spell Damage +1]. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		card.spellpower=1
		setattr(card.data.scripts, 'play', [])
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t14b:
	""" Mageroyal
	[Spell Damage +2]. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		card.spellpower=2
		setattr(card.data.scripts, 'play', [])
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t14c:
	""" Mageroyal
	[Spell Damage +4]. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		card.spellpower=4
		setattr(card.data.scripts, 'play', [])
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t15:
	""" Kingsblood
	[Battlecry:] Draw a card. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Draw(CONTROLLER),))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t15b:###OK
	""" Kingsblood
	[Battlecry:] Draw 2 cards. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Draw(CONTROLLER)*2,))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass

class BAR_079t15c:
	""" Kingsblood
	[Battlecry:] Draw 4 cards. """
	def play(self):
		controller = self.controller
		card = controller.hand[-3]
		cardId=card.id
		BAR_079Buff(card, controller.hand[-2].id)
		card.script_data_text_0+=adjust_text(self.data.description)
		setattr(card.data.scripts, 'play', (Draw(CONTROLLER)*4,))
		controller.hand[-1].zone=Zone.GRAVEYARD
		controller.hand[-1].zone=Zone.GRAVEYARD
	pass



if Barrens_Shadow_Hunter_Voljin:# 
	Barrens_Neutral+=['BAR_080']
class BAR_080:#OK
	"""	Shadow Hunter Vol'jin
	[Battlecry:] Choose a minion. Swap it with a random one in its owner's hand.	"""
	requirements = { PlayReq.REQ_MINION_TARGET: 0,	PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = SwapMinionAndHand(TARGET, RANDOM(FRIENDLY_HAND))
	pass



if Barrens_Southsea_Scoundrel:# 
	Barrens_Neutral+=['BAR_081']
class BAR_081_Southsea_Scoundrel(Choice):## 
	#Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		if Config.LOGINFO:
			Config.log("BAR_081_Southsea_Scoundrel.choose","%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					Give(card.controller,card.id).trigger(card.controller)
				else:
					_card.discard()
			else:
				_card.discard()
		controller = card.controller.opponent##もともと相手のもの->これは自分
		Give(controller,card.id).trigger(controller)
		pass
class BAR_081:#OK
	"""	Southsea Scoundrel
	[Battlecry:] [Discover] a card in your opponent's deck. They draw theirs as well.	"""
	play = BAR_081_Southsea_Scoundrel(CONTROLLER,RANDOM(ENEMY_DECK)*3)
	pass


if Barrens_Barrens_Trapper:# 
	Barrens_Neutral+=['BAR_082','BAR_082e']
class BAR_082:#OK
	"""
	Barrens Trapper
	Your [Deathrattle] cards cost (1) less.
	"""
	play = Buff(FRIENDLY_HAND+DEATHRATTLE,"BAR_082e")
	pass
BAR_082e=buff(cost=-1)




if Barrens_Horde_Operative:# 
	Barrens_Neutral+=['BAR_430']
class BAR_430:#OK
	"""
	Horde Operative
	[Battlecry:] Copy your opponent's [Secrets] and put them into play.
	"""
	play = Summon(CONTROLLER,Copy(ENEMY_SECRETS))
	pass




if Barrens_Mankrik:# 
	Barrens_Neutral+=['BAR_721','BAR_721t','BAR_721t2']
class BAR_721:#OK
	"""
	Mankrik
	[x][Battlecry:] Help Mankrik find his wife! She was last seen somewhere in your deck.
	"""
	play = Shuffle(CONTROLLER,"BAR_721t")
	pass
class BAR_721t:#OK OK 22_10_27
	"""Olgra, Mankrik's Wife
	[x][Casts When Drawn]	Summon a 3/7 Mankrik,		who immediately attacks		the enemy hero.
		<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	"""
	play = Summon(CONTROLLER,'BAR_721t2'), RegularAttack(FRIENDLY_MINIONS+ID('BAR_721t2'),ENEMY_HERO)
	pass
class BAR_721t2:
	"""Mankrik, Consumed by Hatred
	vanilla 	"""
	pass



if Barrens_Toad_of_the_Wilds:# 
	Barrens_Neutral+=['BAR_743','BAR_743e']
class BAR_743:#OK 
	#******NATUREはドルイド、シャーマンの特性****たとえば自然学の予習(SCH_333)**
	"""
	[x][Taunt] [Battlecry:] If you're holding a Nature spell, gain +2 Health.
	"""
	play = Find(FRIENDLY_HAND+SPELL+NATURE) & Buff(SELF,'BAR_743e')
	pass
BAR_743e=buff(health=2)



if Barrens_Spirit_Healer:# 
	Barrens_Neutral+=['BAR_744','BAR_744e']
class BAR_744:#OK
	"""
	Spirit Healer
	After you cast a Holy spell, give a random friendly minion +2 Health.
	-
	"""
	events = Play(CONTROLLER, SPELL+HOLY).on(Buff(RANDOM_FRIENDLY_MINION,"BAR_744e"))
	pass
BAR_744e=buff(health=2)



if Barrens_Hecklefang_Hyena:# 
	Barrens_Neutral+=['BAR_745']
class BAR_745:# <12>[1525] ## OK
	""" Hecklefang Hyena
	[Battlecry:] Deal 3 damage to your hero. """
	play = Hit(FRIENDLY_HERO,3)
	pass





if Barrens_Kindling_Elemental:# 
	Barrens_Neutral+=['BAR_854','BAR_854e']
class BAR_854:# <12>[1525] ##OK
	""" Kindling Elemental
	[Battlecry:] The next Elemental you playcosts (1) less. """
	play = Buff(CONTROLLER, "BAR_854e")
	events = Play(CONTROLLER,ELEMENTAL).on( Destroy(FRIENDLY + ID("BAR_854e")))
	pass
class BAR_854e:
	update = Refresh(FRIENDLY_HAND +ELEMENTAL, {GameTag.COST: -1})
	#+ EnumSelector(Race.ELEMENTAL)
	pass 

if Barrens_Crossroads_Gossiper:# 
	Barrens_Neutral+=['BAR_890','BAR_890e']
class BAR_890:#OK
	"""	Crossroads Gossiper
	After a friendly [Secret] is revealed, gain +2/+2.	"""
	events = Reveal(FRIENDLY_SECRETS).on(Buff(SELF, "BAR_890e"))
	pass
BAR_890e=buff(atk=2,health=2)





if Barrens_Devouring_Ectoplasm:# 
	Barrens_Neutral+=['WC_027']
class WC_027:#OK
	"""	Devouring Ectoplasm
	[x][Deathrattle:] Summon a 2/2 Adventurer with_a random bonus effect.	"""
	deathrattle = SummonAdventurerWithBonus(CONTROLLER)
	pass



if Barrens_Meeting_Stone:# 
	Barrens_Neutral+=['WC_028']
class GiveAdventurerWithBonus(TargetedAction):
	""" Meeting Stone """
	TARGET = ActionArg()#the controller
	def do(self,source,target):
		new_minion = random.choice(['WC_034t','WC_034t2','WC_034t3','WC_034t4','WC_034t5','WC_034t6','WC_034t7','WC_034t8',])##
		new_minion = Give(target, new_minion).trigger(source)
		if new_minion[0] != []:# the hand may be full
			new_minion = new_minion[0][0]
			newAtk=new_minion.atk+random.randint(1,3)
			new_minion._atk = new_minion.atk = newAtk
			new_minion.data.scripts.atk = lambda self, i: self._atk
			newHealth = new_minion.health+random.randint(1,3)
			new_minion.max_health = newHealth
			if Config.LOGINFO:
				print("Give %s with atk=%d, health=%d"%(new_minion.data.name, newAtk, newHealth))
class WC_028:# <12>[1525] ##OK
	""" Meeting Stone
	At the end of your turn,add a 2/2 Adventurerwith a random bonus effectto your hand. """
	events = OWN_TURN_END.on(GiveAdventurerWithBonus(CONTROLLER))
	pass

if Barrens_Selfless_Sidekick:# 
	Barrens_Neutral+=['WC_029']
class WC_029:#OK
	"""	Selfless Sidekick
	[Battlecry:] Equip a random weapon from your deck.	"""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+WEAPON))
	pass



if Barrens_Mutanus_the_Devourer:# 
	Barrens_Neutral+=['WC_030','WC_030e']
class WC_030:#OK
	"""	Mutanus the Devourer
	[x][Battlecry:] Eat a minion in your opponent's hand. Gain its stats.	"""
	play = EatsCard(SELF, RANDOM(ENEMY_HAND + MINION))
	pass
WC_030e=buff()



if Barrens_Archdruid_Naralex:# 
	Barrens_Neutral+=['WC_035','WC_035e','WC_035e2']
class WC_035_Archdruid_Naralex(TargetedAction):
	TARGET = ActionArg()#self
	def do(self, source, target):
		dreams=["DREAM_01","DREAM_02","DREAM_03","DREAM_04","DREAM_05"]
		newCard = random.choice(dreams)##
		Give(target,newCard).trigger(source)
		pass
class WC_035:#OK
	"""	Archdruid Naralex
	[x][Dormant] for 2 turns. While [Dormant], 	add a Dream card to your hand __at the end of your turn.	"""
	play = Buff(CONTROLLER,"WC_035e")
	dormant = 2
	awaken = Destroy(FRIENDLY + ID("WC_035e"))
	pass
class WC_035e:
	events = OWN_TURN_END.on(WC_035_Archdruid_Naralex(CONTROLLER))
	pass
class WC_035e2:
	pass


######


