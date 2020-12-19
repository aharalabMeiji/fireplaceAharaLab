from ..utils import *

####### neutral-shadows,,46,,,,,,

class DAL_544:
	"""Potion Vendor,,1,1,1,Minion,Common,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Restore #2 Health to all friendly characters."""
	play = Heal(FRIENDLY_CHARACTERS, 2)
class DAL_077:
	"""Toxfin,,1,1,2,Minion,Common,Murloc,Battlecry,Poisonous
	&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly Murloc &lt;b&gt;Poisonous&lt;/b&gt;."""
	Play = SetTag(RANDOM(FRIENDLY_MINIONS+MURLOC), (GameTag.POISONOUS, ))
class DAL_092:
	"""Arcane Servant,,2,2,3,Minion,Common,Elemental,-
	Vanilla"""
	pass
class DAL_735:
	"""Dalaran Librarian,,2,2,3,Minion,Common,-,Battlecry,Silence
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Silence&lt;/b&gt;
	adjacent minions."""
	update = SetTag(SELF_ADJACENT, (GameTag.SILENCE, ))
class DAL_400:
	"""EVIL Cable Rat,,2,1,1,Minion,Common,Beast,Battlecry,Lackey
	&lt;b&gt;Battlecry:&lt;/b&gt; Add a &lt;b&gt;Lackey&lt;/b&gt; to_your hand."""
	entourage = ["CFM_066", "DAL_613", "DAL_614", "DAL_615", "DAL_739",\
	   "DAL_741", "DRG_052" ,"LOOT_306","ULD_616"]
	play = Give(CONTROLLER, RandomEntourage())
class DAL_743:
	"""Hench-Clan Hogsteed,,2,2,1,Minion,Common,Beast,Deathrattle,Rush
	&lt;b&gt;Rush&lt;/b&gt;
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 1/1 Murloc."""
	deathrattle = Summon(CONTROLLER, "DAL_743t")
class DAL_743t:
	""" Hench-Clan Squire """
	pass
class DAL_748:
	"""Mana Reservoir,,2,0,6,Minion,Common,Elemental,Spell Damage
	&lt;b&gt;Spell Damage +1&lt;/b&gt;"""
	pass
class DAL_089:
	"""Spellbook Binder,,2,3,2,Minion,Common,-,Battlecry,Spell Damage
	&lt;b&gt;Battlecry:&lt;/b&gt; If you have &lt;b&gt;Spell Damage&lt;/b&gt;, draw a card."""
	play = Find(FRIENDLY_HAND + SPELLPOWER) & Draw(CONTROLLER)
class DAL_086:
	"""Sunreaver Spy,,2,2,3,Minion,Common,-,Battlecry,Secret
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a &lt;b&gt;Secret&lt;/b&gt;, gain +1/+1."""
	play = Find(FRIENDLY_CHARACTERS + SPELL) & Buff(SELF, "DAL_086e")
DAL_086e=buff(1,1)
class DAL_800:#############################  pass
	""""Zayle, Shadow Cloak",,2,3,2,Minion,Legendary,-,-
	You start the game with one of Zayle's EVIL Decks!"""

#### 10 ####
class DAL_434:
	"""Arcane Watcher,,3,5,6,Minion,Rare,-,Spell Damage
	Can't attack unless you have &lt;b&gt;Spell Damage&lt;/b&gt;."""
	update = -Find(FRIENDLY_MINIONS + SPELLPOWER) & SetTag(CONTROLLER, {GameTag.CANT_ATTACK:True})
class DAL_744:
	"""Faceless Rager,,3,5,1,Minion,Common,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Copy a friendly minion's Health."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = SetCurrentHealth(SELF, Attr(TARGET, GameTag.HEALTH))
class DAL_744e:
	pass
class DAL_747:
	"""Flight Master,,3,3,4,Minion,Common,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 2/2 Gryphon for each player."""
	play = Summon(CONTROLLER, "DAL_747t"), Summon(OPPONENT, "DAL_747t")
class DAL_747t:
	""" Gryphon """
	pass
class DAL_090:
	"""Hench-Clan Sneak,,3,3,3,Minion,Common,-,Stealth
	&lt;b&gt;Stealth&lt;/b&gt;"""
	pass
class DAL_773:
	"""Magic Carpet,,3,1,6,Minion,Epic,-,Rush
	After you play a 1-Cost minion, give it +1 Attack and &lt;b&gt;Rush&lt;/b&gt;."""
	play = Play(CONTROLLER, RandomMinion(cost=1)).after(Buff(Play.CARD, "DAL_773e"))
class DAL_773e:
	atk=3
	tags={GameTag.RUSH:True}
class DAL_081:
	"""Spellward Jeweler,,3,3,4,Minion,Rare,-,Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Your hero can't
	be targeted by spells or
	Hero Powers until your
	next turn."""
	play = Buff(FRIENDLY_HERO_POWER, "DAL_081e")
class DAL_081e:
	tags = { GameTag.CANT_BE_TARGETED_BY_SPELLS: True, GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True}
	Events = OWN_TURN_BEGIN.on(Destroy(SELF))
class DAL_558:
	"""Archmage Vargoth,,4,2,6,Minion,Legendary,-,-
	[x]At the end of your turn, cast
	a spell you've cast this turn
	&lt;i&gt;(targets are random)&lt;/i&gt;."""
	play = OWN_TURN_END.on(CastSpell(RANDOM(FRIENDLY + SPELL + {GameTag.NUM_CARDS_PLAYED_THIS_TURN:True})))
class DAL_058:
	"""Hecklebot,,4,3,8,Minion,Rare,Mech,Battlecry,Taunt
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; Your opponent summons a minion from their deck."""
	play = Summon(OPPONENT, RANDOM(ENEMY_DECK + MINION))
class DAL_087:
	"""Hench-Clan Hag,,4,3,3,Minion,Epic,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon two 1/1 Amalgams with all minion types."""
	play = Summon(CONTROLLER, "DAL_087t")*2
class DAL_087t:
	"""Amalgam
	x]&lt;i&gt;This is an Elemental, Mech,
	Demon, Murloc, Dragon,
	Beast, Pirate and Totem.&lt;/i&gt;"""

class DAL_582:
	"""Portal Keeper,,4,5,2,Minion,Rare,Demon,Battlecry,Rush
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle 3 Portals
	into your deck. When drawn,
	summon a 2/2 Demon
	with &lt;b&gt;Rush&lt;/b&gt;."""
	play = Shuffle(CONTROLLER, "DAL_582t")
class DAL_582t:### Casts When Drawn
	""" Felhound Portal 
	&lt;b&gt;Casts When Drawn&lt;/b&gt;
	Summon a 2/2 Felhound with &lt;b&gt;Rush&lt;/b&gt;."""
	play = Summon(CONTROLLER, "DAL_582t2")
	pass
class DAL_582t2:
	"""Felhound
	"""
	pass

#### 20 ####
class DAL_551:
	"""Proud Defender,,4,2,6,Minion,Common,-,Taunt
	&lt;b&gt;Taunt&lt;/b&gt;
	Has +2 Attack while you [x]have no other minions."""
	powered_up = -Find(FRIENDLY_MINIONS)
	update = powered_up & Buff(SELF, "DAL_551e")
DAL_551e=buff(2,0)
class DAL_771:
	"""Soldier of Fortune,,4,5,6,Minion,Common,Elemental,-
	Whenever this minion attacks, give your opponent a Coin."""
	events = Attack(SELF, CHARACTER).on(Give(OPPONENT,"GAME_005"))
class DAL_078:
	"""Traveling Healer,,4,3,2,Minion,Common,-,Battlecry,Divine Shield
	[x]&lt;b&gt;Divine Shield&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; Restore #3 Health."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	play = Heal(TARGET,3)
class DAL_095:
	"""Violet Spellsword,,4,1,6,Minion,Common,-,Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Gain +1 Attack
	for each spell in your hand."""
	update = Buff(SELF, "DAL_095e")*Count(FRIENDLY_HAND + SPELL)
DAL_095e=buff(1,0)
class DAL_548:
	"""Azerite Elemental,,5,2,7,Minion,Epic,Elemental,Spell Damage
	At the start of your turn, gain &lt;b&gt;Spell Damage +2&lt;/b&gt;."""
	play = OWN_TURN_BEGIN.on(Buff(SELF,"DAL_548e"))
DAL_548e = buff(spellpower=2)
class DAL_546:
	"""Barista Lynchen,,5,4,5,Minion,Legendary,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Add a copy of each of your other &lt;b&gt;Battlecry&lt;/b&gt; minions_to_your_hand."""
	play = Give(CONTROLLER, Copy(FRIENDLY_MINIONS + BATTLECRY - SELF))
class DAL_085:
	"""Dalaran Crusader,,5,5,4,Minion,Common,-,Divine Shield
	&lt;b&gt;Divine Shield&lt;/b&gt;"""
	pass
class DAL_749:
	"""Recurring Villain,,5,3,6,Minion,Rare,-,Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; If this minion has 4 or more Attack, resummon it."""
	deathrattle = (ATK(SELF)>3) & Summon(CONTROLLER, ExactCopy(SELF))
class DAL_539:
	"""Sunreaver Warmage,,5,4,4,Minion,Rare,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding a spell that costs (5) or more, deal 4 damage."""
	powered_up = Find(FRIENDLY_HAND + SPELL + (COST>=4))
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	play = powered_up & Hit(TARGET,4) 
class DAL_566:
	"""Eccentric Scribe,,6,6,4,Minion,Common,-,Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon
	four 1/1 Vengeful Scrolls."""
	deathrattle = Summon(CONTROLLER, "DAL_566t") * 4
class DAL_566t:
	""" Vengeful Scroll """
	pass
#### 30 ####
class DAL_751:
	"""Mad Summoner,,6,4,4,Minion,Rare,Demon,Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Fill each player's
	board with 1/1 Imps."""
	play = Summon(CONTROLLER, "DAL_751t")*8, Summon(OPPONENT, "DAL_751t")*8
class DAL_751t:
	""" Imp """
	pass
class DAL_565:
	"""Portal Overfiend,,6,5,6,Minion,Epic,Demon,Battlecry,Rush
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle 3 Portals
	into your deck. When drawn,
	summon a 2/2 Demon
	with &lt;b&gt;Rush&lt;/b&gt;."""
	play = Shuffle(CONTROLLER, "DAL_582t")*3
class DAL_088:
	"""Safeguard,,6,4,5,Minion,Common,Mech,Deathrattle,,Taunt
	[x]&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 0/5
	Vault Safe with &lt;b&gt;Taunt&lt;/b&gt;."""

class DAL_538:
	"""Unseen Saboteur,,6,5,6,Minion,Epic,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Your opponent casts a random spell from their hand &lt;i&gt;(targets chosen randomly)&lt;/i&gt;."""
class DAL_096:
	"""Violet Warden,,6,4,7,Minion,Common,-,Spell Damage,Taunt
	&lt;b&gt;Taunt&lt;/b&gt;
&lt;b&gt;Spell Damage +1&lt;/b&gt;"""
class DAL_554:
	"""Chef Nomi,,7,6,6,Minion,Legendary,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If your deck is empty, summon six 6/6 Greasefire_Elementals."""
class DAL_774:
	"""Exotic Mountseller,,7,5,8,Minion,Rare,-,-
	Whenever you cast a spell, summon a random
3-Cost Beast."""
class DAL_775:
	"""Tunnel Blaster,,7,3,7,Minion,Rare,-,Deathrattle,Taunt
	[x]&lt;b&gt;Taunt&lt;/b&gt;
&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 3 damage
to all minions."""
class DAL_550:
	"""Underbelly Ooze,,7,3,5,Minion,Rare,-,-
	After this minion survives damage, summon a copy_of it."""
class DAL_592:
	"""Batterhead,,8,3,12,Minion,Epic,-,Rush
	&lt;b&gt;Rush&lt;/b&gt;. After this attacks and kills a minion, it may_attack again."""
#### 40 ####
class DAL_560:
	"""Heroic Innkeeper,,8,4,4,Minion,Common,-,Battlecry,Taunt
	&lt;b&gt;Taunt.&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Gain +2/+2 for each other friendly minion."""
class DAL_752:
	"""Jepetto Joybuzz,,8,6,6,Minion,Legendary,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Draw 2 minions from your deck. Set their Attack, Health, and Cost to 1."""
class DAL_742:
	"""Whirlwind Tempest,,8,6,6,Minion,Epic,Elemental,Mega-Windfury,Windfury
	Your minions with &lt;b&gt;Windfury&lt;/b&gt; have &lt;b&gt;Mega-Windfury&lt;/b&gt;."""
class DAL_736:
	"""Archivist Elysiana,,9,7,7,Minion,Legendary,-,Battlecry,Discover
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; 5 cards. Replace your deck with 2_copies of each."""
class DAL_760:
	"""Burly Shovelfist,,9,9,9,Minion,Common,-,Rush
	&lt;b&gt;Rush&lt;/b&gt;"""
class DAL_553:
	"""Big Bad Archmage,,10,6,6,Minion,Epic,-,-
	At the end of your turn, summon a random
6-Cost minion."""
