from ..utils import *

####### neutral-shadows,,46,,,,,,

class DAL_544:#OK
	"""Potion Vendor,,1,1,1,Minion,Common,-,Battlecry
	<b>Battlecry:</b> Restore #2 Health to all friendly characters."""
	play = Heal(FRIENDLY_CHARACTERS, 2)

class DAL_077:#OK
	"""Toxfin,,1,1,2,Minion,Common,Murloc,Battlecry,Poisonous
	<b>Battlecry:</b> Give a friendly Murloc <b>Poisonous</b>."""
	play = SetTag(RANDOM(FRIENDLY_MINIONS + MURLOC), (GameTag.POISONOUS,))
class DAL_092:#OK
	"""Arcane Servant,,2,2,3,Minion,Common,Elemental,-
	Vanilla"""
	pass
class DAL_735:#OK
	"""Dalaran Librarian,,2,2,3,Minion,Common,-,Battlecry,Silence
	<b>Battlecry:</b> <b>Silence</b>
	adjacent minions."""
	play = Silence(SELF_ADJACENT)
class DAL_400:#OK
	"""EVIL Cable Rat,,2,1,1,Minion,Common,Beast,Battlecry,Lackey
	<b>Battlecry:</b> Add a <b>Lackey</b> to_your hand."""
	entourage = ["DAL_613", "DAL_614", "DAL_615", "DAL_739",\
	   "DAL_741", "DRG_052" ,"ULD_616"]
	play = Give(CONTROLLER, RandomEntourage())
class DAL_743:#OK
	"""Hench-Clan Hogsteed,,2,2,1,Minion,Common,Beast,Deathrattle,Rush
	<b>Rush</b>
	<b>Deathrattle:</b> Summon a 1/1 Murloc."""
	deathrattle = Summon(CONTROLLER, "DAL_743t")
class DAL_743t:
	""" Hench-Clan Squire """
	pass
class DAL_748:#OK
	"""Mana Reservoir,,2,0,6,Minion,Common,Elemental,Spell Damage
	<b>Spell Damage +1</b>"""
	pass
class DAL_089:#OK
	"""Spellbook Binder,,2,3,2,Minion,Common,-,Battlecry,Spell Damage
	<b>Battlecry:</b> If you have <b>Spell Damage</b>, draw a card."""
	play = Find(FRIENDLY_HAND + SPELLPOWER) & Draw(CONTROLLER)
class DAL_086:#OK
	"""Sunreaver Spy,,2,2,3,Minion,Common,-,Battlecry,Secret
	<b>Battlecry:</b> If you control a <b>Secret</b>, gain +1/+1."""
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, "DAL_086e")
DAL_086e=buff(1,1)
class DAL_800:#OK  ##two of five decks was implemented
	""""Zayle, Shadow Cloak",,2,3,2,Minion,Legendary,-,-
	You start the game with one of Zayle's EVIL Decks!"""
	def play(self):
		#tempo-rogue
		tempo_rogue = [
		#2x(0:shadowstep),#2x(0:backstab),#2x(0:Preparation),
		'EX1_144','EX1_144','CS2_072','CS2_072','EX1_145','EX1_145',
		#2x(1:Pharaoh Cat),#2x(1:Bloodsail Flybooter),#1x(2:Bloodmage Thalnos),
		'ULD_186','ULD_186','DRG_035','DRG_035','EX1_012',
		#2x(2:EVIL Cable Rat),#1x(2:sap),#2x(2:Eviscerate),
		'DAL_400','DAL_400','EX1_581','EX1_124','EX1_124',
		#2x(3:SI:7 Agent),#1x(3:Edwin VanCleef),#2x(1:Fan of Knives),
		'EX1_134','EX1_134','EX1_613','EX1_129','EX1_129',
		#2x(3:EVIL Miscreant),#2x(4:Waggle Pick),#1x(4:Grand Lackey Erkh),
		'DAL_415','DAL_415','DAL_720','DAL_720','YOD_035',
		#2x(4:Hench-Clan Burglar),#1x(6:Flik Skyshiv),#1x(6:Heistbaron Togwaggle),
		'DAL_416','DAL_416','DRG_037','DAL_417']
		#silence-priest
		silence_priest=[
		#2x(0)<<Silence>>,2x(0)<<Forbidden Words>>,2x(0)<<Whispers of EVIL>>,
		'EX1_332','EX1_332','DAL_723','DAL_723','DRG_301','DRG_301',
		#2x(1)<<Beaming Sidekick>>,2x(2)<<Ancient Watcher>>,2x(2)<<Neferset Ritualist>>,
		'ULD_191','ULD_191','EX1_045','EX1_045','ULD_196','ULD_196',
		#2x(2)<<Injured Tol'vir>>,2x(2)<<Dalaran Librarian>>,1x(3)<<Madame Lazul>>,
		'ULD_271','ULD_271','DAL_735','DAL_735','DAL_729',
		#2x(3)<<Injured Blademaster>>,2x(3)<<Arcane Watcher>>,2x(4)<<Holy Nova>>,
		'CS2_181','CS2_181','DAL_434','DAL_434','CS1_112','CS1_112',
		#2x(4)<<Hench-Clan Shadequill>>,2x(4)<<Unsleeping Soul>>,2x(4)<<Psychopomp>>,1x(4)<<High Priest Amet>>,
		'DAL_040','DAL_040','DAL_065','DAL_065','ULD_268','ULD_268','ULD_262']
		thisDeck=tempo_rogue
		if self.controller.hero.card_class == CardClass.PRIEST:
			thisDeck = silence_priest
		nn=len(self.controller.deck)
		for n in range(nn):
			self.controller.deck[nn-1-n].discard()
		for id in thisDeck:
			self.controller.card(id, zone=Zone.DECK)
		self.controller.shuffle_deck()
#### 10 ####
class DAL_434:#OK
	"""Arcane Watcher,,3,5,6,Minion,Rare,-,Spell Damage
	Can't attack unless you have <b>Spell Damage</b>."""
	update = -Find(FRIENDLY_MINIONS + SPELLPOWER) & SetTag(SELF, (GameTag.CANT_ATTACK,)) | UnsetTag(SELF, (GameTag.CANT_ATTACK,))
class DAL_744:#OK
	"""Faceless Rager,,3,5,1,Minion,Common,-,Battlecry
	<b>Battlecry:</b> Copy a friendly minion's Health."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = SetMaxHealth(SELF, Attr(TARGET, GameTag.HEALTH))
class DAL_744e:
	pass
class DAL_747:#OK
	"""Flight Master,,3,3,4,Minion,Common,-,Battlecry
	<b>Battlecry:</b> Summon a 2/2 Gryphon for each player."""
	play = Summon(CONTROLLER, "DAL_747t"), Summon(OPPONENT, "DAL_747t")
class DAL_747t:
	""" Gryphon """
	pass
class DAL_090:#OK
	"""Hench-Clan Sneak,,3,3,3,Minion,Common,-,Stealth
	<b>Stealth</b>"""
	pass
class DAL_773:#OK
	"""Magic Carpet,,3,1,6,Minion,Epic,-,Rush
	After you play a 1-Cost minion, give it +1 Attack and <b>Rush</b>."""
	play = Play(CONTROLLER, MINION + (COST == 1)).after(Buff(Play.CARD, "DAL_773e"))
class DAL_773e:
	atk = lambda self, i: i+1
	tags = {GameTag.RUSH:True}
class DAL_081:#OK
	"""Spellward Jeweler,,3,3,4,Minion,Rare,-,Battlecry
	[x]<b>Battlecry:</b> Your hero can't
	be targeted by spells or
	Hero Powers until your
	next turn."""
	play = Buff(FRIENDLY_HERO, "DAL_081e")
class DAL_081e:
	tags = { GameTag.CANT_BE_TARGETED_BY_ABILITIES: True, GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True}
	events = OWN_TURN_BEGIN.on(Destroy(SELF))
class DAL_558:#OK
	"""Archmage Vargoth,,4,2,6,Minion,Legendary,-,-
	[x]At the end of your turn, cast
	a spell you've cast this turn
	<i>(targets are random)</i>."""
	events = OWN_TURN_END.on(DAL558ArchmageVargoth(CONTROLLER))
class DAL_058:#OK
	"""Hecklebot,,4,3,8,Minion,Rare,Mech,Battlecry,Taunt
	<b>Taunt</b>
	<b>Battlecry:</b> Your opponent summons a minion from their deck."""
	play = Summon(OPPONENT, RANDOM(ENEMY_DECK + MINION))
class DAL_087:#OK
	"""Hench-Clan Hag,,4,3,3,Minion,Epic,-,Battlecry
	<b>Battlecry:</b> Summon two 1/1 Amalgams with all minion types."""
	play = Summon(CONTROLLER, "DAL_087t")*2
class DAL_087t:
	"""Amalgam
	x]<i>This is an Elemental, Mech,
	Demon, Murloc, Dragon,
	Beast, Pirate and Totem.</i>"""

class DAL_582:#OK
	"""Portal Keeper,,4,5,2,Minion,Rare,Demon,Battlecry,Rush
	[x]<b>Battlecry:</b> Shuffle 3 Portals
	into your deck. When drawn,
	summon a 2/2 Demon
	with <b>Rush</b>."""
	play = Shuffle(CONTROLLER, "DAL_582t")*3
class DAL_582t:
	""" Felhound Portal 
	<b>Casts When Drawn</b>
	Summon a 2/2 Felhound with <b>Rush</b>."""
	play = Summon(CONTROLLER, "DAL_582t2")
	pass
class DAL_582t2:#OK
	"""Felhound
	"""
	pass

#### 20 ####
class DAL_551:#OK
	"""Proud Defender,,4,2,6,Minion,Common,-,Taunt
	<b>Taunt</b>
	Has +2 Attack while you [x]have no other minions."""
	powered_up = -Find(FRIENDLY_MINIONS - SELF)
	update = powered_up & (-Find(FRIENDLY + ID("ULD_179e")) & Buff(SELF, "ULD_179e")) | Destroy(FRIENDLY + ID("ULD_179e"))
#ULD_179e=buff(2,0)
class DAL_771:#OK
	"""Soldier of Fortune,,4,5,6,Minion,Common,Elemental,-
	Whenever this minion attacks, give your opponent a Coin."""
	events = Attack(SELF, CHARACTER).on(Give(OPPONENT,"GAME_005"))
class DAL_078:#OK
	"""Traveling Healer,,4,3,2,Minion,Common,-,Battlecry,Divine Shield
	[x]<b>Divine Shield</b>
	<b>Battlecry:</b> Restore #3 Health."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Heal(TARGET,3)
class DAL_095:#OK
	"""Violet Spellsword,,4,1,6,Minion,Common,-,Battlecry
	[x]<b>Battlecry:</b> Gain +1 Attack
	for each spell in your hand."""
	play = Buff(SELF, "DAL_095e")*Count(FRIENDLY_HAND + SPELL)
DAL_095e=buff(1,0)
class DAL_548:#OK
	"""Azerite Elemental,,5,2,7,Minion,Epic,Elemental,Spell Damage
	At the start of your turn, gain <b>Spell Damage +2</b>."""
	play = OWN_TURN_BEGIN.on(Buff(SELF,"DAL_548e"))
DAL_548e = buff(spellpower=2)
class DAL_546:#OK
	"""Barista Lynchen,,5,4,5,Minion,Legendary,-,Battlecry
	<b>Battlecry:</b> Add a copy of each of your other <b>Battlecry</b> minions_to_your_hand."""
	play = Give(CONTROLLER, Copy(FRIENDLY_MINIONS + BATTLECRY - SELF))
class DAL_085:#OK
	"""Dalaran Crusader,,5,5,4,Minion,Common,-,Divine Shield
	<b>Divine Shield</b>"""
	pass
class DAL_749:#OK
	"""Recurring Villain,,5,3,6,Minion,Rare,-,Deathrattle
	<b>Deathrattle:</b> If this minion has 4 or more Attack, resummon it."""
	deathrattle = (ATK(SELF)>3) & Summon(CONTROLLER, ExactCopy(SELF))
class DAL_539:#OK
	"""Sunreaver Warmage,,5,4,4,Minion,Rare,-,Battlecry
	<b>Battlecry:</b> If you're holding a spell that costs (5) or more, deal 4 damage."""
	powered_up = Find(FRIENDLY_HAND + SPELL + (COST>4))
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	play = powered_up & Hit(TARGET,4) 
class DAL_566:#OK
	"""Eccentric Scribe,,6,6,4,Minion,Common,-,Deathrattle
	<b>Deathrattle:</b> Summon
	four 1/1 Vengeful Scrolls."""
	deathrattle = Summon(CONTROLLER, "DAL_566t") * 4
class DAL_566t:
	""" Vengeful Scroll """
	pass
#### 30 ####
class DAL_751:#OK
	"""Mad Summoner,,6,4,4,Minion,Rare,Demon,Battlecry
	[x]<b>Battlecry:</b> Fill each player's
	board with 1/1 Imps."""
	def play(self):
		controller = self.controller
		for repeat in range(controller.game.MAX_MINIONS_ON_FIELD - len(controller.field)):
		   Summon(controller, "DAL_751t").trigger(controller)
		opponent = controller.opponent
		for repeat in range(opponent.game.MAX_MINIONS_ON_FIELD - len(opponent.field)):
		   Summon(opponent, "DAL_751t").trigger(opponent)
class DAL_751t:
	""" Imp """
	pass
class DAL_565:#OK
	"""Portal Overfiend,,6,5,6,Minion,Epic,Demon,Battlecry,Rush
	[x]<b>Battlecry:</b> Shuffle 3 Portals
	into your deck. When drawn,
	summon a 2/2 Demon
	with <b>Rush</b>."""
	play = Shuffle(CONTROLLER, "DAL_582t")*3
class DAL_088:#OK
	"""Safeguard,,6,4,5,Minion,Common,Mech,Deathrattle,,Taunt
	[x]<b>Taunt</b>
	<b>Deathrattle:</b> Summon a 0/5
	Vault Safe with <b>Taunt</b>."""
	deathrattle = Summon(CONTROLLER, "DAL_088t2")
class DAL_088t2:
	pass
class DAL_538:#OK
	"""Unseen Saboteur,,6,5,6,Minion,Epic,-,Battlecry
	<b>Battlecry:</b> Your opponent casts a random spell from their hand <i>(targets chosen randomly)</i>."""
	play = CastSpell(RANDOM(ENEMY_HAND + SPELL))
class DAL_096:#OK
	"""Violet Warden,,6,4,7,Minion,Common,-,Spell Damage,Taunt
	<b>Taunt</b>
	<b>Spell Damage +1</b>"""
	pass
class DAL_554:# no way to check!
	"""Chef Nomi,,7,6,6,Minion,Legendary,-,Battlecry
	<b>Battlecry:</b> If your deck is empty, summon six 6/6 Greasefire_Elementals."""
	play = -Find(FRIENDLY_DECK) & Summon(CONTROLLER, "DAL_554t")*6
class DAL_554t:
	pass
class DAL_774:#OK
	"""Exotic Mountseller,,7,5,8,Minion,Rare,-,-
	Whenever you cast a spell, summon a random
	3-Cost Beast."""
	events = OWN_SPELL_PLAY.on(Summon(CONTROLLER, RandomBeast(cost=3)))
class DAL_775:#OK
	"""Tunnel Blaster,,7,3,7,Minion,Rare,-,Deathrattle,Taunt
	[x]<b>Taunt</b>
	<b>Deathrattle:</b> Deal 3 damage
	to all minions."""
	deathrattle = Hit(ALL_MINIONS, 3)
class DAL_550:#OK
	"""Underbelly Ooze,,7,3,5,Minion,Rare,-,-
	After this minion survives damage, summon a copy_of it."""
	events = SELF_DAMAGE.on(Summon(CONTROLLER, Copy(SELF)))
	#play = Find(SELF + EnumSelector(GameTag.DAMAGE)) & Summon(CONTROLLER, Copy(SELF))
class DAL_592:#OK
	"""Batterhead,,8,3,12,Minion,Epic,-,Rush
	<b>Rush</b>. After this attacks and kills a minion, it may_attack again."""
	#play = Attack(SELF, MINION).after(Death(ENEMY_MINIONS).on(attack_again))
	events = Attack(SELF, ALL_MINIONS).after(
		Dead(ALL_MINIONS + Attack.DEFENDER) & ExtraAttack(SELF)
	)
#### 40 ####
class DAL_560:#OK
	"""Heroic Innkeeper,,8,4,4,Minion,Common,-,Battlecry,Taunt
	<b>Taunt.</b> <b>Battlecry:</b> Gain +2/+2 for each other friendly minion."""
	play = Buff(FRIENDLY_MINIONS - SELF, "DAL_560e2")
DAL_560e2 = buff(2,2)
class DAL_752:#OK
	"""Jepetto Joybuzz,,8,6,6,Minion,Legendary,-,Battlecry
	<b>Battlecry:</b> Draw 2 minions from your deck. Set their Attack, Health, and Cost to 1."""
	play = Buff(RANDOM(FRIENDLY_DECK + MINION), "DAL_752e").then(ForceDraw(Buff.TARGET)) * 2
class DAL_752e:
	atk=SET(1)
	max_health=SET(1)
	cost=SET(1)
class DAL_742:#OK
	"""Whirlwind Tempest,,8,6,6,Minion,Epic,Elemental,Mega-Windfury,Windfury
	Your minions with <b>Windfury</b> have <b>Mega-Windfury</b>."""
	# SetTag(TARGET, {GameTag.WINDFURY: 3})
	play = SetTag(FRIENDLY_MINIONS + WINDFURY, {GameTag.WINDFURY: 3})
class DAL_736:## simulator ##OK
	"""Archivist Elysiana,,9,7,7,Minion,Legendary,-,Battlecry,Discover
	<b>Battlecry:</b> <b>Discover</b> 5 cards. Replace your deck with 2_copies of each."""
	def play(self):
		new_deck = []
		for n in range(5):
			choice = RandomCollectible().evaluate(self)
			id = choice[0].id
			new_deck.append(id)
			new_deck.append(id)
		nn=len(self.controller.deck)
		for n in range(nn):
			self.controller.deck[0].discard()
		for id in new_deck:
			self.controller.card(id, zone=Zone.DECK)
		self.controller.shuffle_deck()

class DAL_760:#OK
	"""Burly Shovelfist,,9,9,9,Minion,Common,-,Rush
	<b>Rush</b>"""
	pass
class DAL_553:#OK
	"""Big Bad Archmage,,10,6,6,Minion,Epic,-,-
	At the end of your turn, summon a random
	6-Cost minion."""
	play = OWN_TURN_BEGIN.on(Summon(CONTROLLER, RandomMinion(cost=6)))
