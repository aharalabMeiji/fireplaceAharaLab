from ..utils import *

Arthas_DeathKnight=[]

Arthas_Howling_Blast=True
Arthas_Plague_Strike=True
Arthas_Icy_Touch=True
Arthas_Horn_of_Winter=True
Arthas_Unholy_Frenzy=True
Arthas_Dark_Transformation=True
Arthas_Nerubian_Swarmguard=True
Arthas_Frostwyrms_Fury=True
Arthas_Hematurge=True #
Arthas_Deathchiller=True
Arthas_Frostmourne=True
Arthas_Asphyxiate=True
Arthas_Ymirjar_Frostbreaker=True
Arthas_Tomb_Guardians=True
Arthas_The_Scourge=True
Arthas_Corpse_Bride=True
Arthas_Marrow_Manipulator=True
Arthas_Risen_Groom=True
Arthas_Glacial_Advance=True
Arthas_Bone_Breaker=True
Arthas_Freezy_Breezy=False #----->
Arthas_Vicious_Bloodworm=True
Arthas_Blood_Tap=True
Arthas_Lady_Deathwhisper=True
Arthas_Blood_Boil=True
Arthas_Darkfallen_Neophyte=True
Arthas_Might_of_Menethil=True
Arthas_Malignant_Horror=True



if Arthas_Howling_Blast:# 
	Arthas_DeathKnight+=['RLK_015']
class RLK_015_Action(TargetedAction):
	def do(self, source, target):
		Hit(target, 3).trigger(source)
		Freeze(target).trigger(source)
		for card in source.controller.opponent.characters:
			if card!=target:
				Hit(card, 1).trigger(source)
		pass
class RLK_015:# <1>[1869]
	""" Howling Blast (spell)
	Deal $3 damage to an enemy and <b>Freeze</b> it. Deal $1 damage to all other enemies. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	play = RLK_015_Action(TARGET)
	pass

if Arthas_Plague_Strike:# 
	Arthas_DeathKnight+=['RLK_018']
	Arthas_DeathKnight+=['RLK_018t']
class RLK_018_Action(TargetedAction):
	def do(self, source, target):
		Hit(target, 3).trigger(source)
		source.controller.game.process_deaths()
		if target.dead:
			Summon(source.controller, 'RLK_018t').trigger(source)
		pass
class RLK_018:# <1>[1869]
	""" Plague Strike (spell)
	Deal $3 damage to a minion. If that kills it, summon a 2/2 Zombie with <b>Rush</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}	#
	play = RLK_018_Action(TARGET)
	pass
class RLK_018t:# <12>[1776]
	""" Rampaging Zombie
	<b>Rush</b> """
	#
	pass

if Arthas_Icy_Touch:# 
	Arthas_DeathKnight+=['RLK_038']
class RLK_038:# <1>[1869]
	""" Icy Touch
	Deal $2 damage to an enemy and <b>Freeze</b> it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	play = Hit(TARGET, 2), Freeze(TARGET)
	pass

if Arthas_Horn_of_Winter:# 
	Arthas_DeathKnight+=['RLK_042']
class RLK_042:# <1>[1869]
	""" Horn of Winter
	Refresh 2 Mana Crystals. """
	play = RefreshMana(CONTROLLER, 2)
	pass

if Arthas_Unholy_Frenzy:# 
	Arthas_DeathKnight+=['RLK_056']
class RLK_056_Action(TargetedAction):
	def do(self, source, target):
		killed=[]
		for card in reversed(source.controller.field):
			RegularAttack(card, target).trigger(source)
			source.controller.game.process_deaths()
			if card.dead:
				killed.append(card.id)
		for cardID in killed:
			Summon(source.controller, cardID).trigger(source)
		pass
class RLK_056:# <1>[1869]
	""" Unholy Frenzy
	Choose an enemy minion. Your minions attack it. Resummon any that die. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	play = RLK_056_Action(TARGET)
	pass

if Arthas_Dark_Transformation:# 
	Arthas_DeathKnight+=['RLK_057']
	Arthas_DeathKnight+=['RLK_057t']
class RLK_057:# <1>[1869]
	""" Dark Transformation
	Transform an Undead into a 4/5 Undead Monstrosity with <b>Rush</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.UNDEAD }	#
	play = Morph(TARGET, 'RLK_057t')
	pass
class RLK_057t:# <1>[1869]
	""" Undead Monstrosity
	<b>Rush</b> """
	#
	pass

if Arthas_Nerubian_Swarmguard:# 
	Arthas_DeathKnight+=['RLK_062']
class RLK_062:# <1>[1869]
	""" Nerubian Swarmguard
	<b>Taunt</b> <b>Battlecry:</b> Summon two copies of this minion. """
	play = Summon(CONTROLLER, ExactCopy(SELF)) * 2
	pass

if Arthas_Frostwyrms_Fury:# 
	Arthas_DeathKnight+=['RLK_063']
	Arthas_DeathKnight+=['RLK_063t']
class RLK_063:# <1>[1869]
	""" Frostwyrm's Fury
	Deal $5 damage. <b>Freeze</b> all enemy minions. Summon a 5/5 Frostwyrm. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	play = Hit(TARGET, 5), Freeze(ENEMY_MINIONS), Summon(CONTROLLER, 'RLK_063t')
	pass
class RLK_063t:# <1>[1869]
	""" Frostwyrm
	 """	#
	pass

if Arthas_Hematurge:# ### OK ###
	Arthas_DeathKnight+=['RLK_066']
class RLK_066_Action(GameAction):
	def do(self, source):
		controller = source.controller
		if controller.corpse>0:
			SpendCorpse(controller, 1).trigger(source)
			Discover(controller, RandomBloodRune()).trigger(source)# COST_BLOOD
		pass
class RLK_066:# <1>[1869]
	""" Hematurge
	<b>Battlecry:</b> Spend a <b>Corpse</b> to <b>Discover</b> a Blood Rune card. """
	play = RLK_066_Action()
	pass

if Arthas_Deathchiller:# 
	Arthas_DeathKnight+=['RLK_083']
class RLK_083:# <1>[1869]
	""" Deathchiller
	After you cast a spell, deal 1 damage to two random enemies. """
	events = OWN_SPELL_PLAY.after(Hit(RANDOM(ENEMY_MINIONS), 1), Hit(RANDOM(ENEMY_MINIONS), 1))
	pass

if Arthas_Frostmourne:# ### 
	Arthas_DeathKnight+=['RLK_086']
class RLK_086_Action1(TargetedAction):
	def do(self, source, target):
		# if it is killed
		source.sidequest_list0.append(target.id)
		pass
class RLK_086_Action2(GameAction):
	def do(self, source):
		for card in source.sidequest_list0:
			Summon(source.controller, card).trigger(source)
		pass
class RLK_086:# <1>[1869]
	""" Frostmourne
	<b>Deathrattle:</b> Summon every minion killed by this weapon. """
	events = Attack(FRIENDLY_HERO).after(RLK_086_Action1(Attack.DEFENDER))
	deathrattle = RLK_086_Action2()
	pass

if Arthas_Asphyxiate:# 
	Arthas_DeathKnight+=['RLK_087']
class RLK_087_Action(GameAction):
	def do(self, source):
		high=[]
		for card in source.controller.opponent.field:
			if card.type==CardType.MINION:
				if high==[] or high[0].atk<card.atk:
					high=[card]
				elif high[0].atk==card.atk:
					high.append(card)
		if len(high):
			card = random.choice(high)
			Destroy(card).trigger(source)
		pass
class RLK_087:# <1>[1869]
	""" Asphyxiate
	Destroy the highest Attack enemy minion. """
	play = RLK_087_Action()
	pass

if Arthas_Ymirjar_Frostbreaker:# 
	Arthas_DeathKnight+=['RLK_110']
	Arthas_DeathKnight+=['RLK_110e']
class RLK_110_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.FROST]
		if len(cards):
			Buff(source, 'RLK_110e', atk=len(cards)).trigger(source)
		pass
class RLK_110:# <1>[1869]
	""" Ymirjar Frostbreaker
	<b>Battlecry:</b> Gain +1_Attack for each Frost spell in your hand. """
	play = RLK_110_Action()
	pass
class RLK_110e:# <1>[1869]
	""" Shattering Strength	+1 Attack. """
	pass

if Arthas_Tomb_Guardians:# 
	Arthas_DeathKnight+=['RLK_118']
	Arthas_DeathKnight+=['RLK_118t3']
class RLK_118_Action(GameAction):
	def do(self, source):
		controller = source.controller
		for repeat in range(2):
			card = get00(Summon(controller, 'RLK_118t3').trigger(source))
			if controller.corpse>=4:
				SpendCorpse(controller, 4).trigger(source)
				card.reborn = True
		pass
class RLK_118:# <1>[1869]
	""" Tomb Guardians
	Summon two 2/2 Zombies with <b>Taunt</b>. Spend 4 <b>Corpses</b> to give them <b>Reborn</b>. """
	play = RLK_118_Action()
	pass
class RLK_118t3:# <1>[1869]
	""" Menacing Zombie
	<b>Taunt</b> """
	#
	pass

if Arthas_The_Scourge:# 
	Arthas_DeathKnight+=['RLK_122']
class RLK_122_Action(GameAction):
	def do(self, source):
		controller=source.controller
		amount=7-len(controller.field)
		for repeat in range(amount):
			card = get00(RandomMinion(race=Race.UNDEAD).evaluate(source))
			card.zone=Zone.PLAY
		pass
class RLK_122:# <1>[1869]
	""" The Scourge
	Fill your board with random Undead. """
	play = RLK_122_Action()
	pass

if Arthas_Corpse_Bride:# 
	Arthas_DeathKnight+=['RLK_504']#RLK_506t(1/1/1)
class RLK_504_Action(GameAction):
	def do(self, source):
		controller=source.controller
		amount = min(controller.corpse, 8)
		SpendCorpse(controller, amount).trigger(source)
		card = get00(Summon(controller, 'RLK_506t').trigger(source))
		if amount>1:
			Buff(card, 'RLK_504_e', atk=amount-1, max_health=amount-1).trigger(source)
		pass
class RLK_504:# <1>[1869]
	""" Corpse Bride
	<b>Battlecry:</b> Spend up to 8 <b>Corpses</b>. Summon a Risen Groom with stats equal to the amount spent. """
	play = RLK_504_Action()
	pass
@custom_card
class RLK_504_e:
	tags = {
		GameTag.CARDNAME: "Corpse Bride",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}

if Arthas_Marrow_Manipulator:# 
	Arthas_DeathKnight+=['RLK_505']
class RLK_505_Action(GameAction):
	def do(self, source):
		controller=source.controller
		amount = min(5, controller.corpse)
		SpendCorpse(controller, amount).trigger(source)
		for repeat in range(amount):
			target = random.choice(controller.opponent.characters)
			Hit(target, 2).trigger(source)
		pass
class RLK_505:# <1>[1869]
	""" Marrow Manipulator
	<b>Battlecry:</b> Spend up to 5 <b>Corpses</b>. Deal 2 damage to a random enemy for each. """
	play = RLK_505_Action()
	pass

if Arthas_Risen_Groom:# 
	Arthas_DeathKnight+=['RLK_506t']
class RLK_506t:# <1>[1869]
	""" Risen Groom
	<i>Doesn't leave a <b>Corpse</b>.</i> """
	# this is not collectible.
	# implementation in class Death.
	pass

if Arthas_Glacial_Advance:# 
	Arthas_DeathKnight+=['RLK_512']
class RLK_512:# <1>[1869]
	""" Glacial Advance
	Deal $4 damage. Your next spell this turn costs (2) less. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	play = Hit(TARGET, 4), Buff(FRIENDLY_HAND, 'RLK_512_e')
	pass
@custom_card
class RLK_512_e:
	tags = {
		GameTag.CARDNAME: "Glacial Advance",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}
	events = [ OWN_SPELL_PLAY.on(Destroy(SELF)), OWN_TURN_END.on(Destroy(SELF))]
	cost = lambda self, i:max(i-2,0)

if Arthas_Bone_Breaker:# 
	Arthas_DeathKnight+=['RLK_516']
class RLK_516:# <1>[1869]
	""" Bone Breaker
	After your hero attacks a minion, deal 2 damage to the enemy hero. """
	events = Attack(FRIENDLY_HERO, MINION).after(Hit(ENEMY_HERO, 2))
	pass

if Arthas_Freezy_Breezy:# 
	Arthas_DeathKnight+=['RLK_710e']
class RLK_710e:# <1>[1869]
	""" Freezy Breezy
	Costs (1) less. """
	#
	pass

if Arthas_Vicious_Bloodworm:# 
	Arthas_DeathKnight+=['RLK_711']
	Arthas_DeathKnight+=['RLK_711e']
class RLK_711_Action(GameAction):
	def do(self, source):
		controller = source.controller
		if len(controller.hand):
			card = random.choice(controller.hand)
			Buff(card, 'RLK_711e', atk=source.atk).trigger(source)
		pass
class RLK_711:# <1>[1869]
	""" Vicious Bloodworm
	<b>Battlecry:</b> Give a minion in your hand Attack equal to this minion's Attack. """
	play = RLK_711_Action()
	pass
class RLK_711e:# <1>[1869]
	""" Blood Gift
	Increased Attack. """

if Arthas_Blood_Tap:# 
	Arthas_DeathKnight+=['RLK_712']
	Arthas_DeathKnight+=['RLK_712e']
class RLK_712_Action(GameAction):
	def do(self, source):
		controller =source.controller
		for card in controller.hand:
			Buff(card, 'RLK_712e').trigger(source)
		if controller.corpse>=3:
			SpendCorpse(controller, 3).trigger(source)
			for card in controller.hand:
				Buff(card, 'RLK_712e').trigger(source)
		pass
class RLK_712:# <1>[1869]
	""" Blood Tap
	Give all minions in your hand +1/+1. Spend 3 <b>Corpses</b> to give them +1/+1 more. """
	play = RLK_712_Action()
	pass
RLK_712e=buff(1,1)
""" Tapped Blood	+1/+1. """


if Arthas_Lady_Deathwhisper:# 
	Arthas_DeathKnight+=['RLK_713']
class RLK_713_Action(GameAction):
	def do(self, source):
		controller = source.controller
		cards=[card.id for card in controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.FROST]
		for cardID in cards:
			Give(controller, cardID).trigger(source)
		pass
class RLK_713:# <1>[1869]
	""" Lady Deathwhisper
	<b>Deathrattle:</b> Copy all Frost spells in your hand. """
	deathrattle = RLK_713_Action()
	pass

if Arthas_Blood_Boil:# 
	Arthas_DeathKnight+=['RLK_730']
	Arthas_DeathKnight+=['RLK_730e']
class RLK_730:# <1>[1869]
	""" Blood Boil
	<b>Lifesteal</b> Infect all enemy minions. At the end of your turns, they take 2 damage. """
	play = Buff(ENEMY_MINIONS, 'RLK_730e')
	pass
class RLK_730e:# <1>[1869]
	""" Boiling Blood
	At the end of your opponent's turns, take 2 damage. """
	events = EndTurn(CONTROLLER).on(Hit(OWNER, 2))
	pass

if Arthas_Darkfallen_Neophyte:# 
	Arthas_DeathKnight+=['RLK_731']
	Arthas_DeathKnight+=['RLK_731e']
class RLK_731_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if controller.corpse>=2:
			SpendCorpse(controller, 2).trigger(source)
			for card in controller.hand:
				if card.type==CardType.MINION:
					Buff(card, 'RLK_731e').trigger(source)
		pass
class RLK_731:# <1>[1869]
	""" Darkfallen Neophyte
	<b>Battlecry:</b> Spend 2 <b>Corpses</b> to give all minions in your hand +2 Attack. """
	play = RLK_731_Action()
	pass
RLK_731e=buff(2,0)
""" Fallen to Dark	+2 Attack. """


if Arthas_Might_of_Menethil:# 
	Arthas_DeathKnight+=['RLK_740']
class RLK_740_Action(GameAction):
	def do(self, source):
		controller=source.controller
		amount = min(3,controller.corpse)
		cards = [card for card in controller.opponent.field if card.type==CardType.MINION]
		amount = min(amount, len(cards))
		if len(cards)>amount:
			cards = random.sample(cards, amount)
		for card in cards:
			Freeze(card).trigger(source)
		pass
class RLK_740:# <1>[1869]
	""" Might of Menethil
	<b>Battlecry:</b> Spend up to 3 <b>Corpses</b>. <b>Freeze</b> that many enemy minions. """
	play = RLK_740_Action()
	pass

if Arthas_Malignant_Horror:# 
	Arthas_DeathKnight+=['RLK_745']
class RLK_745_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if controller.corpse>=5:
			SpendCorpse(controller, 5).trigger(source)
			Summon(controller,'RLK_745').trigger(source)
		pass
class RLK_745:# <1>[1869]
	""" Malignant Horror
	<b>Reborn</b> At the end of your turn, spend 5 <b>Corpses</b> to summon a copy of this minion. """
	events = OWN_TURN_END.on(RLK_745_Action())
	pass

