from ..utils import *

####### neutral in savior,  45 cards#######

class ULD_191:
	"""Beaming Sidekick		1	1	2	Minion	Common	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly minion +2 Health."""
	play = Buff(RANDOM(FRIENDLY_MINIONS), {GameTag.HEALTH: 2})
#ULD_191e = buff(0,2) use this elsewhere

class ULD_282:
	"""Jar Dealer		1	1	1	Minion	Common	-	Deathrattle
	[x]&lt;b&gt;Deathrattle:&lt;/b&gt; Add a random
	1-Cost minion to your hand."""
	deathrattle = Give(CONTROLLER,RandomMinion(cost=1))

class ULD_705:
	"""Mogu Cultist		1	1	1	Minion	Epic	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If your board is full of Mogu Cultists, sacrifice them all and summon Highkeeper Ra."""
	powered_up = Count(FRIENDLY_MINIONS + ID('ULD_705'))==8
	play = powered_up & Destroy(FRIENDLY_MINIONS + ID('ULD_705')), Summon(CONTROLLER, "ULD_705t")
class ULD_705t:
	""" Highkeeper Ra
	At the end of your turn, deal 20 damage to all_enemies."""
	play = OWN_TURN_END.on(Damage(ENEMY_CHARACTERS,20))

class ULD_723:#OK
	"""Murmy		1	1	1	Minion	Common	Murloc	Reborn
	&lt;b&gt;Reborn&lt;/b&gt;"""
	pass

class ULD_712:
	"""Bug Collector		2	2	1	Minion	Common	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 1/1 Locust with &lt;b&gt;Rush&lt;/b&gt;."""
	play = Summon(CONTROLLER, "ULD_430t")

class ULD_309:
	"""Dwarven Archaeologist		2	2	3	Minion	Epic	-	Discover
	After you &lt;b&gt;Discover&lt;/b&gt; a card, reduce its cost by (1)."""
	play = Discover(RandomCollectible()).after(Buff(Discover.CARDS, "ULD_309e"))
class ULD_309e:
	cost = SET(1)

class ULD_289:
	"""Fishflinger		2	3	2	Minion	Common	Murloc	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Add a
	random Murloc to each player's_hand."""
	play = Give(CONTROLLER, RandomMurloc()), Give(OPPONENT, RandomMurloc())

class ULD_271:
	"""Injured Tol'vir		2	2	6	Minion	Common	-	Battlecry
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 3 damage to this minion."""
	play = Hit(SELF, 3)

class ULD_184:
	"""Kobold Sandtrooper		2	2	1	Minion	Common	-	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 3 damage to the enemy_hero."""
	deathrattle = Hit(ENEMY_HERO, 3)

class ULD_196:
	"""Neferset Ritualist		2	2	3	Minion	Rare	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Restore adjacent minions to full_Health."""
	play = FullHeal(SELF_ADJACENT)

##### 10 #####


class ULD_157:
	"""Questing Explorer		2	2	3	Minion	Rare	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a &lt;b&gt;Quest&lt;/b&gt;, draw a card."""
	play = Find(FRIENDLY_CHARACTERS + SECRET) & Draw(CONTROLLER)

class ULD_197:
	"""Quicksand Elemental		2	3	2	Minion	Rare	Elemental	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Give all enemy minions -2 Attack this_turn."""
	play = Buff(ENEMY_MINIONS, "ULD_197e")
class ULD_197e:
   atk =-2
   play = OWN_TURN_END.on(Destroy(SELF))

class ULD_174:
	"""Serpent Egg		2	0	3	Minion	Common	-	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 3/4 Sea Serpent."""
	deathrattle = Summon(CONTROLLER, "ULD_174t")
class ULD_174t:
	"""Sea Serpent """
	pass
class ULD_182:
	"""Spitting Camel		2	2	4	Minion	Common	Beast	-
	[x]At the end of your turn,
	__deal 1 damage to another__
	random friendly minion."""
	play = OWN_TURN_END.on(Hit(RANDOM(FRIENDLY_MINIONS), 1))

class ULD_185:
	"""Temple Berserker		2	1	2	Minion	Common	-	Reborn
	&lt;b&gt;Reborn&lt;/b&gt;
	Has +2 Attack while damaged."""
	update = (CURRENT_HEALTH(SELF)<MAX_HEALTH(SELF)) & Buff(SELF, "ULD_185e")
ULD_185e = buff(2,0)

class ULD_450:
	"""Vilefiend		2	2	2	Minion	Common	Demon	Lifesteal
	&lt;b&gt;Lifesteal&lt;/b&gt;"""

class ULD_003:########################## mimic
	"""Zephrys the Great		2	3	2	Minion	Legendary	Elemental	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has no duplicates, wish for the perfect card."""
	def play(self):
		powered_up = FindDuplicates(FRIENDLY_DECK)
		if not powered_up:
			entourage=['CS2_046','CS2_011']##Bloodlust, Savage Roar
			if self.controller.opponent.health<10:
				entourage=['BT_512','CS2_029','EX1_241','EX1_308']#Inner Demon, Fireball, Lava Burst, Soulfire
			else:
				for card in self.controller,opponent.field:
					if card.taunt == True and card.max_health-card.damage>2:
						entourage=['EX1_626','EX1_303','EX1_332']#Mass Dispel, Shadowflame, Silence
						break
			Give(CONTROLLER,RandomEntourage())

class ULD_205:
	"""Candletaker		3	3	2	Minion	Common	-	Reborn
	&lt;b&gt;Reborn&lt;/b&gt;"""

class ULD_719:
	"""Desert Hare		3	1	1	Minion	Common	Beast	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon two 1/1 Desert Hares."""
	play = Summon(CONTROLLER, "ULD_719")*2

class ULD_214:
	"""Generous Mummy		3	5	4	Minion	Rare	-	Reborn
	&lt;b&gt;Reborn&lt;/b&gt;
	Your opponent's cards cost (1) less."""
	play = Buff(ENEMY_HAND, "ULD_214e")
class ULD_214e:
	cost=-1
#####20#####

class ULD_188:
	"""Golden Scarab		3	2	2	Minion	Common	Beast	Battlecry
	&lt;b&gt;&lt;b&gt;Battlecry:&lt;/b&gt; Discover&lt;/b&gt; a
	4-Cost card."""
	play = Discover(CONTROLLER, RandomCollectible(cost=4))

class ULD_290:
	"""History Buff		3	3	4	Minion	Epic	-	-
	Whenever you play a minion, give a random minion in your hand +1/+1."""
	events = Play(CONTROLLER, MINION).on(Buff(RANDOM(FRIENDLY_HAND + MINION), "ULD_290e"))
ULD_290e=buff(1,1)

class ULD_250:
	"""Infested Goblin		3	2	3	Minion	Rare	-	Deathrattle
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Deathrattle:&lt;/b&gt; Add two 1/1 Scarabs with &lt;b&gt;Taunt&lt;/b&gt; to your hand."""
	deathrattle = Give(CONTROLLER, "LOE_009t")

class ULD_229:
	"""Mischief Maker		3	3	3	Minion	Epic	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Swap the top card of your deck with your_opponent's."""
	def play(self):
		controller = self.controller
		opponent = controller.opponent
		controller.deck[-1], opponent.deck[-1] = opponent.deck[-1], controller.deck[-1]
		pass

class ULD_209:
	"""Vulpera Scoundrel		3	2	3	Minion	Epic	-	Battlecry
	&lt;b&gt;Battlecry&lt;/b&gt;: &lt;b&gt;Discover&lt;/b&gt; a spell or pick a mystery choice."""
	choose = (SELF, "ULD_209t")
	play = DISCOVER(RandomSpell())
class ULD_209t:
	"""Mystery Choice!
	Add a random spell to your hand.""" 
	play = Give(CONTROLLER, RandomSpell())

class ULD_727:
	"""Body Wrapper		4	4	4	Minion	Epic	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a friendly minion that died this game. Shuffle it into your deck."""
	play = Shuffle(CONTROLLER, Discover(CONTROLLER, RANDOM(FRIENDLY + KILLED)))

class ULD_275:
	"""Bone Wraith		4	2	5	Minion	Common	-	Reborn
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Reborn&lt;/b&gt;"""
	
class ULD_198:
	"""Conjured Mirage		4	3	10	Minion	Rare	-	Taunt
	&lt;b&gt;Taunt&lt;/b&gt;
	At the start of your turn, shuffle this minion into your deck."""
	play = OWN_TURN_BEGIN.on(Shuffle(CONTROLLER, SELF))

class ULD_180:############################################no asleep
	"""Sunstruck Henchman		4	6	5	Minion	Rare	-	-
	At the start of your turn, this has a 50% chance to_fall asleep."""
	pass
	#play = OWN_TURN_BEGIN.on(COINFLIP & asleep(SELF))

class ULD_703:
	"""Desert Obelisk		5	0	5	Minion	Epic	-	-
	[x]If you control 3 of these
	at the end of your turn,
	deal 5 damage to a
	random enemy."""
	powered_up = Count(FRIENDLY_MINIONS + ID("ULD_703"))==3
	play = powered_up & Hit(RANDOM(ENEMY_CHARACTERS),5)

##### 30 #####

class ULD_189:#########need to make doubling max_health
	"""Faceless Lurker		5	3	3	Minion	Common	-	Battlecry
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; Double this minion's Health."""
	play = Buff(SELF, "ULD_189e")
ULD_189e=buff(0,3)
class ULD_702:
	"""Mortuary Machine		5	8	8	Minion	Epic	Mech	Reborn
	After your opponent plays a minion, give it &lt;b&gt;Reborn&lt;/b&gt;."""
	play = Play(OPPONENT,MINION).after(SetTag(SELF,GameTag.REBORN))
class ULD_179:
	"""Phalanx Commander		5	4	5	Minion	Common	-	Taunt
	Your &lt;b&gt;Taunt&lt;/b&gt; minions
	have +2 Attack."""
	play = Buff(FRIENDLY_MINIONS+TAUNT,"ULD_179e")
ULD_179e=buff(2,0)

class ULD_274:
	"""Wasteland Assassin		5	4	2	Minion	Common	-	Reborn
	&lt;b&gt;Stealth&lt;/b&gt;
	&lt;b&gt;Reborn&lt;/b&gt;"""
	pass
class ULD_706:
	"""Blatant Decoy		6	5	5	Minion	Epic	-	Deathrattle
	[x]&lt;b&gt;Deathrattle:&lt;/b&gt; Each player
	summons the lowest Cost
	minion from their hand."""
	deathrattle = Summon(CONTROLLER, RandomMinion(cost= OpAttr(FRIENDLY_HAND+MINION, GameTag.COST, min))), Summon(OPPONENT, RandomMinion(cost= OpAttr(ENEMY_HAND+MINION, GameTag.COST, min)))
class ULD_208:
	"""Khartut Defender		6	3	4	Minion	Rare	-	Deathrattle
	[x]&lt;b&gt;Taunt&lt;/b&gt;, &lt;b&gt;Reborn&lt;/b&gt;
	&lt;b&gt;Deathrattle:&lt;/b&gt; Restore #3
	Health to your hero."""
	play = Heal(FRIENDLY_HERO, 3)
class ULD_178:###################  will consider later 
	"""Siamat		7	6	6	Minion	Legendary	Elemental	Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Gain 2 of &lt;b&gt;Rush&lt;/b&gt;,
	&lt;b&gt;Taunt&lt;/b&gt;, &lt;b&gt;Divine Shield&lt;/b&gt;, or
	&lt;b&gt;Windfury&lt;/b&gt; &lt;i&gt;(your choice).&lt;/i&gt;"""
class ULD_194:
	"""Wasteland Scorpid		7	3	9	Minion	Common	Beast	Poisonous
	&lt;b&gt;Poisonous&lt;/b&gt;"""
	pass
class ULD_215:
	"""Wrapped Golem		7	7	5	Minion	Rare	-	Reborn
	[x]&lt;b&gt;Reborn&lt;/b&gt;
	At the end of your turn,
	summon a 1/1 Scarab
	with &lt;b&gt;Taunt&lt;/b&gt;."""
	events = OWN_TURN_END.on(Summon(CONTROLLER, "ULD_215t"))
class ULD_215t:
	pass
class ULD_177:
	"""Octosari		8	8	8	Minion	Legendary	Beast	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Draw 8 cards."""
	deathrattle = Draw(CONTROLLER) * 8

##### 40 #####

class ULD_190:
	"""Pit Crocolisk		8	5	6	Minion	Common	Beast	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 5 damage."""
	requirements = { PlayReq.REQ_MINION_OR_ENEMY_HERO:0, PlayReq.REQ_TARGET_TO_PLAY:0}
class ULD_183:
	"""Anubisath Warbringer		9	9	6	Minion	Common	-	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Give all minions in your hand +3/+3."""
	deathrattle = Buff(FRIENDLY_HAND + MINION, "ULD_183e")
ULD_183e = buff(3,3)
class ULD_721:
	"""Colossus of the Moon		10	10	10	Minion	Legendary	-	Divine Shield
	&lt;b&gt;Divine Shield&lt;/b&gt;
	&lt;b&gt;Reborn&lt;/b&gt;"""
	pass
class ULD_304:
	"""King Phaoris		10	5	5	Minion	Legendary	-	Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; For each spell
	in your hand, summon a
	random minion of the
	same Cost."""
	def play(self):
		hands = self.controller.hand
		for card in hands:
			if card.type == CardType.SPELL:
				cost = card.cost
				Summon(self.controller, RandomMinion(cost=cost)).trigger(self)
			
class ULD_193:
	"""Living Monument		10	10	10	Minion	Common	-	Taunt
	&lt;b&gt;Taunt&lt;/b&gt;"""
	pass
