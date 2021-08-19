from ..utils import *

####### neutral in savior,  45 cards#######

class ULD_191:#OK
	"""Beaming Sidekick		1	1	2	Minion	Common	-	Battlecry
	<b>Battlecry:</b> Give a friendly minion +2 Health."""
	play = Buff(RANDOM(FRIENDLY_MINIONS - SELF), "ULD_191e")
ULD_191e = buff(0,2)

class ULD_282:#OK
	"""Jar Dealer		1	1	1	Minion	Common	-	Deathrattle
	[x]<b>Deathrattle:</b> Add a random
	1-Cost minion to your hand."""
	deathrattle = Give(CONTROLLER,RandomMinion(cost=1))

class ULD_705:#OK
	"""Mogu Cultist		1	1	1	Minion	Epic	-	Battlecry
	<b>Battlecry:</b> If your board is full of Mogu Cultists, sacrifice them all and summon Highkeeper Ra."""
	powered_up = Count(FRIENDLY_MINIONS + ID('ULD_705'))==8
	play = powered_up & Destroy(FRIENDLY_MINIONS + ID('ULD_705')).then( -Find(FRIENDLY_MINIONS+ID('ULD_705t')) & Summon(CONTROLLER, "ULD_705t"))
class ULD_705t:#OK
	""" Highkeeper Ra
	At the end of your turn, deal 20 damage to all_enemies."""
	events = OWN_TURN_END.on(Hit(ENEMY_CHARACTERS,20))

class ULD_723:#OK
	"""Murmy		1	1	1	Minion	Common	Murloc	Reborn
	<b>Reborn</b>"""
	pass

class ULD_712:#OK
	"""Bug Collector		2	2	1	Minion	Common	-	Battlecry
	<b>Battlecry:</b> Summon a 1/1 Locust with <b>Rush</b>."""
	play = Summon(CONTROLLER, "ULD_430t")

class ULD_309:#OK
	"""Dwarven Archaeologist		2	2	3	Minion	Epic	-	Discover
	After you <b>Discover</b> a card, reduce its cost by (1)."""
	play = Choice(CONTROLLER, RandomMinion()*3).then(Give(CONTROLLER, Choice.CARD).then(Buff(Give.CARD, "ULD_309e")))
ULD_309e = buff(cost=-1)

class ULD_289:
	"""Fishflinger		2	3	2	Minion	Common	Murloc	Battlecry
	<b>Battlecry:</b> Add a
	random Murloc to each player's_hand."""
	play = Give(CONTROLLER, RandomMurloc()), Give(OPPONENT, RandomMurloc())

class ULD_271:#OK
	"""Injured Tol'vir		2	2	6	Minion	Common	-	Battlecry
	<b>Taunt</b>
	<b>Battlecry:</b> Deal 3 damage to this minion."""
	play = Hit(SELF, 3)

class ULD_184:#OK
	"""Kobold Sandtrooper		2	2	1	Minion	Common	-	Deathrattle
	<b>Deathrattle:</b> Deal 3 damage to the enemy_hero."""
	deathrattle = Hit(ENEMY_HERO, 3)

class ULD_196:#OK
	"""Neferset Ritualist		2	2	3	Minion	Rare	-	Battlecry
	<b>Battlecry:</b> Restore adjacent minions to full_Health."""
	play = FullHeal(SELF_ADJACENT)

##### 10 #####


class ULD_157:#OK
	"""Questing Explorer		2	2	3	Minion	Rare	-	Battlecry
	<b>Battlecry:</b> If you control a <b>Quest</b>, draw a card."""
	play = Find(EnumSelector(Zone.SECRET) + FRIENDLY + EnumSelector(GameTag.SIDEQUEST)) & Draw(CONTROLLER)

class ULD_197:#OK
	"""Quicksand Elemental		2	3	2	Minion	Rare	Elemental	Battlecry
	<b>Battlecry:</b> Give all enemy minions -2 Attack this_turn."""
	play = Buff(ENEMY_MINIONS, "ULD_197e")
class ULD_197e:
	atk = lambda self, i: i-2
	events = OWN_TURN_END.on(Destroy(SELF))

class ULD_174:#OK
	"""Serpent Egg		2	0	3	Minion	Common	-	Deathrattle
	<b>Deathrattle:</b> Summon a 3/4 Sea Serpent."""
	deathrattle = Summon(CONTROLLER, "ULD_174t")
class ULD_174t:
	"""Sea Serpent """
	pass

class ULD_182:#OK
	"""Spitting Camel		2	2	4	Minion	Common	Beast	-
	[x]At the end of your turn,
	__deal 1 damage to another__
	random friendly minion."""
	play = OWN_TURN_END.on(Hit(RANDOM(FRIENDLY_MINIONS-SELF), 1))

class ULD_185:########'while damaged'#####################
	"""Temple Berserker		2	1	2	Minion	Common	-	Reborn
	<b>Reborn</b>
	Has +2 Attack while damaged."""
	update = Find(SELF + DAMAGED) & BuffOnce(SELF, "ULD_185e")
ULD_185e = buff(2,0)

class ULD_450:#OK
	"""Vilefiend		2	2	2	Minion	Common	Demon	Lifesteal
	<b>Lifesteal</b>"""

class ULD_003:# mimic#OK
	"""Zephrys the Great		2	3	2	Minion	Legendary	Elemental	Battlecry
	<b>Battlecry:</b> If your deck has no duplicates, wish for the perfect card."""
	def play(self):
		powered_up = -FindDuplicates(FRIENDLY_DECK)
		if powered_up:
			entourage=['CS2_046','CS2_011']##Bloodlust, Savage Roar
			if self.controller.opponent.hero.health<10:
				entourage=['BT_512','CS2_029','EX1_241','EX1_308']#Inner Demon, Fireball, Lava Burst, Soulfire
			else:
				for card in self.controller.opponent.field:
					if card.taunt == True and card.max_health-card.damage>2:
						entourage=['EX1_626','EX1_303','EX1_332']#Mass Dispel, Shadowflame, Silence
						break
			card = random.choice(entourage)
			Give(self.controller, card).trigger(self.controller)

class ULD_205:#OK
	"""Candletaker		3	3	2	Minion	Common	-	Reborn
	<b>Reborn</b>"""

class ULD_719:#OK
	"""Desert Hare		3	1	1	Minion	Common	Beast	Battlecry
	<b>Battlecry:</b> Summon two 1/1 Desert Hares."""
	play = Summon(CONTROLLER, "ULD_719")*2

class ULD_214:#OK
	"""Generous Mummy		3	5	4	Minion	Rare	-	Reborn
	<b>Reborn</b>
	Your opponent's cards cost (1) less."""
	play = Buff(ENEMY_HAND, "ULD_214e")
ULD_214e = buff(cost=-1)

#####20#####

class ULD_188:#OK
	"""Golden Scarab		3	2	2	Minion	Common	Beast	Battlecry
	<b><b>Battlecry:</b> Discover</b> a
	4-Cost card."""
	play = Discover(CONTROLLER, RandomCollectible(cost=4))

class ULD_290:#OK
	"""History Buff		3	3	4	Minion	Epic	-	-
	Whenever you play a minion, give a random minion in your hand +1/+1."""
	events = Play(CONTROLLER, MINION).on(Buff(RANDOM(FRIENDLY_HAND + MINION), "ULD_290e"))
ULD_290e=buff(1,1)

class ULD_250:#OK
	"""Infested Goblin		3	2	3	Minion	Rare	-	Deathrattle
	<b>Taunt</b>
	<b>Deathrattle:</b> Add two 1/1 Scarabs with <b>Taunt</b> to your hand."""
	deathrattle = Give(CONTROLLER, "ULD_215t")*2

class ULD_229:#OK
	"""Mischief Maker		3	3	3	Minion	Epic	-	Battlecry
	<b>Battlecry:</b> Swap the top card of your deck with your_opponent's."""
	def play(self):
		controller = self.controller
		opponent = controller.opponent
		controller.deck[-1], opponent.deck[-1] = opponent.deck[-1], controller.deck[-1]
		pass

class ULD_209:#OK
	"""Vulpera Scoundrel		3	2	3	Minion	Epic	-	Battlecry
	<b>Battlecry</b>: <b>Discover</b> a spell or pick a mystery choice."""
	choose = ("ULD_209", "ULD_209t")
	play = Discover(CONTROLLER, RandomSpell())
class ULD_209t:
	"""Mystery Choice!
	Add a random spell to your hand.""" 
	play = Give(CONTROLLER, RandomSpell())

class ULD_727:#OK
	"""Body Wrapper		4	4	4	Minion	Epic	-	Battlecry
	<b>Battlecry:</b> <b>Discover</b> a friendly minion that died this game. Shuffle it into your deck."""
	play = Choice(CONTROLLER, RANDOM(FRIENDLY + KILLED)*3).then(Shuffle(CONTROLLER, Choice.CARD))

class ULD_275:#OK
	"""Bone Wraith		4	2	5	Minion	Common	-	Reborn
	<b>Taunt</b>
	<b>Reborn</b>"""
	
class ULD_198:#OK
	"""Conjured Mirage		4	3	10	Minion	Rare	-	Taunt
	<b>Taunt</b>
	At the start of your turn, shuffle this minion into your deck."""
	play = OWN_TURN_BEGIN.on(Shuffle(CONTROLLER, SELF))

class ULD_180:#OK ###1-turn-asleep = dormant###
	"""Sunstruck Henchman		4	6	5	Minion	Rare	-	-
	At the start of your turn, this has a 50% chance to_fall asleep."""
	#play = OWN_TURN_BEGIN.on(COINFLIP & SetTag(SELF,(GameTag.SLEEP,)))
	play = OWN_TURN_BEGIN.on(COINFLIP & SetAttr(SELF, 'dormant',2))

class ULD_703:#OK
	"""Desert Obelisk		5	0	5	Minion	Epic	-	-
	[x]If you control 3 of these
	at the end of your turn,
	deal 5 damage to a
	random enemy."""
	events = OWN_TURN_END.on(ULD703DesertObelisk(SELF))
	#powered_up = Count(FRIENDLY_MINIONS + ID("ULD_703"))==3
	#play = powered_up & Hit(RANDOM(ENEMY_CHARACTERS),5)

##### 30 #####

class ULD_189:#OK
	"""Faceless Lurker		5	3	3	Minion	Common	-	Battlecry
	<b>Taunt</b>
	<b>Battlecry:</b> Double this minion's Health."""
	play = Buff(SELF, "ULD_189e")
class ULD_189e:
	max_health = lambda self, i : i*2

class ULD_702:#OK
	"""Mortuary Machine		5	8	8	Minion	Epic	Mech	Reborn
	After your opponent plays a minion, give it <b>Reborn</b>."""
	play = Play(OPPONENT,MINION).after(SetTag(Play.CARD, (GameTag.REBORN, )))

class ULD_179:#OK
	"""Phalanx Commander		5	4	5	Minion	Common	-	Taunt
	Your <b>Taunt</b> minions
	have +2 Attack."""
	play = Buff(FRIENDLY_MINIONS + TAUNT,"ULD_179e")
ULD_179e=buff(2,0)

class ULD_274:#OK
	"""Wasteland Assassin		5	4	2	Minion	Common	-	Reborn
	<b>Stealth</b>
	<b>Reborn</b>"""
	pass

class ULD_706:#OK
	"""Blatant Decoy		6	5	5	Minion	Epic	-	Deathrattle
	[x]<b>Deathrattle:</b> Each player
	summons the lowest Cost
	minion from their hand."""
	deathrattle = Summon(CONTROLLER, RandomMinion(cost= OpAttr(FRIENDLY_HAND+MINION, GameTag.COST, min))), Summon(OPPONENT, RandomMinion(cost= OpAttr(ENEMY_HAND+MINION, GameTag.COST, min)))

class ULD_208:#OK
	"""Khartut Defender		6	3	4	Minion	Rare	-	Deathrattle
	[x]<b>Taunt</b>, <b>Reborn</b>
	<b>Deathrattle:</b> Restore #3
	Health to your hero."""
	deathrattle = Heal(FRIENDLY_HERO, 3)

class ULD_178:# OK for once ##################  ( how we do twice? )
	"""Siamat		7	6	6	Minion	Legendary	Elemental	Battlecry
	[x]<b>Battlecry:</b> Gain 2 of <b>Rush</b>,
	<b>Taunt</b>, <b>Divine Shield</b>, or
	<b>Windfury</b> <i>(your choice).</i>"""
	choose = ('ULD_178a', 'ULD_178a2', 'ULD_178a3', 'ULD_178a4')

class ULD_178a:
	play = SetTag(FRIENDLY_MINIONS + ID('ULD_178'),(GameTag.RUSH, ))
class ULD_178a2:
	play = SetTag(FRIENDLY_MINIONS + ID('ULD_178'),(GameTag.TAUNT, ))
class ULD_178a3:
	play = SetTag(FRIENDLY_MINIONS + ID('ULD_178'),(GameTag.DIVINE_SHIELD, ))
class ULD_178a4:
	play = SetTag(FRIENDLY_MINIONS + ID('ULD_178'),(GameTag.WINDFURY, ))

class ULD_194:#OK
	"""Wasteland Scorpid		7	3	9	Minion	Common	Beast	Poisonous
	<b>Poisonous</b>"""
	pass

class ULD_215:#OK
	"""Wrapped Golem		7	7	5	Minion	Rare	-	Reborn
	[x]<b>Reborn</b>
	At the end of your turn,
	summon a 1/1 Scarab
	with <b>Taunt</b>."""
	events = OWN_TURN_END.on(Summon(CONTROLLER, "ULD_215t"))
class ULD_215t:
	pass

class ULD_177:#OK
	"""Octosari		8	8	8	Minion	Legendary	Beast	Deathrattle
	<b>Deathrattle:</b> Draw 8 cards."""
	deathrattle = Draw(CONTROLLER) * 8

##### 40 #####

class ULD_190:#OK
	"""Pit Crocolisk		8	5	6	Minion	Common	Beast	Battlecry
	<b>Battlecry:</b> Deal 5 damage."""
	requirements = { PlayReq.REQ_MINION_OR_ENEMY_HERO:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Hit(TARGET, 5)

class ULD_183:#OK
	"""Anubisath Warbringer		9	9	6	Minion	Common	-	Deathrattle
	<b>Deathrattle:</b> Give all minions in your hand +3/+3."""
	deathrattle = Buff(FRIENDLY_HAND + MINION, "ULD_183e")
ULD_183e = buff(3,3)

class ULD_721:#OK
	"""Colossus of the Moon		10	10	10	Minion	Legendary	-	Divine Shield
	<b>Divine Shield</b>
	<b>Reborn</b>"""
	pass

class ULD_304:#OK
	"""King Phaoris		10	5	5	Minion	Legendary	-	Battlecry
	[x]<b>Battlecry:</b> For each spell
	in your hand, summon a
	random minion of the
	same Cost."""
	def play(self):
		hands = self.controller.hand
		for card in hands:
			if card.type == CardType.SPELL:
				cost = card.cost
				Summon(self.controller, RandomMinion(cost=cost)).trigger(self)
			
class ULD_193:#OK
	"""Living Monument		10	10	10	Minion	Common	-	Taunt
	<b>Taunt</b>"""
	pass
