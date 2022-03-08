from ..utils import *

#BAR_041e
#BAR_041e2
#BAR_045e
#BAR_308e
#BAR_315e1
#BAR_315e2
#BAR_315e3
#BAR_315e4
#BAR_318e
#BAR_320e
#BAR_322e
#BAR_333e
#BAR_552e
#BAR_705e
#WC_013e
#WC_023e
#WC_040e
#WC_007e
#BAR_064e
#BAR_064e2



class BAR_854:#Perfait
	"""Kindling Elemental
	[x]<b>Battlecry:</b> The next  Elemental you play costs (1) less.
	"""
	play = Buff(CONTROLLER, "BAR_854e")
	events = Play(CONTROLLER,ELEMENTAL).on( Destroy(FRIENDLY + ID("BAR_854e")))
	pass

class BAR_854e:
	update = Refresh(FRIENDLY_HAND +ELEMENTAL, {GameTag.COST: -1})
	#+ EnumSelector(Race.ELEMENTAL)
	pass 

class GiveAdventurerWithBonus(TargetedAction):
	""" Meeting Stone """
	TARGET = ActionArg()#the controller
	def do(self,source,target):
		new_minion = random.choice(['WC_034t','WC_034t2','WC_034t3','WC_034t4','WC_034t5','WC_034t6','WC_034t7','WC_034t8',])##
		new_minion =  Give(target, new_minion).trigger(source)
		if new_minion[0] != []:# the hand may be full
			new_minion = new_minion[0][0]
			newAtk=new_minion.atk+random.randint(1,3)
			new_minion._atk = new_minion.atk = newAtk
			new_minion.data.scripts.atk = lambda self, i: self._atk
			newHealth = new_minion.health+random.randint(1,3)
			new_minion.max_health = newHealth
			log.info("Give %s with atk=%d, health=%d"%(new_minion.data.name, newAtk, newHealth))

class WC_028:#OK
	"""
	Meeting Stone
	[x]At the end of your turn, add a 2/2 Adventurer with a random bonus effect to your hand.
	"""
	events = OWN_TURN_END.on(GiveAdventurerWithBonus(CONTROLLER))
	pass

class BAR_074:#OK　　
	"""
	Far Watch Post

	[x]Can't attack. After your opponent draws a card, it ___costs (1) more <i>(up to 10)</i>.__
	"""
	update = Refresh(SELF, {GameTag.CANT_ATTACK: True})
	events = Draw(OPPONENT).on(Buff(Draw.CARD,"BAR_074e"))
	pass

class BAR_074e:
	# Spotted!"""
	cost = lambda self, i: min(i+1,10)

class BAR_745:#OK
	"""
	Hecklefang Hyena
	<b>Battlecry:</b> Deal 3 damage to your hero.
	"""
	play = Hit(FRIENDLY_HERO,3)
	pass

class BAR_062:#OK
	"""
	Lushwater Murcenary
	<b>Battlecry:</b> If you control a Murloc, gain +1/+1.
	"""
	play = Find(FRIENDLY_MINIONS + MURLOC - SELF) & Buff(SELF, "BAR_062e")
	pass
BAR_062e = buff(atk=1,health=1)

class BAR_063:#OK
	"""
	Lushwater Scout
	After you summon a Murloc, give it +1 Attack and <b>Rush</b>.
	"""
	events = Summon(CONTROLLER,MURLOC).on(Buff(Summon.CARD,"BAR_063e"))
	pass
BAR_063e=buff(atk=1, rush=True)

class BAR_024:#OK
	"""
	Oasis Thrasher
	<b>Frenzy:</b> Deal 3 damage to the enemy Hero.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Hit(ENEMY_HERO,3)))
	pass

class BAR_022:#OK
	"""
	Peon
	[x]<b>Frenzy:</b> Add a random spell from your class to your hand.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Give(CONTROLLER,RandomSpell(card_class=FRIENDLY_CLASS))))
	pass

class BAR_064:###OK  ## OWN_SPELL_PLAY.after is calid. no '.on'
	"""
	Talented Arcanist
	<b>Battlecry:</b> Your next spell_this turn has <b>Spell_Damage +2</b>.
	"""
	play = SetAttr(SELF,'spellpower',2)
	events = [ OWN_SPELL_PLAY.after( SetAttr(SELF,'spellpower',0)),
		   OWN_TURN_END.on( SetAttr(SELF,'spellpower',0))
		   ]
	pass

#class BAR_064e:#<4> [1525]
#	update = Refresh(FRIENDLY_HAND, {GameTag.SPELLPOWER: 2})
#class BAR_064e2: #<4> [1525]

class BAR_743:#OK 
	#******NATUREはドルイド、シャーマンの特性****たとえば自然学の予習(SCH_333)**
	"""
	[x]<b>Taunt</b> <b>Battlecry:</b> If you're holding a Nature spell, gain +2 Health.
	"""
	play = Find(FRIENDLY_HAND+SPELL+NATURE) & Buff(SELF,'BAR_743e')
	pass
BAR_743e=buff(health=2)

class WC_035_Archdruid_Naralex(TargetedAction):
	TARGET = ActionArg()#self
	def do(self, source, target):
		dreams=["DREAM_01","DREAM_02","DREAM_03","DREAM_04","DREAM_05"]
		newCard = random.choice(dreams)##
		Give(target,newCard).trigger(source)
		pass


class WC_035:#OK
	"""
	Archdruid Naralex
	[x]<b>Dormant</b> for 2 turns. While <b>Dormant</b>, 
	add a Dream card to your hand __at the end of your turn.
	"""
	play = Buff(CONTROLLER,"WC_035e")
	dormant = 2
	awaken = Destroy(FRIENDLY + ID("WC_035e"))
	pass

class WC_035e:
	events = OWN_TURN_END.on(WC_035_Archdruid_Naralex(CONTROLLER))
	pass


class BAR_082:#OK
	"""
	Barrens Trapper
	Your <b>Deathrattle</b> cards cost (1) less.
	"""
	play = Buff(FRIENDLY_HAND+DEATHRATTLE,"BAR_082e")
	pass
BAR_082e=buff(cost=-1)

class BAR_890:#OK
	"""
	Crossroads Gossiper
	After a friendly <b>Secret</b> is revealed, gain +2/+2.
	"""
	events = Reveal(FRIENDLY_SECRETS).on(Buff(SELF, "BAR_890e"))
	pass
BAR_890e=buff(atk=2,health=2)

class BAR_026:#OK
	"""
	Death's Head Cultist
	<b>Taunt</b> <b>Deathrattle:</b> Restore 4 Health to your hero.
	"""
	deathrattle = Heal(FRIENDLY_HERO,4)
	pass


class WC_027:#OK
	"""
	Devouring Ectoplasm
	[x]<b>Deathrattle:</b> Summon a 2/2 Adventurer with_a random bonus effect.
	"""
	deathrattle = SummonAdventurerWithBonus(CONTROLLER)
	pass

class WC_034t: # <12>[1525] OK (WC_034 is a paladin card.)
	""" Deadly Adventurer
	Poisonous"""
	pass
class WC_034t2: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class WC_034t3: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class WC_034t4: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class WC_034t5: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class WC_034t6: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class WC_034t7: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class WC_034t8: # <12>[1525]  OK (WC_034 is a paladin card.)
	pass
class BAR_060:#OK
	"""
	Hog Rancher
	<b>Battlecry:</b> Summon a 2/1 Hog with <b>Rush</b>.
	"""
	play = Summon(CONTROLLER, "BAR_060t")
	pass
class BAR_060t:
	""" Hog """
	pass

class BAR_430:#OK
	"""
	Horde Operative
	<b>Battlecry:</b> Copy your opponent's <b>Secrets</b> and put them into play.
	"""
	play = Summon(CONTROLLER,Copy(ENEMY_SECRETS))
	pass

class BAR_721:#OK
	"""
	Mankrik
	[x]<b>Battlecry:</b> Help Mankrik find his wife! She was last seen somewhere in your deck.
	"""
	play = Shuffle(CONTROLLER,"BAR_721t"),
	pass
class BAR_721t:#OK
	"""Olgra, Mankrik's Wife
	[x]<b>Casts When Drawn</b>	Summon a 3/7 Mankrik,		who immediately attacks		the enemy hero.
		<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	"""
	play = Summon(CONTROLLER,'BAR_721t2'),Attack(FRIENDLY_MINIONS+ID('BAR_721t2'),ENEMY_HERO)
	pass
class BAR_721t2:
	"""Mankrik, Consumed by Hatred
	vanilla
	"""
	pass

class BAR_076:#OK
	"""
	Mor'shan Watch Post
	[x]Can't attack. After your opponent plays a minion, _summon a 2/2 Grunt.
<Tag enumID="227" name="CANT_ATTACK" type="Int" value="1"/>
	"""
	events = Play(OPPONENT,MINION).on(Summon(CONTROLLER,"BAR_076t"))
	pass
class BAR_076t:
	"""Watchful Grunt
	vanilla
	"""
	pass

class BAR_061:#OK
	"""
	Ratchet Privateer
	<b>Battlecry:</b> Give your weapon +1 Attack.
	"""
	play = Find(FRIENDLY_WEAPON) & Buff(FRIENDLY_WEAPON, "BAR_061e")
	pass
BAR_061e=buff(atk=1)

class BAR_025:#OK
	"""
	Sunwell Initiate
	<b>Frenzy:</b> Gain <b>Divine Shield</b>.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,SetTag(SELF, (GameTag.DIVINE_SHIELD,))))
	pass

class BAR_065:#OK
	"""
	Venomous Scorpid
	<b>Poisonous</b>
	<b>Battlecry:</b> <b>Discover</b> a spell.
	"""
	play = Discover(CONTROLLER, RandomSpell())
	pass

class BAR_078:#OK
	"""
	Blademaster Samuro
	[x]<b>Rush</b> <b>Frenzy:</b> Deal damage equal to this minion's Attack _to all enemy minions.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Hit(ENEMY_MINIONS,Attr(SELF, GameTag.ATK))))
	pass

class BAR_075:#OK (2回やれば2つつく。)
	"""
	Crossroads Watch Post
	[x]Can't attack. Whenever your opponent casts a spell, give your minions +1/+1.
<Tag enumID="227" name="CANT_ATTACK" type="Int" value="1"/>
	"""
	events = Play(OPPONENT,SPELL).on(Buff(FRIENDLY_MINIONS,"BAR_075e")) 
	pass
BAR_075e=buff(atk=1,health=1)

class BAR_027:#OK
	"""
	Darkspear Berserker
	<b>Deathrattle:</b> Deal 5 damage to your hero.
	"""
	deathrattle = Hit(FRIENDLY_HERO,5)
	pass

class BAR_070:#OK
	"""
	Gruntled Patron
	><b>Frenzy:</b> Summon another Gruntled Patron.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Summon(CONTROLLER,Copy(SELF))))
	pass

class BAR_069:#OK
	"""
	Injured Marauder
	<b>Taunt</b> <b>Battlecry:</b> Deal 6 damage to this minion.
	"""
	play = Hit(SELF,6)
	pass

class BAR_079_firstChoice(GenericChoice):
	secondChoice = ["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]# first choice
	def choose(self, card):
		super().choose(card)
		choiceCard = controller.hand[-1]
		choiceCardId = choiceCard.id
		choiceCard.zone = Zone.GRAVEYARD
		BAR_079_secondChoice(controller,RandomEntourage()*3).trigger(self)

class BAR_079:###OK
	"""
	Kazakus, Golem Shaper
	<b>Battlecry:</b> If your deck has no 4-Cost cards, build a custom Golem.
	First, choose one of 'cost 1, cost 5, cost 10'
	Next, choose one of 'rush, taunt, divine shield, life steal,  stealth, poisonous'

	"""
	entourage = ["BAR_079_m1","BAR_079_m2","BAR_079_m3"]# first choice
	powered_up = -Find(FRIENDLY_DECK + (COST==4))
	def play(self):
		controller = self.controller
		if self.powered_up:
			GenericChoiceBattlecry(controller,RandomEntourage()*3).trigger(self)
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
	<b>Rush</b> """
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
	<b>Taunt</b> """
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
	<b>Divine Shield</b> """
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
	<b>Lifesteal</b> """
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
	<b>Stealth</b> """
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
	<b>Poisonous</b> """
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
	return text.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')

class BAR_079t10:
	""" Wildvine
	<b>Battlecry:</b> Give your other minions +1/+1. """
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
	<b>Battlecry:</b> Give your other minions +2/+2. """
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
	<b>Battlecry:</b> Give your other minions +4/+4. """
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
	<b>Battlecry:</b> Summon a copy of this. """
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
	<b>Battlecry:</b> <b>Freeze</b> a random enemy minion. """
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
	<b>Battlecry:</b> <b>Freeze</b> two random enemy minions. """
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
	<b>Battlecry:</b> <b>Freeze</b> all enemy minions. """
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
	<b>Battlecry:</b> Deal 3 damage to a random enemy minion. """
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
	<b>Battlecry:</b> Deal 3 damage to two random enemy minions. """
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
	<b>Battlecry:</b> Deal 3 damage to all enemy minions. """
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
	<b>Spell Damage +1</b>. """
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
	<b>Spell Damage +2</b>. """
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
	<b>Spell Damage +4</b>. """
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
	<b>Battlecry:</b> Draw a card. """
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
	<b>Battlecry:</b> Draw 2 cards. """
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
	<b>Battlecry:</b> Draw 4 cards. """
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

class BAR_081:#OK
	"""
	Southsea Scoundrel
	<b>Battlecry:</b> <b>Discover</b> a card in your opponent's deck. They draw theirs as well.
	"""
	play = BAR_081_Southsea_Scoundrel(CONTROLLER,RANDOM(ENEMY_DECK)*3)
	pass

class BAR_744:#OK
	"""
	Spirit Healer
	After you cast a Holy spell, give a random friendly minion +2 Health.
	-
	"""
	events = Play(CONTROLLER, SPELL+HOLY).on(Buff(RANDOM_FRIENDLY_MINION,"BAR_744e"))
	pass
BAR_744e=buff(health=2)

class BAR_073:#OK
	"""
	Barrens Blacksmith
	<b>Frenzy:</b> Give your other minions +2/+2.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Buff(FRIENDLY_MINIONS - SELF,"BAR_073e")))
	pass
BAR_073e=buff(atk=2,health=2)

class BAR_072:#OK
	"""
	Burning Blade Acolyte
	<b>Deathrattle:</b> Summon a 5/8 Demonspawn with <b>Taunt</b>.
	"""
	deathrattle = Summon(CONTROLLER, "BAR_072t")
	pass
class BAR_072t:
	""" Demonspawn
	"""
	pass

class BAR_021:#OK
	"""
	Gold Road Grunt
	[x]<b>Taunt</b> <b>Frenzy:</b> Gain Armor equal to the damage taken.
	"""
	events = Damage(SELF).on(Frenzy(SELF,GainArmor(FRIENDLY_HERO,Damage.AMOUNT)))
	pass

class BAR_020:#OK
	"""
	Razormane Raider
	<b>Frenzy:</b> Attack a random enemy.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Attack(SELF,RANDOM_ENEMY_CHARACTER)))
	pass

class BAR_080:#OK
	"""
	Shadow Hunter Vol'jin
	<b>Battlecry:</b> Choose a minion. Swap it with a random one in its owner's hand.
	"""
	requirements = { PlayReq.REQ_MINION_TARGET: 0,	PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = SwapMinionAndHand(TARGET, RANDOM(FRIENDLY_HAND))
	pass

class BAR_071:#OK
	"""
	Taurajo Brave
	<b>Frenzy:</b> Destroy a random enemy minion.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Destroy(RANDOM(ENEMY_MINIONS))))
	pass

class BAR_077:#OK
	"""
	Kargal Battlescar
	[x]<b>Battlecry:</b> Summon a 5/5 Lookout for each Watch Post you've __summoned this game.
	"""
	play = Summon(CONTROLLER,"BAR_077t") * CountSummon(SELF,["BAR_074","BAR_075","BAR_076"])
	pass
class BAR_077t:
	""" Lookout """

class WC_030:#OK
	"""
	Mutanus the Devourer
	[x]<b>Battlecry:</b> Eat a minion in your opponent's hand. Gain its stats.
	"""
	play = EatsCard(SELF, RANDOM(ENEMY_HAND + MINION))
	pass
WC_030e=buff()

class WC_029:#OK
	"""
	Selfless Sidekick
	<b>Battlecry:</b> Equip a random weapon from your deck.
	"""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+WEAPON))
	pass

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
			log.info("Highest cost spell is %r (cost %d)"%(_card, _cost))
			log.info("Summon a minion of cost %d"%( _cost))
			Give(target,_card).trigger(source)
			_highestMinions = []
			for _card2 in target.deck:
				if _card2.type==CardType.MINION and _card2.cost == _cost:
					_highestMinions.append(_card2)
			if(len(_highestMinions)>0):
				_card2 = random.choice(_highestMinions)##
				Summon(target,_card2).trigger(source)
			else:
				log.info("no minion of cost %d"%( _cost))
		else:
			log.info("no spell is in the deck"%())

class BAR_042:#OK
	"""
	Primordial Protector
	[x]<b>Battlecry:</b> Draw your highest Cost spell. 
	Summon a random minion with the same Cost.
	"""
	play = BAR_042_Action(CONTROLLER) 
	pass

