from ..utils import *

class SCH_133:
	""" Wolpertinger """
	play = Summon(CONTROLLER, Copy(SELF))

class SCH_617:
	"""  カワイイ侵入者 """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"),Give(CONTROLLER, "SCH_617t")

SCH_617e = buff(+1, +1)


class DRG_253:
	""" ドワーフの狙撃手
	[x]自分のヒーローパワーはミニオンを対象にできる。
	""" 
	update = Refresh(CONTROLLER, {GameTag.STEADY_SHOT_CAN_TARGET: True})#STADY_SHOT=不抜の一矢
	#むしろ、別カードにMorphする処理のほうが適切と思われる。
	#検証不能

class SCH_600:
	""" 悪魔の相棒 
	 ランダムな悪魔の相棒を1体召喚する。 """
	#play = Summon(CONTROLLER, "SCH_600t1")#, "SCH_600t2", "SCH_600t3"}))##内容確認
	def play(self):
		friend_demon = random.choice(["SCH_600t1", "SCH_600t2", "SCH_600t3"])
		yield Summon(CONTROLLER, friend_demon)

class SCH_600t1:
	pass
class SCH_600t2:
	pass
class SCH_600t3:
	""" [x]自身を除く味方のミニオンは攻撃力+1を得る。 """
	update = Refresh(FRIENDLY_MINIONS - SELF, "SCH_600t3e")

SCH_600t3e = buff(atk=+1)

class DRG_252:
	""" フェーズ・ストーカー 
	[x]自分がヒーローパワーを使用した後自分のデッキから&lt;b&gt;秘策&lt;/b&gt;を1つ準備する。 """
	play = Activate(CONTROLLER, HERO_POWER).after(Play(CONTROLLER, FRIENDLY_DECK + SECRET))
	pass

class EX1_611:
	""" 感圧板 
	&lt;b&gt;秘策:&lt;/b&gt;相手が呪文を使用した後ランダムな敵のミニオン1体を破壊する。 """
	secret =  Play(OPPONENT, SPELL).after(Destroy(RANDOM_ENEMY_MINION))
	pass

class DRG_256:
	""" ドラゴンベイン 
	[x]自分がヒーローパワーを使用した後ランダムな敵1体に___5ダメージを与える。 """
	events = Activate(CONTROLLER, HERO_POWER).after(Hit(RANDOM_ENEMY_CHARACTER, 5))
	pass
