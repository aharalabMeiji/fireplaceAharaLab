from ..utils import *

Lich_Neutral=[]

#Lich_Rampaging_Zombie=True# ------------------>
Lich_Shatterskin_Gargoyle=True
Lich_Infected_Peasant=True
Lich_Street_Sweeper=True
Lich_Brittleskin_Zombie=True
Lich_Incorporeal_Corporal=True
Lich_Drakkari_Embalmer=True
Lich_Bone_Flinger=True
Lich_Silvermoon_Arcanist=True
Lich_Sunfury_Clergy=True
Lich_Tenacious_Sanlayn=True
Lich_Crystal_Broker=True
Lich_Astalor_Bloodsworn=True
Lich_Silvermoon_Sentinel=True
Lich_The_Sunwell=True
Lich_Bonelord_Frostwhisper=True
Lich_Invincible=True
Lich_Lorthemar_Theron=True
Lich_Infectious_Ghoul=True
Lich_Sanctum_Spellbender=True
Lich_Arms_Dealer=True
#Lich_Silvermoon_Farstrider_Spellpower=True# ------------------>
Lich_Flesh_Behemoth=True
Lich_Plaguespreader=True
Lich_Foul_Egg=True
Lich_Nerubian_Vizier=True
Lich_Vrykul_Necrolyte=True
Lich_Scourge_Rager=True
Lich_Umbral_Geist=True
Lich_Amber_Whelp=True
Lich_Bloodied_Knight=True
Lich_Translocation_Instructor=True
Lich_Coroner=True
Lich_Enchanter=True
Lich_Silvermoon_Armorer=True
Lich_Banshee=True
Lich_Hawkstrider_Rancher=True

Lich_Banshee=True


if Lich_Rampaging_Zombie:# ------------------>
	Lich_Neutral+=['RLK_018t']
class RLK_018t:# <12>[1776]
	""" Rampaging Zombie
	<b>Rush</b> """
	#
	pass

if Lich_Shatterskin_Gargoyle:# ###
	Lich_Neutral+=['RLK_029']
class RLK_029:# <12>[1776]
	""" Shatterskin Gargoyle
	<b>Taunt</b> <b>Deathrattle:</b> Deal 4 damage to a random enemy. """
	deathrattle = Hit(RANDOM(ENEMY_CHARACTERS), 4)
	pass

if Lich_Infected_Peasant:# ###
	Lich_Neutral+=['RLK_070']
	Lich_Neutral+=['RLK_070t']
class RLK_070:# <12>[1776]
	""" Infected Peasant
	<b>Deathrattle:</b> Summon a 2/2 Undead Peasant. """
	deathrattle = Summon(CONTROLLER, 'RLK_070t')
	pass

class RLK_070t:# <12>[1776]
	""" Undead Peasant
	 """
	#
	pass

if Lich_Street_Sweeper:# 
	Lich_Neutral+=['RLK_104']
class RLK_104:# <12>[1776]
	""" Street Sweeper
	<b>Battlecry:</b> Deal 2 damage to all other minions. """
	play = Hit(ALL_MINIONS - SELF, 2)
	pass

if Lich_Brittleskin_Zombie:# 
	Lich_Neutral+=['RLK_113']
class RLK_113_Action(GameAction):
	def do(self, source):
		if source.controller != source.controller.game.current_player:
			for card in source.controller.opponent.field:
				Hit(card, 3).trigger(source)
		pass
class RLK_113:# <12>[1776]
	""" Brittleskin Zombie
	<b>Deathrattle:</b> If it's your opponent's turn, deal 3 damage to them. """
	deathrattle = RLK_113_Action()
	pass

if Lich_Incorporeal_Corporal:# 
	Lich_Neutral+=['RLK_117']
class RLK_117:# <12>[1776]
	""" Incorporeal Corporal
	After this minion attacks, destroy it. """
	events = Attack(SELF).after(Destroy(Attack.DEFFENDER))
	pass

if Lich_Drakkari_Embalmer:# 
	Lich_Neutral+=['RLK_119']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_119:# <12>[1776]
	""" Drakkari Embalmer
	<b>Battlecry:</b> Give a friendly Undead <b>Reborn</b>. """
	#
	pass

if Lich_Bone_Flinger:# 
	Lich_Neutral+=['RLK_123']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_123:# <12>[1776]
	""" Bone Flinger
	<b>Battlecry:</b> If a friendly Undead died after your last turn, deal 2 damage. """
	#
	pass

if Lich_Silvermoon_Arcanist:# 
	Lich_Neutral+=['RLK_218']
	Lich_Neutral+=['RLK_218e']
	Lich_Neutral+=['RLK_218e2']
	Lich_Neutral+=['RLK_218e3']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_218:# <12>[1776]
	""" Silvermoon Arcanist
	<b>Spell Damage +2</b> <b>Battlecry:</b> Your spells canÅft target heroes this turn. """
	#
	pass

class RLK_218e:# <12>[1776]
	""" Insane Arcanity
	Can't be targeted by spells this turn. """
	#
	pass

class RLK_218e2:# <12>[1776]
	""" Arcane Insanity
	Can't be targeted by spells this turn. """
	#
	pass

class RLK_218e3:# <12>[1776]
	""" Insane Arcane Power
	Your spells canÅft target heroes this turn. """
	#
	pass

if Lich_Sunfury_Clergy:# 
	Lich_Neutral+=['RLK_219']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_219:# <12>[1776]
	""" Sunfury Clergy
	<b>Battlecry:</b> Restore 3 Health to all friendly characters. <b>Manathirst (6):</b> Restore 6 Health instead. """
	#
	pass

if Lich_Tenacious_Sanlayn:# 
	Lich_Neutral+=['RLK_220']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_220:# <12>[1776]
	""" Tenacious San'layn
	<b>Lifesteal</b> Whenever this attacks, deal 2 damage to the enemy hero. """
	#
	pass

if Lich_Crystal_Broker:# 
	Lich_Neutral+=['RLK_221']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_221:# <12>[1776]
	""" Crystal Broker
	<b>Manathirst (5):</b> Summon a random 3-Cost minion. <b>Manathirst (10):</b> Summon an 8-Cost minion instead. """
	#
	pass

if Lich_Astalor_Bloodsworn:# 
	Lich_Neutral+=['RLK_222']
	Lich_Neutral+=['RLK_222t1']
	Lich_Neutral+=['RLK_222t2']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_222:# <12>[1776]
	""" Astalor Bloodsworn
	<b>Battlecry:</b> Add Astalor, the Protector to your hand. <b>Manathirst (@):</b> Deal 2 damage. """
	#
	pass

class RLK_222t1:# <12>[1776]
	""" Astalor, the Protector
	<b>Battlecry:</b> Add Astalor, the Flamebringer to your hand. <b>Manathirst (@):</b> Gain 5 Armor. """
	#
	pass

class RLK_222t2:# <12>[1776]
	""" Astalor, the Flamebringer
	<b>Battlecry:</b> Deal 8 damage randomly split between all enemies. <b>Manathirst (10):</b> Deal 8 more. """
	#
	pass

if Lich_Silvermoon_Sentinel:# 
	Lich_Neutral+=['RLK_518']
	Lich_Neutral+=['RLK_518e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_518:# <12>[1776]
	""" Silvermoon Sentinel
	<b>Taunt</b> <b>Manathirst (@):</b> Gain +2/+2 and <b>Divine Shield</b>. """
	#
	pass

class RLK_518e:# <12>[1776]
	""" Silvermoon's Might
	+2/+2. """
	#
	pass

if Lich_The_Sunwell:# 
	Lich_Neutral+=['RLK_590']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_590:# <12>[1776]
	""" The Sunwell
	Fill your hand with random spells. Costs (1) less for each other card in your hand. """
	#
	pass

if Lich_Bonelord_Frostwhisper:# 
	Lich_Neutral+=['RLK_591']
	Lich_Neutral+=['RLK_591e']
	Lich_Neutral+=['RLK_591e2']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_591:# <12>[1776]
	""" Bonelord Frostwhisper
	<b>Deathrattle:</b> For the rest of the game, your first card each turn costs (0). You die in 3 turns. """
	#
	pass

class RLK_591e:# <12>[1776]
	""" Lich Death Counter
	Your hero dies in @ turns. """
	#
	pass

class RLK_591e2:# <12>[1776]
	""" Lich's Deathcurse
	Costs (0). """
	#
	pass

if Lich_Invincible:# 
	Lich_Neutral+=['RLK_592']
	Lich_Neutral+=['RLK_592e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_592:# <12>[1776]
	""" Invincible
	<b>Reborn</b> <b>Battlecry and Deathrattle:</b> Give a random friendly Undead +5/+5 and <b>Taunt</b>. """
	#
	pass

class RLK_592e:# <12>[1776]
	""" Invincible's Reins
	+5/+5. """
	#
	pass

if Lich_Lorthemar_Theron:# 
	Lich_Neutral+=['RLK_593']
	Lich_Neutral+=['RLK_593e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_593:# <12>[1776]
	""" Lor'themar Theron
	<b>Battlecry:</b> Double the stats of all minions in your deck. """
	#
	pass

class RLK_593e:# <12>[1776]
	""" Superior Strategy
	Doubled Attack and Health. """
	#
	pass

if Lich_Infectious_Ghoul:# 
	Lich_Neutral+=['RLK_653']
	Lich_Neutral+=['RLK_653e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_653:# <12>[1776]
	""" Infectious Ghoul
	<b>Deathrattle:</b> Give a random friendly minion "<b>Deathrattle:</b> Summon an Infectious Ghoul." """
	#
	pass

class RLK_653e:# <12>[1776]
	""" Infected
	<b>Deathrattle:</b> Summon an Infectious Ghoul. """
	#
	pass

if Lich_Sanctum_Spellbender:# 
	Lich_Neutral+=['RLK_677']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_677:# <12>[1776]
	""" Sanctum Spellbender
	Whenever your opponent targets another minion with a spell, redirect it to this. """
	#
	pass

if Lich_Arms_Dealer:# 
	Lich_Neutral+=['RLK_824']
	Lich_Neutral+=['RLK_824e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_824:# <12>[1776]
	""" Arms Dealer
	After you summon an Undead, give it +1 Attack. """
	#
	pass

class RLK_824e:# <12>[1776]
	""" Undead Fortitude
	+1 Attack. """
	#
	pass

if Lich_Silvermoon_Farstrider_Spellpower:# # ------------------>
	Lich_Neutral+=['RLK_826e']
class RLK_826e:# <12>[1776]
	""" Silvermoon Farstrider Spellpower
	<b>Spell Damage +1</b>. """
	#
	pass

if Lich_Flesh_Behemoth:# 
	Lich_Neutral+=['RLK_830']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_830:# <12>[1776]
	""" Flesh Behemoth
	<b>Taunt</b> <b>Deathrattle:</b> Draw another Undead and summon a copy of it. """
	#
	pass

if Lich_Plaguespreader:# 
	Lich_Neutral+=['RLK_831']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_831:# <12>[1776]
	""" Plaguespreader
	<b>Deathrattle:</b> Transform a random minion in your opponent's hand into a Plaguespreader. """
	#
	pass

if Lich_Foul_Egg:# 
	Lich_Neutral+=['RLK_833']
	Lich_Neutral+=['RLK_833t']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_833:# <12>[1776]
	""" Foul Egg
	<b>Deathrattle:</b> Summon a 3/3 Undead Chicken. """
	#
	pass

class RLK_833t:# <12>[1776]
	""" Foul Fowl
	 """
	#
	pass

if Lich_Nerubian_Vizier:# 
	Lich_Neutral+=['RLK_834']
	Lich_Neutral+=['RLK_834e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_834:# <12>[1776]
	""" Nerubian Vizier
	<b>Battlecry:</b> <b>Discover</b> a spell. If a friendly Undead died after your last turn, it costs (2) less. """
	#
	pass

class RLK_834e:# <12>[1776]
	""" Nerubian Vision
	Costs (2) less. """
	#
	pass

if Lich_Vrykul_Necrolyte:# 
	Lich_Neutral+=['RLK_867']
	Lich_Neutral+=['RLK_867e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_867:# <12>[1776]
	""" Vrykul Necrolyte
	<b>Battlecry:</b> Give a friendly minion "<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Rush</b>." """
	#
	pass

class RLK_867e:# <12>[1776]
	""" It's Necro-Lit
	<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Rush</b>. """
	#
	pass

if Lich_Scourge_Rager:# 
	Lich_Neutral+=['RLK_900']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_900:# <12>[1776]
	""" Scourge Rager
	<b>Reborn</b> <b>Battlecry:</b> Die. """
	#
	pass

if Lich_Umbral_Geist:# 
	Lich_Neutral+=['RLK_914']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_914:# <12>[1776]
	""" Umbral Geist
	<b>Deathrattle:</b> Add a random Shadow spell to your hand. """
	#
	pass

if Lich_Amber_Whelp:# 
	Lich_Neutral+=['RLK_915']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_915:# <12>[1776]
	""" Amber Whelp
	<b>Battlecry:</b> If you're holding a Dragon, deal 3 damage. """
	#
	pass

if Lich_Bloodied_Knight:# 
	Lich_Neutral+=['RLK_926']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_926:# <12>[1776]
	""" Bloodied Knight
	At the end of your turn, deal 2 damage to your hero. """
	#
	pass

if Lich_Translocation_Instructor:# 
	Lich_Neutral+=['RLK_950']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_950:# <12>[1776]
	""" Translocation Instructor
	<b>Battlecry:</b> Choose an enemy minion. Swap it with a random one in their deck. """
	#
	pass

if Lich_Coroner:# 
	Lich_Neutral+=['RLK_951']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_951:# <12>[1776]
	""" Coroner
	<b>Battlecry:</b> <b>Freeze</b> an enemy minion. <b>Manathirst (6):</b> <b>Silence</b> it first. """
	#
	pass

if Lich_Enchanter:# 
	Lich_Neutral+=['RLK_952']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_952:# <12>[1776]
	""" Enchanter
	Enemy minions take double damage during your turn. """
	#
	pass

if Lich_Silvermoon_Armorer:# 
	Lich_Neutral+=['RLK_955']
	Lich_Neutral+=['RLK_955e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_955:# <12>[1776]
	""" Silvermoon Armorer
	<b>Rush</b> <b>Manathirst (@):</b> Gain +2/+2. """
	#
	pass

class RLK_955e:# <12>[1776]
	""" Supplied
	+2/+2. """
	#
	pass

if Lich_Banshee:# 
	Lich_Neutral+=['RLK_957']
	Lich_Neutral+=['RLK_957e']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_957:# <12>[1776]
	""" Banshee
	<b>Deathrattle:</b> Give a random friendly Undead +2/+1. """
	#
	pass

class RLK_957e:# <12>[1776]
	""" Banshee's Wail
	+2/+1. """
	#
	pass

if Lich_Hawkstrider_Rancher:# 
	Lich_Neutral+=['RLK_970']
	Lich_Neutral+=['RLK_970e']
	Lich_Neutral+=['RLK_970t']
class RLK__Action(GameAction):
	def do(self, source):
		pass
class RLK_970:# <12>[1776]
	""" Hawkstrider Rancher
	After you play a minion, give it +1/+1 and "<b>Deathrattle:</b> Summon a 1/1 Hawkstrider." """
	#
	pass

class RLK_970e:# <12>[1776]
	""" Hawkriding
	+1/+1. <b>Deathrattle:</b> Summon a 1/1 Hawkstrider. """
	#
	pass

class RLK_970t:# <12>[1776]
	""" Hawkstrider
	 """
	#
	pass


