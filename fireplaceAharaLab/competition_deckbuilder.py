from hearthstone.enums import CardClass
from fireplace.debug_utilities import parseDeck
from agent_Standard import StandardVectorAgent
from utils import play_one_game

### deckCat ###
class deckCatCard:
	def __init__(self):
		self.id=''
		self.e_name="name"
		self.card_class='CardClass.NEUTRAL'
		self.rarity='Rarity.FREE'
		self.cost=1
		self.atk=0
		self.max_health=0
		self.description=""
		self.max_number=2
		pass

class deckCatBlock:
	def __init__(self):
		self.cardId=''
		self.card=None
		self.pickupStep=-1
		self.active=True
		self.number=2
		pass



class CompetitionDeckbuilding:


######### entries (samples) ############



	



	def deckCatMain(repeat=0):
		sourceClass=CardClass.DRUID
		sourceClassName='DRUID'
		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=sourceClass)

		deckcatDruid0={"name":"deckcatDruid0","deck":[## Wins: 819 / 900 = 0.910000 (4)
			"VAN_EX1_509","VAN_EX1_509",#(0)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
			"VAN_CS2_179","VAN_CS2_179",#(0)VAN_CS2_179,Sen'jin Shieldmasta,Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
			"VAN_NEW1_019","VAN_NEW1_019",#(0)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
			"VAN_EX1_048","VAN_EX1_048",#(0)VAN_EX1_048,Spellbreaker,Neutral,Rarity.COMMON,4,4,3,<b>Battlecry:</b> <b>Silence</b> a_minion.
			"VAN_CS2_009","VAN_CS2_009",#(1)VAN_CS2_009,Mark of the Wild,Druid,Rarity.FREE,2,0,0,Give a minion <b>Taunt</b> and +2/+2.<i>(+2 Attack/+2 Health)</i>
			"VAN_EX1_011","VAN_EX1_011",#(1)VAN_EX1_011,Voodoo Doctor,Neutral,Rarity.FREE,1,2,1,<b>Battlecry:</b> Restore #2_Health.
			"VAN_EX1_062",#(1)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
			"VAN_EX1_405","VAN_EX1_405",#(1)VAN_EX1_405,Shieldbearer,Neutral,Rarity.COMMON,1,0,4,<b>Taunt</b>
			"VAN_NEW1_029",#(2)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
			"VAN_CS2_203","VAN_CS2_203",#(2)VAN_CS2_203,Ironbeak Owl,Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
			"VAN_CS2_012","VAN_CS2_012",#(2)VAN_CS2_012,Swipe,Druid,Rarity.FREE,4,0,0,Deal $4 damage to an enemy and $1 damage to all other enemies.
			"VAN_CS2_125","VAN_CS2_125",#(2)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
			"VAN_CS2_142","VAN_CS2_142",#(3)VAN_CS2_142,Kobold Geomancer,Neutral,Rarity.FREE,2,2,2,<b>Spell Damage +1</b>
			"VAN_EX1_029","VAN_EX1_029",#(3)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
			"VAN_CS2_141","VAN_CS2_141",#(3)VAN_CS2_141,Ironforge Rifleman,Neutral,Rarity.FREE,3,2,2,<b>Battlecry:</b> Deal 1 damage.
			"VAN_EX1_066","VAN_EX1_066",#(3)VAN_EX1_066,Acidic Swamp Ooze,Neutral,Rarity.FREE,2,3,2,<b>Battlecry:</b> Destroy your opponent's weapon.
			],"class":CardClass.DRUID}
		#deckCatHunter ## this is a sample
		deckcatHunter0={"name":"deckCatHunter0",### 908/1000
			"deck":[
			"VAN_CS2_162","VAN_CS2_162",#VAN_CS2_162#,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
			"VAN_EX1_032","VAN_EX1_032",#VAN_EX1_032#,Sunwalker, Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
			"VAN_EX1_050","VAN_EX1_050",#VAN_EX1_050#,Coldlight Oracle, Neutral,Rarity.RARE,3,2,2,<b>Battlecry:</b> Each player draws 2 cards.
			"VAN_CS2_226","VAN_CS2_226",#VAN_CS2_226#,Frostwolf Warlord, Neutral,Rarity.FREE,5,4,4,<b>Battlecry:</b> Gain +1/+1 for each other friendly minion on the battlefield.
			"VAN_DS1_184","VAN_DS1_184",#VAN_DS1_184#,Tracking, Hunter,Rarity.FREE,1,0,0,Look at the top 3 cards of your deck. Draw one and discard the others.
			"VAN_EX1_533","VAN_EX1_533",#VAN_EX1_533,Misdirection, Hunter,Rarity.RARE,2,0,0,<b>Secret:</b> When an enemy attacks your hero instead it attacks another random character.
			"VAN_EX1_537","VAN_EX1_537",#VAN_EX1_537,Explosive Shot, Hunter,Rarity.RARE,5,0,0,Deal $5 damage to a minion and $2 damage to adjacent ones.
			"VAN_CS2_187","VAN_CS2_187",#VAN_CS2_187,Booty Bay Bodyguard, Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
			"VAN_CS2_179","VAN_CS2_179",#VAN_CS2_179,Sen'jin Shieldmasta, Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
			"VAN_CS2_125","VAN_CS2_125",#VAN_CS2_125,Ironfur Grizzly, Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
			"VAN_CS2_203","VAN_CS2_203",#VAN_CS2_203,Ironbeak Owl, Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
			"VAN_EX1_049","VAN_EX1_049",#VAN_EX1_049,Youthful Brewmaster, Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
			"VAN_EX1_539","VAN_EX1_539",#VAN_EX1_539,Kill Command, Hunter,Rarity.FREE,3,0,0,Deal $3 damage. If you control a Beast deal$5 damage instead.
			"VAN_EX1_080","VAN_EX1_080",#VAN_EX1_080,Secretkeeper, Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
			"VAN_CS2_181","VAN_CS2_181",#VAN_CS2_181,Injured Blademaster,Neutral,Rarity.RARE,3,4,7,<b>Battlecry:</b> Deal 4 damage to HIMSELF.
			],"class":CardClass.HUNTER }
		deckcatMage0={"name":"deckcatMage0","deck":[## Wins: 739 / 900 = 0.821111 (3)
			"VAN_EX1_066","VAN_EX1_066",#(0)VAN_EX1_066,Acidic Swamp Ooze,Neutral,Rarity.FREE,2,3,2,<b>Battlecry:</b> Destroy your opponent's weapon.
			"VAN_EX1_507","VAN_EX1_507",#(0)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
			"VAN_EX1_062",#(0)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
			"VAN_NEW1_012","VAN_NEW1_012",#(0)VAN_NEW1_012,Mana Wyrm,Mage,Rarity.COMMON,1,1,3,Whenever you cast a spell gain +1 Attack.
			"VAN_NEW1_025","VAN_NEW1_025",#(1)VAN_NEW1_025,Bloodsail Corsair,Neutral,Rarity.RARE,1,1,2,[x]<b>Battlecry:</b> Remove1 Durability from youropponent's weapon.
			"VAN_EX1_045","VAN_EX1_045",#(1)VAN_EX1_045,Ancient Watcher,Neutral,Rarity.RARE,2,4,5,Can't attack.
			"VAN_EX1_015","VAN_EX1_015",#(1)VAN_EX1_015,Novice Engineer,Neutral,Rarity.FREE,2,1,1,<b>Battlecry:</b> Draw a card.
			"VAN_NEW1_027","VAN_NEW1_027",#(1)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
			"VAN_EX1_277","VAN_EX1_277",#(2)VAN_EX1_277,Arcane Missiles,Mage,Rarity.FREE,1,0,0,Deal $3 damage randomly split among all enemy characters.
			"VAN_EX1_080","VAN_EX1_080",#(2)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
			"VAN_EX1_029","VAN_EX1_029",#(2)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
			"VAN_EX1_556","VAN_EX1_556",#(2)VAN_EX1_556,Harvest Golem,Neutral,Rarity.COMMON,3,2,3,<b>Deathrattle:</b> Summon a 2/1 Damaged Golem.
			"VAN_CS2_189","VAN_CS2_189",#(3)VAN_CS2_189,Elven Archer,Neutral,Rarity.FREE,1,1,1,<b>Battlecry:</b> Deal 1 damage.
			"VAN_NEW1_017","VAN_NEW1_017",#(3)VAN_NEW1_017,Hungry Crab,Neutral,Rarity.EPIC,1,1,2,<b>Battlecry:</b> Destroy a Murloc and gain +2/+2.
			"VAN_EX1_275","VAN_EX1_275",#(3)VAN_EX1_275,Cone of Cold,Mage,Rarity.COMMON,4,0,0,<b>Freeze</b> a minion and the minions next to it and deal $1 damage to them.
			"VAN_CS2_031",#(3)VAN_CS2_031,Ice Lance,Mage,Rarity.COMMON,1,0,0,<b>Freeze</b> a character. If it was already <b>Frozen</b> deal $4 damage instead.
			], "class":CardClass.MAGE}
		deckcatPaladin0={"name":"deckcatPaladin0","deck":[## Wins: 640 / 900 = 0.711111 (3)
			"VAN_CS2_187","VAN_CS2_187",#(0)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
			"VAN_CS2_092","VAN_CS2_092",#(0)VAN_CS2_092,Blessing of Kings,Paladin,Rarity.FREE,4,0,0,Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i>
			"VAN_CS2_097","VAN_CS2_097",#(0)VAN_CS2_097,Truesilver Champion,Paladin,Rarity.FREE,4,4,0,Whenever your hero attacks restore #2_Health to it.
			"VAN_EX1_132","VAN_EX1_132",#(0)VAN_EX1_132,Eye for an Eye,Paladin,Rarity.COMMON,1,0,0,<b>Secret:</b> When your hero takes damage deal_that much damage to the enemy hero.
			"VAN_EX1_032","VAN_EX1_032",#(1)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
			"VAN_EX1_365","VAN_EX1_365",#(1)VAN_EX1_365,Holy Wrath,Paladin,Rarity.RARE,5,0,0,Draw a card and deal_damage equal to_its Cost.
			"VAN_NEW1_023","VAN_NEW1_023",#(1)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
			"VAN_NEW1_027","VAN_NEW1_027",#(1)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
			"VAN_EX1_507","VAN_EX1_507",#(2)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
			"VAN_CS2_146","VAN_CS2_146",#(2)VAN_CS2_146,Southsea Deckhand,Neutral,Rarity.COMMON,1,2,1,Has <b>Charge</b> while you have a weapon equipped.
			"VAN_EX1_616","VAN_EX1_616",#(2)VAN_EX1_616,Mana Wraith,Neutral,Rarity.RARE,2,2,2,ALL minions cost (1) more.
			"VAN_EX1_049","VAN_EX1_049",#(2)VAN_EX1_049,Youthful Brewmaster,Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
			"VAN_NEW1_018","VAN_NEW1_018",#(3)VAN_NEW1_018,Bloodsail Raider,Neutral,Rarity.COMMON,2,2,3,<b>Battlecry:</b> Gain Attack equal to the Attackof your weapon.
			"VAN_NEW1_026","VAN_NEW1_026",#(3)VAN_NEW1_026,Violet Teacher,Neutral,Rarity.RARE,4,3,5,Whenever you cast a spell summon a 1/1 Violet Apprentice.
			"VAN_EX1_025","VAN_EX1_025",#(3)VAN_EX1_025,Dragonling Mechanic,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Summon a 2/1 Mechanical Dragonling.
			"VAN_EX1_170","VAN_EX1_170",#(3)VAN_EX1_170,Emperor Cobra,Neutral,Rarity.RARE,3,2,3,Destroy any minion damaged by this minion.
			], "class":CardClass.PALADIN}
		deckcatPriest0={"name":"deckcatPriest0","deck":[## Wins: 681 / 900 = 0.756667 (4)
			"VAN_CS2_117","VAN_CS2_117",#(0)VAN_CS2_117,Earthen Ring Farseer,Neutral,Rarity.COMMON,3,3,3,<b>Battlecry:</b> Restore #3_Health.
			"VAN_CS2_231","VAN_CS2_231",#(0)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
			"VAN_EX1_062",#(0)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
			"VAN_EX1_032","VAN_EX1_032",#(0)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
			"VAN_CS2_127","VAN_CS2_127",#(1)VAN_CS2_127,Silverback Patriarch,Neutral,Rarity.FREE,3,1,4,<b>Taunt</b>
			"VAN_EX1_593","VAN_EX1_593",#(1)VAN_EX1_593,Nightblade,Neutral,Rarity.FREE,5,4,4,<b>Battlecry: </b>Deal 3 damage to the enemy hero.
			"VAN_tt_004","VAN_tt_004",#(1)VAN_tt_004,Flesheating Ghoul,Neutral,Rarity.COMMON,3,2,3,Whenever a minion dies gain +1 Attack.
			"VAN_CS1_042","VAN_CS1_042",#(1)VAN_CS1_042,Goldshire Footman,Neutral,Rarity.FREE,1,1,2,<b>Taunt</b>
			"VAN_EX1_046","VAN_EX1_046",#(2)VAN_EX1_046,Dark Iron Dwarf,Neutral,Rarity.COMMON,4,4,4,<b>Battlecry:</b> Give a minion +2_Attack this turn.
			"VAN_EX1_011","VAN_EX1_011",#(2)VAN_EX1_011,Voodoo Doctor,Neutral,Rarity.FREE,1,2,1,<b>Battlecry:</b> Restore #2_Health.
			"VAN_EX1_028","VAN_EX1_028",#(2)VAN_EX1_028,Stranglethorn Tiger,Neutral,Rarity.COMMON,5,5,5,<b>Stealth</b>
			"VAN_CS2_146","VAN_CS2_146",#(2)VAN_CS2_146,Southsea Deckhand,Neutral,Rarity.COMMON,1,2,1,Has <b>Charge</b> while you have a weapon equipped.
			"VAN_EX1_170","VAN_EX1_170",#(3)VAN_EX1_170,Emperor Cobra,Neutral,Rarity.RARE,3,2,3,Destroy any minion damaged by this minion.
			"VAN_EX1_048","VAN_EX1_048",#(3)VAN_EX1_048,Spellbreaker,Neutral,Rarity.COMMON,4,4,3,<b>Battlecry:</b> <b>Silence</b> a_minion.
			"VAN_EX1_116",#(3)VAN_EX1_116,Leeroy Jenkins,Neutral,Rarity.LEGENDARY,4,6,2,<b>Charge</b>. <b>Battlecry:</b> Summon two 1/1 Whelps for your opponent.
			"VAN_EX1_102","VAN_EX1_102",#(3)VAN_EX1_102,Demolisher,Neutral,Rarity.RARE,3,1,4,At the start of your turn deal 2 damage to a random enemy.
			], "class":CardClass.PRIEST}
		deckcatRogue0={"name":"deckcatRogue0","deck":[##Wins: 765 / 900 = 0.850000 (5)
			## "VAN_NEW1_005","VAN_NEW1_005",#(0)VAN_NEW1_005,Kidnapper,Rogue,Rarity.EPIC,6,5,3,<b>Combo:</b> Return a minion to_its owner's hand.
			"VAN_CS2_080","VAN_CS2_080",#(1)VAN_CS2_080,Assassin's Blade,Rogue,Rarity.FREE,5,3,0,
			"VAN_EX1_097","VAN_EX1_097",#(1)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
			## "VAN_PRO_001",#(1)VAN_PRO_001,Elite Tauren Chieftain,Neutral,Rarity.LEGENDARY,5,5,5,<b>Battlecry:</b> Give both players the power to ROCK! (with a Power Chord card)
			## "VAN_CS2_077","VAN_CS2_077",#(2)VAN_CS2_077,Sprint,Rogue,Rarity.FREE,7,0,0,Draw 4 cards.
			"VAN_EX1_507","VAN_EX1_507",#(2)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
			"VAN_NEW1_027","VAN_NEW1_027",#(2)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
			## "VAN_EX1_561",#(2)VAN_EX1_561,Alexstrasza,Neutral,Rarity.LEGENDARY,9,8,8,<b>Battlecry:</b> Set a hero's remaining Health to 15.
			"VAN_EX1_522","VAN_EX1_522",#(3)VAN_EX1_522,Patient Assassin,Rogue,Rarity.EPIC,2,1,1,<b>Stealth</b>. Destroy any minion damaged by this minion.
			"VAN_CS2_121","VAN_CS2_121",#(3)VAN_CS2_121,Frostwolf Grunt,Neutral,Rarity.FREE,2,2,2,<b>Taunt</b>
			"VAN_CS2_073","VAN_CS2_073",#(3)VAN_CS2_073,Cold Blood,Rogue,Rarity.COMMON,1,0,0,Give a minion +2 Attack. <b>Combo:</b> +4 Attack instead.
			"VAN_NEW1_029",#(3)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
			"VAN_CS2_173","VAN_CS2_173",#(4)VAN_CS2_173,Bluegill Warrior,Neutral,Rarity.FREE,2,2,1,<b>Charge</b>
			"VAN_EX1_124","VAN_EX1_124",#(4)VAN_EX1_124,Eviscerate,Rogue,Rarity.COMMON,2,0,0,Deal $2 damage. <b>Combo:</b> Deal $4 damage instead.
			"VAN_NEW1_022","VAN_NEW1_022",#(4)VAN_NEW1_022,Dread Corsair,Neutral,Rarity.COMMON,4,3,3,<b>Taunt</b>Costs (1) less per Attack of_your weapon.
			"VAN_EX1_021","VAN_EX1_021",#(4)VAN_EX1_021,Thrallmar Farseer,Neutral,Rarity.COMMON,3,2,3,<b>Windfury</b>
			"VAN_EX1_029","VAN_EX1_029",#(5)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
			"VAN_EX1_080","VAN_EX1_080",#(5)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
			"VAN_EX1_412","VAN_EX1_412",#(5)VAN_EX1_412,Raging Worgen,Neutral,Rarity.COMMON,3,3,3,<b>Enrage:</b> <b>Windfury</b> and +1 Attack
			"VAN_EX1_019",#(5)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
			], "class":CardClass.ROGUE}
		deckcatShaman0={"name":"deckcatShaman0","deck":[## Wins: 462 / 540 = 0.855556 (7)
			## "VAN_EX1_561",#(0)VAN_EX1_561,Alexstrasza,Neutral,Rarity.LEGENDARY,9,8,8,<b>Battlecry:</b> Set a hero's remaining Health to 15.
			## "VAN_NEW1_030",#(1)VAN_NEW1_030,Deathwing,Neutral,Rarity.LEGENDARY,10,12,12,<b>Battlecry:</b> Destroy all other minions and discard your_hand.
			## "VAN_EX1_560",#(2)VAN_EX1_560,Nozdormu,Neutral,Rarity.LEGENDARY,9,8,8,Players only have 15 seconds to take their_turns.
			"VAN_EX1_509","VAN_EX1_509",#(3)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
			"VAN_CS2_179","VAN_CS2_179",#(3)VAN_CS2_179,Sen'jin Shieldmasta,Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
			"VAN_EX1_244","VAN_EX1_244",#(3)VAN_EX1_244,Totemic Might,Shaman,Rarity.FREE,0,0,0,Give your Totems +2_Health.
			## "VAN_DS1_055","VAN_DS1_055",#(3)VAN_DS1_055,Darkscale Healer,Neutral,Rarity.FREE,5,4,5,<b>Battlecry:</b> Restore #2 Health to all friendly characters.
			"VAN_EX1_097","VAN_EX1_097",#(4)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
			"VAN_CS2_162","VAN_CS2_162",#(4)VAN_CS2_162,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
			"VAN_CS2_187","VAN_CS2_187",#(4)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
			"VAN_CS2_196","VAN_CS2_196",#(4)VAN_CS2_196,Razorfen Hunter,Neutral,Rarity.FREE,3,2,3,<b>Battlecry:</b> Summon a 1/1_Boar.
			"VAN_EX1_250","VAN_EX1_250",#(5)VAN_EX1_250,Earth Elemental,Shaman,Rarity.EPIC,5,7,8,<b>Taunt</b>. <b><b>Overload</b>:</b> (3)
			"VAN_EX1_616","VAN_EX1_616",#(5)VAN_EX1_616,Mana Wraith,Neutral,Rarity.RARE,2,2,2,ALL minions cost (1) more.
			"VAN_CS2_203","VAN_CS2_203",#(5)VAN_CS2_203,Ironbeak Owl,Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
			"VAN_NEW1_021","VAN_NEW1_021",#(5)VAN_NEW1_021,Doomsayer,Neutral,Rarity.EPIC,2,0,7,At the start of your turn destroy ALL minions.
			"VAN_EX1_009","VAN_EX1_009",#(6)VAN_EX1_009,Angry Chicken,Neutral,Rarity.RARE,1,1,1,<b>Enrage:</b> +5 Attack.
			"VAN_CS2_117","VAN_CS2_117",#(6)VAN_CS2_117,Earthen Ring Farseer,Neutral,Rarity.COMMON,3,3,3,<b>Battlecry:</b> Restore #3_Health.
			"VAN_tt_004","VAN_tt_004",#(6)VAN_tt_004,Flesheating Ghoul,Neutral,Rarity.COMMON,3,2,3,Whenever a minion dies gain +1 Attack.
			"VAN_EX1_005","VAN_EX1_005",#(6)VAN_EX1_005,Big Game Hunter,Neutral,Rarity.EPIC,3,4,2,<b>Battlecry:</b> Destroy a minion with 7 or more Attack.
			], "class":CardClass.SHAMAN}
		deckcatWarlock0={"name":"deckcatWarlock0","deck":[## Wins: 469 / 540 = 0.868519 (5)
			"VAN_EX1_309","VAN_EX1_309",#(0)VAN_EX1_309,Siphon Soul,Warlock,Rarity.RARE,6,0,0,Destroy a minion. Restore #3 Health to_your hero.
			"VAN_EX1_301","VAN_EX1_301",#(1)VAN_EX1_301,Felguard,Warlock,Rarity.RARE,3,3,5,<b>Taunt</b><b>Battlecry:</b> Destroy one of your Mana Crystals.
			## "VAN_PRO_001",#(1)VAN_PRO_001,Elite Tauren Chieftain,Neutral,Rarity.LEGENDARY,5,5,5,<b>Battlecry:</b> Give both players the power to ROCK! (with a Power Chord card)
			"VAN_EX1_093","VAN_EX1_093",#(2)VAN_EX1_093,Defender of Argus,Neutral,Rarity.RARE,4,2,3,<b>Battlecry:</b> Give adjacent minions +1/+1 and <b>Taunt</b>.
			## "VAN_NEW1_029",#(2)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
			"VAN_NEW1_019","VAN_NEW1_019",#(2)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
			"VAN_CS2_231","VAN_CS2_231",#(2)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
			"VAN_EX1_319","VAN_EX1_319",#(3)VAN_EX1_319,Flame Imp,Warlock,Rarity.COMMON,1,3,2,<b>Battlecry:</b> Deal 3 damage to your hero.
			"VAN_EX1_032","VAN_EX1_032",#(3)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
			"VAN_EX1_390","VAN_EX1_390",#(3)VAN_EX1_390,Tauren Warrior,Neutral,Rarity.COMMON,3,2,3,<b>Taunt</b>. <b>Enrage:</b> +3 Attack
			"VAN_EX1_048","VAN_EX1_048",#(3)VAN_EX1_048,Spellbreaker,Neutral,Rarity.COMMON,4,4,3,<b>Battlecry:</b> <b>Silence</b> a_minion.
			"VAN_EX1_306","VAN_EX1_306",#(4)VAN_EX1_306,Felstalker,Warlock,Rarity.FREE,2,4,3,<b>Battlecry:</b> Discard a random card.
			"VAN_EX1_019","VAN_EX1_019",#(4)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
			"VAN_NEW1_023","VAN_NEW1_023",#(4)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
			"VAN_CS2_125","VAN_CS2_125",#(4)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
			"VAN_NEW1_025","VAN_NEW1_025",#(5)VAN_NEW1_025,Bloodsail Corsair,Neutral,Rarity.RARE,1,1,2,[x]<b>Battlecry:</b> Remove1 Durability from youropponent's weapon.
			"VAN_EX1_616","VAN_EX1_616",#(5)VAN_EX1_616,Mana Wraith,Neutral,Rarity.RARE,2,2,2,ALL minions cost (1) more.
			"VAN_NEW1_026","VAN_NEW1_026",#(5)VAN_NEW1_026,Violet Teacher,Neutral,Rarity.RARE,4,3,5,Whenever you cast a spell summon a 1/1 Violet Apprentice.
			], "class":CardClass.WARLOCK}
		deckcatWarrior0={"name":"deckcatWarrior0","deck":[## Wins: 459 / 540 = 0.850000 (4)
			## "VAN_EX1_284","VAN_EX1_284",#(0)VAN_EX1_284,Azure Drake,Neutral,Rarity.RARE,5,4,4,<b>Spell Damage +1</b><b>Battlecry:</b> Draw a card.
			"VAN_EX1_050","VAN_EX1_050",#(0)VAN_EX1_050,Coldlight Oracle,Neutral,Rarity.RARE,3,2,2,<b>Battlecry:</b> Each player draws 2 cards.
			## "VAN_EX1_583","VAN_EX1_583",#(0)VAN_EX1_583,Priestess of Elune,Neutral,Rarity.COMMON,6,5,4,<b>Battlecry:</b> Restore #4 Health to your hero.
			## "VAN_NEW1_041","VAN_NEW1_041",#(0)VAN_NEW1_041,Stampeding Kodo,Neutral,Rarity.RARE,5,3,5,<b>Battlecry:</b> Destroy a random enemy minion with 2 or less Attack.
			"VAN_EX1_004","VAN_EX1_004",#(1)VAN_EX1_004,Young Priestess,Neutral,Rarity.RARE,1,2,1,At the end of your turn give another random friendly minion +1 Health.
			"VAN_CS2_187","VAN_CS2_187",#(1)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
			"VAN_EX1_564","VAN_EX1_564",#(1)VAN_EX1_564,Faceless Manipulator,Neutral,Rarity.EPIC,5,3,3,<b>Battlecry:</b> Choose a minion and become a copy of it.
			"VAN_CS2_114","VAN_CS2_114",#(1)VAN_CS2_114,Cleave,Warrior,Rarity.FREE,2,0,0,[x]Deal $2 damage totwo random enemyminions.
			"VAN_EX1_062",#(2)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
			"VAN_EX1_509","VAN_EX1_509",#(2)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
			"VAN_EX1_059","VAN_EX1_059",#(2)VAN_EX1_059,Crazed Alchemist,Neutral,Rarity.RARE,2,2,2,<b>Battlecry:</b> Swap the Attack and Health of a minion.
			"VAN_EX1_590","VAN_EX1_590",#(2)VAN_EX1_590,Blood Knight,Neutral,Rarity.EPIC,3,3,3,<b>Battlecry:</b> All minions lose <b>Divine Shield</b>. Gain +3/+3 for each Shield lost.
			"VAN_EX1_010","VAN_EX1_010",#(3)VAN_EX1_010,Worgen Infiltrator,Neutral,Rarity.COMMON,1,2,1,<b>Stealth</b>
			"VAN_EX1_507","VAN_EX1_507",#(3)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
			"VAN_NEW1_016","VAN_NEW1_016",#(3)VAN_NEW1_016,Captain's Parrot,Neutral,Rarity.EPIC,2,1,1,<b>Battlecry:</b> Draw a Pirate from your deck.
			"VAN_EX1_606","VAN_EX1_606",#(3)VAN_EX1_606,Shield Block,Warrior,Rarity.FREE,3,0,0,Gain 5 Armor.Draw a card.
			"VAN_CS1_042","VAN_CS1_042",#(4)VAN_CS1_042,Goldshire Footman,Neutral,Rarity.FREE,1,1,2,<b>Taunt</b>
			"VAN_EX1_019","VAN_EX1_019",#(4)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
			"VAN_CS2_104",#(4)VAN_CS2_104,Rampage,Warrior,Rarity.COMMON,2,0,0,Give a damaged minion +3/+3.
			], "class":CardClass.WARRIOR}

		DruidRandom={"name":"DruidRandom", "deck":[], "class":CardClass.DRUID}
		HunterRandom={"name":"HunterRandom", "deck":[], "class":CardClass.HUNTER}
		MageRandom={"name":"MageRandom", "deck":[], "class":CardClass.MAGE}
		PaladinRandom={"name":"PaladinRandom", "deck":[], "class":CardClass.PALADIN}
		PriestRandom={"name":"PriestRandom", "deck":[], "class":CardClass.PRIEST}
		RogueRandom={"name":"RogueRandom", "deck":[], "class":CardClass.ROGUE}
		ShamanRandom={"name":"ShamanRandom", "deck":[], "class":CardClass.SHAMAN}
		WarlockRandom={"name":"WarlockRandom", "deck":[], "class":CardClass.WARLOCK}
		WarriorRandom={"name":"WarriorRandom", "deck":[], "class":CardClass.WARRIOR}

		targetClasses=[deckcatDruid0, deckcatHunter0, deckcatMage0, deckcatPaladin0, deckcatPriest0, deckcatRogue0, deckcatShaman0, deckcatWarlock0, deckcatWarrior0]
		#targetClasses=[DruidRandom, HunterRandom, MageRandom, PaladinRandom, PriestRandom, RogueRandom, ShamanRandom, WarlockRandom, WarriorRandom]
		#targetClasses=[CardClass.SHAMAN]
		targetClassName='N100k4ALL-2-%d'%(repeat)
		lenTarget=len(targetClasses)
		poolfilename="classic_pool_en.csv"
		matchN=100
		myDeck=[
			'VAN_CS2_231','VAN_CS2_231',
			'VAN_EX1_509','VAN_EX1_509',
			'VAN_CS2_146','VAN_CS2_146',
			'VAN_EX1_506','VAN_EX1_506',
			]
		myDeckTexts = []
		myDeckBlocks = []
		myDeckWinrate = []
		mydict ={}
		mydict['XXXX']=0
		pf = open(poolfilename, 'r')
		datalist = pf.readlines()
		pf.close()
		poolcardlist = []
		for line in datalist:
			terms = line.split(',')
			newcard = deckCatCard()
			newcard.id=terms[0]
			newcard.e_name=terms[1]
			newcard.card_class=terms[2]
			newcard.rarity=terms[3]
			newcard.cost=int(terms[4])
			newcard.atk=int(terms[5])
			newcard.max_health=int(terms[6])
			newcard.description=terms[7]
			if newcard.rarity=="Rarity.LEGENDARY":
				newcard.max_number=1
			poolcardlist.append(newcard)
			pass

		stepcount=0

		processend=False

		myDeckTexts.append("\t\t## deckCat-%s-%s"%(sourceClassName,targetClassName))
		for stepcount in range(20):
			cardsfilename="deckCatblockdic-%s-%s_%d.csv"%(sourceClassName,targetClassName,stepcount)
			deckfilename="deckCat-%s-%s_%d.txt"%(sourceClassName,targetClassName,stepcount)
			win_count=0
			mydict ={}
			mydict['XXXX']=0		
			for myCardClass in targetClasses:
				Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
					,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
					,myClass=myCardClass["class"],
					mulliganStrategy=StandardVectorAgent.StandardMulligan)
				for repeat in range(matchN):
					winner , mydict_thisplay = play_one_game(Vector1, Vector2, deck1=myDeck, deck2=myCardClass["deck"], debugLog=True)
					if winner=='Vector1':
						win_count += 1
						for key in mydict_thisplay:
							if key in mydict.keys():
								mydict[key] = mydict[key]+1
							else:
								mydict[key] = 1
					else:
						for key in mydict_thisplay:
							if key in mydict.keys():
								mydict[key] = mydict[key]-1
							else:
								mydict[key] = -1
			myDeckWinrate.append([win_count, matchN*lenTarget, stepcount])
		
			if processend==True:
				myDeckTexts=[]		
				for winrate in myDeckWinrate:
					myDeckTexts.append("\t\t## Wins: %d / %d = %f (%d)\n"%(winrate[0], winrate[1], 1.0*winrate[0]/winrate[1], winrate[2]))
				for block in myDeckBlocks:
					blockText="\t\t"
					if block.active==False:
						blockText+="## "
					if block.number==2:
						blockText+='"%s","%s",'%(block.cardId,block.cardId)
					else:
						blockText+='"%s",'%(block.cardId)
					blockText+=('#(%d)%s,%s,%s,%s,%d,%d,%d,%s'%(
							block.pickupStep,
							block.card.id,
							block.card.e_name,
							block.card.card_class,
							block.card.rarity,
							block.card.cost,
							block.card.atk,
							block.card.max_health,
							block.card.description
							))
					myDeckTexts.append(blockText)
				df = open(deckfilename, 'w')
				for text in myDeckTexts:
					df.write("%s"%(text))
				df.close()
				return


			blockdic = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
			cf = open(cardsfilename, 'w')
			for key,value in blockdic:
				cf.write(key+','+str(value)+"\n")
			cf.close()

			for block in myDeckBlocks:
				block.active=False
			blocklinecount=0
			blockcardcount=0
			for key, value in blockdic:
				if blocklinecount>=4 or value<-30:
					break
				thisblock = [block for block in myDeckBlocks if block.cardId==key] 
				if len(thisblock)>0:
					thisblock[0].active=True
					blockcardcount += thisblock[0].number
					if blockcardcount>= 30:
						print("End point 2")
						processend=True
						break
				else:
					thisblockcard=[card for card in poolcardlist if card.id==key]
					if len(thisblockcard)==0:
						continue
					thisblock = deckCatBlock()
					thisblock.cardId = key
					thisblock.card = thisblockcard[0]
					thisblock.pickupStep=stepcount
					thisblock.active=True
					thisblock.number=thisblock.card.max_number
					myDeckBlocks.append(thisblock)
					blocklinecount += 1
					blockcardcount += thisblock.number
					if blockcardcount> 30:
						thisblock.number=blockcardcount-30
						print("End point 3")
						processend=True
						break
					if blockcardcount==30:
						print("End point 4")
						processend=True
						break
			myDeckTexts=[]		
			myDeck=[]
			for winrate in myDeckWinrate:
				myDeckTexts.append("\t\t## Wins: %d / %d = %f (%d)\n"%(winrate[0], winrate[1], 1.0*winrate[0]/winrate[1], winrate[2]))
			for block in myDeckBlocks:
				blockText="\t\t"
				if block.active==False:
					blockText+="## "
				if block.number==2:
					blockText+='"%s","%s",'%(block.cardId,block.cardId)
				else:
					blockText+='"%s",'%(block.cardId)
				blockText+=('#(%d)%s,%s,%s,%s,%d,%d,%d,%s'%(
						block.pickupStep,
						block.card.id,
						block.card.e_name,
						block.card.card_class,
						block.card.rarity,
						block.card.cost,
						block.card.atk,
						block.card.max_health,
						block.card.description
						))
				myDeckTexts.append(blockText)
				if block.active==True:
					myDeck.append(block.cardId)
					if block.number==2:
						myDeck.append(block.cardId)

			df = open(deckfilename, 'w')
			for text in myDeckTexts:
				df.write("%s"%(text))
			df.close()
		pass


	
