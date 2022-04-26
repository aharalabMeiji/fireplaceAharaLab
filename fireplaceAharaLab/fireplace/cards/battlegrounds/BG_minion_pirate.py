from ..utils import *
from fireplace.battlegrounds.BG_actions import *

BG_Minion_Pirate=[
	'BGS_055','TB_BaconUps_126',#Deck Swabbie (1)
	'BGS_061','BGS_061t','TB_BaconUps_141','TB_BaconUps_141t',#Scallywag,1
	'BGS_049','TB_BaconUps_127',#Freedealing Gambler,2
	'CORE_NEW1_027','NEW1_027e','TB_BaconUps_136','TB_BaconUps_136e',#Southsea Captain,2
	'BGS_060','TB_BaconUps_150',#Yo-Ho-Ogre,2
	'BG21_017','BG21_017_G',#Briny Bootlegger,3
	'BGS_081','BGS_081e','TB_BaconUps_143','TB_BaconUps_143e',#Salty Looter,3
	'BGS_048','BGS_048e','TB_BaconUps_140','TB_BaconUps_140e',#Southsea Strongarm,3,
	'BGS_066','BGS_066e','TB_BaconUps_130','TB_BaconUps_130e',#Goldgrubber,4
	'BG21_016','BG21_016e','BG21_016_G','BG21_016_Ge',#Peggy Brittlebone,4
	'BGS_056','BGS_056e','TB_BaconUps_139','TB_BaconUps_139e',#Ripsnarl Captain,4,
	'BGS_072','TB_BaconUps_133',#Cap'n Hoggarr,5
	'BG21_031','BG21_031_G',#Tony Two-Tusk,5
	'BGS_047','BGS_047e','TB_BaconUps_134','TB_BaconUps_134e',#Dread Admiral Eliza,6
	'BG21_019','BG21_019_G',#Nosy Looter,6
	]

BG_PoolSet_Pirate=[
	['BGS_055','BGS_061',],
	['BGS_049','CORE_NEW1_027','BGS_060',],
	['BG21_017','BGS_081','BGS_048',],
	['BGS_066','BG21_016','BGS_056',],
	['BGS_072','BG21_031',],
	['BGS_047', 'BG21_019',],
	]

BG_Pirate_Gold={
	'BGS_055':'TB_BaconUps_126',#Deck Swabbie (1)
	'BGS_061':'TB_BaconUps_141',#Scallywag,1
	'BGS_049':'TB_BaconUps_127',#Freedealing Gambler,2
	'CORE_NEW1_027':'TB_BaconUps_136',#Southsea Captain,2
	'BGS_060':'TB_BaconUps_150',#Yo-Ho-Ogre,2
	'BG21_017':'BG21_017_G',#Briny Bootlegger,3
	'BGS_081':'TB_BaconUps_143',#Salty Looter,3
	'BGS_048':'TB_BaconUps_140',#Southsea Strongarm,3,
	'BGS_066':'TB_BaconUps_130',#Goldgrubber,4
	'BG21_016':'BG21_016_G',#Peggy Brittlebone,4
	'BGS_056':'TB_BaconUps_139',#Ripsnarl Captain,4,
	'BGS_072':'TB_BaconUps_133',#Cap'n Hoggarr,5
	'BG21_031':'BG21_031_G',#Tony Two-Tusk,5
	'BGS_047':'TB_BaconUps_134',#Dread Admiral Eliza,6
	'BG21_019':'BG21_019_G',#Nosy Looter,6
	}


#Deck Swabbie,1,2,2,Pirate,Battlecry
class BGS_055:# 甲板みがき　動作確認済み
	""" Deck Swabbie <pirate>  (2/2)
	&lt;b&gt;Battlecry:&lt;/b&gt; Reduce the cost of upgrading Bob's Tavern by (1). """
	play = ReduceTierUpCost(CONTROLLER,1)
	pass
class TB_BaconUps_126:
	""" Deck Swabbie <pirate>  (4/4)
	&lt;b&gt;Battlecry:&lt;/b&gt; Reduce the cost of upgrading Bob's Tavern by (2). """
	play = ReduceTierUpCost(CONTROLLER,2)
	pass

#Scallywag,1,3,1,Pirate,Deathrattle
class BGS_061:# <12>[1453]
	""" Scallywag
	[Deathrattle:] Summon a 1/1 Pirate. It attacks immediately. """
	deathrattle = Summon(CONTROLLER, 'BGS_061t').then(RegularAttack(Summon.CARD,RANDOM_ENEMY_MINION))
	pass
class BGS_061t:# <7>[1453]
	""" Sky Pirate
	 """
	#
	pass
class TB_BaconUps_141:# <12>[1453]
	""" Scallywag
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 2/2 Pirate. It attacks immediately. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_141t').then(RegularAttack(Summon.CARD,RANDOM_ENEMY_MINION))
	pass
class TB_BaconUps_141t:# <7>[1453]
	""" Sky Pirate
	 """
	#
	pass

#Freedealing Gambler,2,3,3,Pirate,-
class BGS_049:# <12>[1453]
	""" Freedealing Gambler
	This minion sells for 3 Gold. """
	#		<Tag enumID="1587" name="3" type="Int" value="3"/> 謎タグ
	pass
class TB_BaconUps_127:# <12>[1453]
	""" Freedealing Gambler
	This minion sells for 6 Gold. """
	#		<Tag enumID="1587" name="6" type="Int" value="6"/> 謎タグ
	pass

#Southsea Captain,2,3,3,Pirate,-
class NEW1_027:
	""" Southsea Captain
	Your other Pirates have +1/+1. """
	update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="NEW1_027e")
	pass
NEW1_027e = buff(+1, +1)
class TB_BaconUps_136:
	""" Southsea Captain
	Your other Pirates have +2/+2. """
	update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="TB_BaconUps_136e")
	pass
TB_BaconUps_136e = buff(+2, +2)

#Yo-Ho-Ogre,2,3,5,Pirate,Taunt
class BGS_060:# <12>[1453]
	""" Yo-Ho-Ogre
	[Taunt]After this minion survives being attacked, attack immediately. """
	events = Attack(ENEMY_MINIONS, SELF).after(RegularAttack(SELF, RANDOM_ENEMY_MINION))
	pass
class TB_BaconUps_150:# <12>[1453]
	""" Yo-Ho-Ogre (2/6/10)
	[Taunt]After this minion survives being attacked, attack immediately. """
	events = Attack(ENEMY_MINIONS, SELF).after(RegularAttack(SELF, RANDOM_ENEMY_MINION)) 
	pass

#Briny Bootlegger,3,4,4,Pirate,-
class BG21_017:# <12>[1453]
	""" Briny Bootlegger
	At the end of your turn,if you have another Pirate,add a Gold Coin to your hand. """
	events = OWN_TURN_END.on(Find(FRIENDLY_MINIONS - SELF + PIRATE) & Give(CONTROLLER, "GAME_005"))
	pass
class BG21_017_G:# <12>[1453]
	""" Briny Bootlegger
	At the end of your turn,if you have another Pirate,add 2 Gold Coins to your hand. """
	events = OWN_TURN_END.on(Find(FRIENDLY_MINIONS - SELF + PIRATE) & (Give(CONTROLLER, "GAME_005"),Give(CONTROLLER, "GAME_005")))
	pass

#Salty Looter,3,4,5,Pirate,-
class BGS_081:# <7>[1453]
	""" Salty Looter
	Whenever you play a Pirate, gain +1/+1. """
	events = BG_Play(CONTROLLER, PIRATE).on(Buff(SELF,'BGS_081e'))
	pass
BGS_081e=buff(1,1)
class TB_BaconUps_143:# <7>[1453]
	""" Salty Looter
	Whenever you play a Pirate, gain +2/+2. """
	events = BG_Play(CONTROLLER, PIRATE).on(Buff(SELF,'TB_BaconUps_143e'))
	pass
TB_BaconUps_143e=buff(2,2)

#Southsea Strongarm,3,4,3,Pirate,Battlecry
class BGS_048:# <12>[1453]
	""" Southsea Strongarm
	[Battlecry:] Give a friendly Pirate +1/+1. Repeat foreach Pirate you bought this turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	def play(self):
		count=1
		log = self.controller.buy_this_turn_log()
		for card in log:
			if card.race == Race.PIRATE:
				count += 1
		for repeat in range(count):
			yield Buff(TARGET, 'BGS_048e')
	pass
BGS_048e=buff(1,1)
class TB_BaconUps_140:# <12>[1453]
	""" Southsea Strongarm
	[Battlecry:] Give a friendly Pirate +2/+2. Repeat foreach Pirate you boughtthis turn. """
	def play(self):
		count=1
		log = self.controller.buy_this_turn_log()
		for card in log:
			if card.race == Race.PIRATE:
				count += 1
		for repeat in range(count):
			yield Buff(TARGET, 'TB_BaconUps_140e')
	pass
TB_BaconUps_140e=buff(2,2)



#Goldgrubber,4,4,4,Pirate,-
class BGS_066:# <12>[1453] 金ぴか
	""" Goldgrubber
	At the end of your turn, gain +2/+2 for each friendly Golden minion. """
	events = OWN_TURN_END.on(Buff(FRIENDLY_MINIONS + GOLDEN, 'BGS_066e'))
	pass
BGS_066e=buff(2,2)
class TB_BaconUps_130:# <12>[1453]
	""" Goldgrubber
	At the end of your turn, gain +4/+4 for each friendly Golden minion. """
	events = OWN_TURN_END.on(Buff(FRIENDLY_MINIONS + GOLDEN, 'TB_BaconUps_130e'))
	pass
TB_BaconUps_130e=buff(4,4)



#Peggy Brittlebone,4,6,5,Pirate,-
class BG21_016:# <12>[1453] 義足
	""" Peggy Brittlebone
	After a card is added to your hand, give another friendly Pirate +1/+1. """
	events = [
		Buy(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'BG21_016e')),
		Give(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'BG21_016e')),
		]
	pass
BG21_016e=buff(1,1)
class BG21_016_G:# <12>[1453]
	""" Peggy Brittlebone
	After a card is added to your hand, give another friendly Pirate +2/+2. """
	events = [
		Buy(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'BG21_016_Ge')),
		Give(CONTROLLER,MINION).on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'BG21_016_Ge')),
		]
	pass
BG21_016_Ge=buff(2,2)

#Ripsnarl Captain,4,4,6,Pirate,-
class BGS_056:# <12>[1453] ギリガルル
	""" Ripsnarl Captain
	Whenever another friendly Pirate attacks, give it +2/+2. """
	events = Attack(FRIENDLY + PIRATE).on(Buff(Attack.ATTACKER,'BGS_056e'))
	pass
BGS_056e=buff(2,2)
class TB_BaconUps_139:# <12>[1453]
	""" Ripsnarl Captain
	Whenever another friendly Pirate attacks, give it +4/+4. """
	events = Attack(FRIENDLY + PIRATE).on(Buff(Attack.ATTACKER,'TB_BaconUps_139e'))
	pass
TB_BaconUps_139e=buff(4,4)



#Cap'n Hoggarr,5,6,6,Pirate,-
class BGS_072:# <12>[1453] ホガァ
	""" Cap'n Hoggarr
	Whenever you buy a Pirate,gain 1 Gold this turn only. """
	events = Buy(CONTROLLER, MINION + PIRATE).on(ManaThisTurn(CONTROLLER, 1))
	pass
class TB_BaconUps_133:# <12>[1453]
	""" Cap'n Hoggarr
	Whenever you buy a Pirate, gain 2 Gold this turn only. """
	events = Buy(CONTROLLER, MINION + PIRATE).on(ManaThisTurn(CONTROLLER, 2))
	pass



#Tony Two-Tusk,5,4,6,Pirate,Avenge (X)
class BG21_031_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		friendly_pirates=[]
		for card in controller.field:
			if card.race==Race.PIRATE:
				friendly_pirates.append(card)
		if len(friendly_parates)>0:
			card = random.choice(friendly_pirates)
			original_card = card.deepcopy_original
			new_card = controller.game.BG_morph_gold(card)
			new_original_card = original_card.controller.game.BG_morph_gold(card)
		pass
class BG21_031:# <12>[1453]
	""" Tony Two-Tusk
	[Avenge (4):] Make another friendly Pirate Golden permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [BG21_031_Action(CONTROLLER)]))
	pass
class BG21_031_G:# <12>[1453]
	""" Tony Two-Tusk
	[Avenge (4):] Make 2 other friendly Pirates Golden permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [BG21_031_Action(CONTROLLER), BG21_031_Action(CONTROLLER)]))
	pass




#Dread Admiral Eliza,6,6,7,Pirate,-
class BGS_047:# <12>[1453]  エリザ
	""" Dread Admiral Eliza
	Whenever a friendly Pirate attacks, give all friendly minions +2/+1. """
	events = Attack(FRIENDLY_MINIONS + PIRATE).on(Buff(FRIENDLY_MINIONS,'BGS_047e'))
	pass
BGS_047e=buff(2,1)
class TB_BaconUps_134:# <12>[1453]
	""" Dread Admiral Eliza
	Whenever a friendly Pirate attacks, give all friendly minions +4/+2. """
	events = Attack(FRIENDLY_MINIONS + PIRATE).on(Buff(FRIENDLY_MINIONS,'TB_BaconUps_134e'))
	pass
TB_BaconUps_134e=buff(4,2)




#Nosy Looter,6,9,8,Pirate,-
class BG21_019_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		decks = controller.game.parent.BG_decks
		dk=[]
		for i in range(grade):
			dk += decks[i]
		for repeat in range(amount):
			cardID = random.choice(dk)
			controller.game.BG_deal_gold(cardID)
		pass
class BG21_019:# <12>[1453] 戦利品詮索屋
	""" Nosy Looter
	Every two turns,add a random Golden minion to your hand.<i>(@ |4(turn, turns) left!)</i> """
	events = OWN_TURN_BEGIN.on(SidequestCounter(SELF, 2, [BG21_019_Action(CONTROLLER,1)]))
	pass
class BG21_019_G:# <12>[1453]
	""" Nosy Looter
	At the start of your turn,add a random Golden minion to your hand. """
	events = OWN_TURN_BEGIN.on(SidequestCounter(SELF, 2, [BG21_019_Action(CONTROLLER,2)]))
	pass



