from ..utils import *

#class SCH_133:
#	""" Wolpertinger 
#	雄叫び: このミニオンの   コピーを1体召喚する。"""
#	play = Summon(CONTROLLER, Copy(SELF))

#class SCH_617:
#	"""  カワイイ侵入者 
#	ミニオン1体に +1/+1を付与する。 1/1の仔を1体召喚する。 仔1体を自分の 手札に追加する。"""
#	requirements = {
#		PlayReq.REQ_MINION_TARGET: 0,
#		PlayReq.REQ_TARGET_TO_PLAY: 0}
#	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"),Give(CONTROLLER, "SCH_617t")

#SCH_617e = buff(1, 1)

#class SCH_617t:
#	pass


#class DRG_253:
#	""" ドワーフの狙撃手
#	[x]自分のヒーローパワーはミニオンを対象にできる。
#	""" 
	#update = Refresh(CONTROLLER, {GameTag.STEADY_SHOT_CAN_TARGET: True})#STADY_SHOT=不抜の一矢
	#むしろ、別カードにMorphする処理のほうが適切と思われる。
	#検証不能

#class SCH_600:
#	""" 悪魔の相棒 
#	 ランダムな悪魔の相棒を1体召喚する。 """
#	#play = Summon(CONTROLLER, "SCH_600t1")#, "SCH_600t2", "SCH_600t3"}))##内容確認
#	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
#	entourage = ["SCH_600t1", "SCH_600t2", "SCH_600t3"]
#	play = Summon(CONTROLLER, RandomEntourage())
#	#def play(self):
#	#	friend_demon = random.choice(["SCH_600t1", "SCH_600t2", "SCH_600t3"])
#	#	yield Summon(CONTROLLER, friend_demon)

#class SCH_600t1:
#	""" フハァー """
#	pass
#class SCH_600t2:
#	""" シーミャ """
#	pass
#class SCH_600t3:
#	""" オレック
#	[x]自身を除く味方のミニオンは攻撃力+1を得る。 """
#	update = Refresh(FRIENDLY_MINIONS - SELF, buff="SCH_600t3e")

#SCH_600t3e = buff(1,0)

#class DRG_252:
#	""" フェーズ・ストーカー 
#	[x]自分がヒーローパワーを使用した後自分のデッキから<b>秘策</b>を1つ準備する。 """
#	play = Activate(CONTROLLER, HERO_POWER).on(Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + SECRET)))
#	pass


#class ULD_152:
#	#""" 感圧板 
#	#<b>秘策:</b>相手が呪文を使用した後ランダムな敵のミニオン1体を破壊する。 """
#	secret = Play(OPPONENT, SPELL).on(Reveal(SELF), Destroy(RANDOM_ENEMY_MINION))

#	#pass

#class DRG_256:
#	""" ドラゴンベイン 
#	[x]自分がヒーローパワーを使用した後ランダムな敵1体に___5ダメージを与える。 """
#	play = Activate(CONTROLLER, HERO_POWER).on(Hit(RANDOM_ENEMY_CHARACTER, 5))
#	pass
