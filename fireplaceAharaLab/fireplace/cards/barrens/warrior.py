
from ..utils import *

Barrens_Warrior=['BAR_334','BAR_840','BAR_841','BAR_841e',
'BAR_842','BAR_842t','BAR_842t2','BAR_843',
'BAR_846','BAR_847','BAR_896','BAR_896e',
'WC_024','WC_024e','WC_025','WC_025e','WC_026','WC_026t',]
#'BAR_844','BAR_845',

class BAR_334:# <10>[1525]
	""" Overlord Saurfang
	[Battlecry:] Resurrect 2 friendly [Frenzy] minions. Deal 1 damage to all other minions. """
	#
	pass

class BAR_840:# <10>[1525]
	""" Whirling Combatant
	[Battlecry and Frenzy:]Deal 1 damage to allother minions. """
	#
	pass

class BAR_841:# <10>[1525]
	""" Bulk Up
	Give a random [Taunt] minion in your hand +1/+1 and copy it. """
	#
	pass

class BAR_841e:# <10>[1525]
	""" Swoll
	+1/+1. """
	#
	pass

class BAR_842:# <10>[1525]
	""" Conditioning (Rank 1)
	Give minions in your hand +1/+1. <i>(Upgrades when you have 5 Mana.)</i> """
	#
	pass

class BAR_842t:# <10>[1525]
	""" Conditioning (Rank 2)
	Give minions in yourhand +2/+2. <i>(Upgradeswhen you have 10 Mana.)</i> """
	#
	pass

class BAR_842t2:# <10>[1525]
	""" Conditioning (Rank 3)
	Give minions in your hand +3/+3. """
	#
	pass

class BAR_843:# <10>[1525]
	""" Warsong Envoy
	[Frenzy:] Gain +1  Attackfor each damaged character. """
	#
	pass

#class BAR_844:### bigWarrior
#	"""Outrider's Axe
#	After your hero attacks and kills a minion, draw a card."""
#	events = Attack(FRIENDLY_HERO, ALL_MINIONS).after(
#		Dead(ALL_MINIONS + Attack.DEFENDER) & Draw(CONTROLLER))
#	pass

#class BAR_845:###OK   bigWarrior
#	"""Rancor
#	Deal 2 damage to all minions. Gain 2 Armor for each destroyed."""
#	# 生の苦悩、ケルスザード校長らへんが参考になりそうだがわからん
#	# これでよいなら・・・動いているような感じはある。
#	play = Hit(ALL_MINIONS, 2).then( Dead(ALL_MINIONS + Hit.TARGET) & GainArmor(FRIENDLY_HERO, 2))
#	pass

class BAR_846:# <10>[1525]
	""" Mor'shan Elite
	[Taunt]. [Battlecry:] If your heroattacked this turn, summona copy of this. """
	#
	pass

class BAR_847:# <10>[1525]
	""" Rokara
	[Rush]After a friendly minionattacks and survives,give it +1/+1. """
	#
	pass

class BAR_896:# <10>[1525]
	""" Stonemaul Anchorman
	[Rush][Frenzy:] Draw a card. """
	#
	pass

class BAR_896e:# <10>[1525]
	""" Incensed
	Increased Attack. """
	#
	pass

class BOM_01_ArrivalInOrgrimmar_01e:# <10>[1525]
	""" Rokara's Aspiration
	Costs (1). """
	#
	pass

class BOM_01_ArrivalInOrgrimmar_01s:# <10>[1525]
	""" Arrival In Orgrimmar
	Add two Champions of the Horde to your hand.They cost (1). """
	#
	pass

class BOM_01_ForTheHorde_05s:# <10>[1525]
	""" Strength and Honor!
	Summon your allies. """
	#
	pass

class BOM_01_Garrosh_008hb:# <10>[1525]
	""" Garrosh
	<i>Garrosh has been waiting for Rokara to return andhe is NOT_happy_about it.</i> """
	#
	pass

class BOM_01_Garrosh_08p:# <10>[1525]
	""" Equip Gorehowl
	[Hero Power]Equip GorehowlYour hero is[Immune] while attacking. """
	#
	pass

class BOM_01_Golem_005hb:# <10>[1525]
	""" Golem
	<i>Kazakus saw to itthat his caravanwas well-guarded.</i> """
	#
	pass

class BOM_01_PrideOfTheFrostwolves_0:# <10>[1525]
	""" Pride of the Frostwolves
	Gain 5 Armor. Equip a random weapon. """
	#
	pass

class BOM_01_Rokara_001hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_002hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_003hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_004hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_005hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_006hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_007hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_008hp:# <10>[1525]
	""" Rokara
	 """
	#
	pass

class BOM_01_Rokara_01p:# <10>[1525]
	""" Early Axes
	[Hero Power]Equip a 3/1 Axe. """
	#
	pass

class BOM_01_Rokara_03p:# <10>[1525]
	""" Ask for Help
	[Passive Hero Power]Choose an ally tohelp you in battle! """
	#
	pass

class BOM_01_Rokara_04p:# <10>[1525]
	""" Ask for Help
	[Passive Hero Power]Choose an ally tohelp you in battle! """
	#
	pass

class BOM_01_Rokara_05p:# <10>[1525]
	""" Ask for Help
	[Passive Hero Power]Choose an ally tohelp you in battle! """
	#
	pass

class BOM_01_Rokara_06p:# <10>[1525]
	""" Ask for Help
	[Passive Hero Power]Choose an ally tohelp you in battle! """
	#
	pass

class BOM_01_Rokara_07p:# <10>[1525]
	""" Ask for Help
	[Passive Hero Power]Choose an ally tohelp you in battle! """
	#
	pass

class BOM_01_Rokara_08p:# <10>[1525]
	""" Axe and Receive
	[Hero Power]Equip a 4/2 Axe. """
	#
	pass

class BOM_01_RokarasAxe_01w:# <10>[1525]
	""" Rokara's Axe
	 """
	#
	pass

class BOM_01_RokarasGreatAxe_08w:# <10>[1525]
	""" Rokara's Great Axe
	 """
	#
	pass

class BOM_01_SecurityGolem_05t:# <10>[1525]
	""" Security Golem
	 """
	#
	pass

class BOM_01_StrengthAndHonor_05s_Copy:# <10>[1525]
	""" Strength and Honor!_Copy
	Summon your allies. """
	#
	pass

class BOM_01_Twinbraid_06p:# <10>[1525]
	""" Armored Slam
	[Hero Power]Gain 1 Armor. Deal 1 damage to a minion for each Armor you have. """
	#
	pass

class BOM_02_BigRedButton_04p:# <10>[1525]
	""" Big Red Button
	[Hero Power]Activate this turn'sMech Suit power! """
	#
	pass

class BOM_02_Haywire_05s:# <10>[1525]
	""" Haywire
	[Casts When Drawn]You take 4 damage. """
	#
	pass

class BOM_02_Kargal_001hb:# <10>[1525]
	""" Kargal Battlescar
	<i>Belligerent orc grunts defend the frontier of the_Horde's_domain.</i> """
	#
	pass

class BOM_02_Kargal_01p:# <10>[1525]
	""" Keep Watch
	[Hero Power]Summon a random Watch Post. """
	#
	pass

class BOM_02_Xyrella_05p:# <10>[1525]
	""" Big Red Button
	[Hero Power]Activate this turn'sMech Suit power! """
	#
	pass

class BOM_03_Rokara_02p:# <10>[1525]
	""" Rokara
	[Hero Power]Give a friendly minion +1/+1 and [Taunt]. """
	#
	pass

class BOM_03_Rokara_02pe1:# <10>[1525]
	""" Rokara's Might
	+1/+1 and [Taunt]. """
	#
	pass

class BOM_03_Rokara_08t:# <10>[1525]
	""" Rokara
	[Rush][Deathrattle:] Go [Dormant] for 2 turns. """
	#
	pass

class BOM_04_Samuro_001hb:# <10>[1525]
	""" Samuro
	<i>Kurtrus wakes from his nightmare and finds a battle_is_underway.</i> """
	#
	pass

class BOM_04_Samuro_001p:# <10>[1525]
	""" Bladestorm
	[Hero Power]Deal 1 damage to all minions. """
	#
	pass

class BOM_04_SamurosBlade_001w:# <10>[1525]
	""" Samuro's Blade
	Also damages the minions next to whomever your hero_attacks. """
	#
	pass

class Story_07_AthleticStudies:# <10>[1525]
	""" Athletic Studies
	[Discover] a [Rush] minion. Your next one costs (1) less. """
	#
	pass

class Story_07_CorruptGarrosh:# <10>[1525]
	""" Garrosh Hellscream
	 """
	#
	pass

class Story_07_Deathwing_006hb:# <10>[1525]
	""" Deathwing
	<i>Once the noble Aspect of Earth, he has betrayed his charge, becoming bent on destruction.</i> """
	#
	pass

class Story_07_Deathwing_006hb2:# <10>[1525]
	""" Deathwing
	 """
	#
	pass

class Story_07_Deathwing_006hb3:# <10>[1525]
	""" Deathwing
	 """
	#
	pass

class Story_07_Devastate:# <10>[1525]
	""" Devastate
	Deal $4 damage to a damaged minion. """
	#
	pass

class Story_07_Garrosh_008hb:# <10>[1525]
	""" Garrosh
	<i>Instead of gaining wisdom, he has lost his honor. You must be the one to remove him from command.</i> """
	#
	pass

class Story_07_Garrosh_008p2:# <10>[1525]
	""" Equip Gorehowl
	[Hero Power]Equip Gorehowl. """
	#
	pass

class Story_07_Grommash:# <10>[1525]
	""" Grommash Hellscream
	[Charge]Has +6 Attack while damaged.[Deathrattle:] Go [Dormant] for4 turns. """
	#
	pass

class Story_07_GrommashDormant:# <10>[1525]
	""" Grommash Hellscream
	[Dormant] """
	#
	pass

class Story_07_Stranger_003hb:# <10>[1525]
	""" Mysterious Stranger
	<i>He speaks ill of Grommash Hellscream and his efforts to free the imprisoned orcs. But why?</i> """
	#
	pass

class Story_07_Stranger_003hb2:# <10>[1525]
	""" Orgrim Doomhammer
	 """
	#
	pass

class Story_07_Thrall_001hp:# <10>[1525]
	""" Thrall
	 """
	#
	pass

class Story_07_Thrall_002hp:# <10>[1525]
	""" Thrall
	 """
	#
	pass

class Story_08_Saurfang_008h2:# <10>[1525]
	""" Varok Saurfang
	 """
	#
	pass

class Story_08_Saurfang_008p:# <10>[1525]
	""" Survival of the Horde
	[Passive Hero Power]If you have less than 3 minions, your minions have +1/+1 this turn. """
	#
	pass

class Story_09_Blackhand_004hb:# <10>[1525]
	""" Chieftains of the Horde
	<i>The hour has come to corrupt the orcs so they will serve as Kil'jaeden's army.</i> """
	#
	pass

class Story_09_Blackhand_004p:# <10>[1525]
	""" Instruments of War
	<i>The orc chieftains gather on the eve of battle...</i> """
	#
	pass

class Story_09_Durotan:# <10>[1525]
	""" Durotan
	 """
	#
	pass

class Story_09_Grommash:# <10>[1525]
	""" Grommash Hellscream
	 """
	#
	pass

class Story_09_Grommash_004hb:# <10>[1525]
	""" Grommash Hellscream
	 """
	#
	pass

class Story_09_Grommash_004hb2:# <10>[1525]
	""" Grommash Hellscream
	 """
	#
	pass

class Story_09_Hurkan:# <10>[1525]
	""" Hurkan Skullsplinter
	 """
	#
	pass

class Story_09_Hurkan2:# <10>[1525]
	""" Hurkan Skullsplinter
	 """
	#
	pass

class Story_09_Kargath:# <10>[1525]
	""" Kargath Bladefist
	 """
	#
	pass

class Story_09_Kargath2:# <10>[1525]
	""" Kargath Bladefist
	 """
	#
	pass

class Story_09_Kilrogg:# <10>[1525]
	""" Kilrogg Deadeye
	 """
	#
	pass

class Story_09_Kilrogg2:# <10>[1525]
	""" Kilrogg Deadeye
	 """
	#
	pass

class Story_09_Orgrim_004hb:# <10>[1525]
	""" Orgrim Doomhammer
	 """
	#
	pass

class Story_09_Orgrim_006hb:# <10>[1525]
	""" Orgrim Doomhammer
	<i>The tides of war have turned in favor of this insolent upstart. As warchief, he now controls your fate.</i> """
	#
	pass

class Story_09_Orgrim_006p:# <10>[1525]
	""" Warchief's Vengeance
	[Passive Hero Power]Your minions have +1/+1 while you have a weapon equipped. """
	#
	pass

class Story_09_Warrior_001hb:# <10>[1525]
	""" Forgotten Warrior
	<i>No one living remembers the leader of Gul'dan's village, but the legacy of his cruelty outlasted him.</i> """
	#
	pass

class Story_09_Warrior_001p:# <10>[1525]
	""" Bully the Weak
	[Hero Power]Deal the damage of the highest Attack minion to the enemy hero. """
	#
	pass

class WC_024:# <10>[1525]
	""" Man-at-Arms
	[Battlecry:] If you have a weapon equipped, gain +1/+1. """
	#
	pass

class WC_024e:# <10>[1525]
	""" Armed
	+1/+1 """
	#
	pass

class WC_025:# <10>[1525]
	""" Whetstone Hatchet
	After your hero attacks, give a minion in your hand +1 Attack. """
	#
	pass

class WC_025e:# <10>[1525]
	""" Armed
	+1 Attack """
	#
	pass

class WC_026:# <10>[1525]
	""" Kresh, Lord of Turtling
	[Frenzy:] Gain 8 Armor. [Deathrattle:] Equip a 2/5 Turtle Spike. """
	#
	pass

class WC_026t:# <10>[1525]
	""" Turtle Spike
	 """
	#
	pass

