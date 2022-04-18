from fireplace.game import Game
from fireplace.deepcopy import deepcopy_game
from fireplace.actions import BeginTurn, BG_RegularAttack, Deaths, BeginBattle
import random
from hearthstone.enums import PlayState

class BG_Battle(Game):
	def __init__(self, bars):
		#エージェントのデータからバトルフィールドの設定をする。
		self.game1=deepcopy_game(bars[0], bars[0].controller, 0)
		self.game2=deepcopy_game(bars[1], bars[1].controller, 0)
		self.player1 = self.game1.player1
		self.player2 = self.game2.player1
		super().__init__([self.player1, self.player2])
		pass
	def battle(self):
		#プレイヤーのopponentを設定
		self.player1.opponent=self.player2
		self.player2.opponent=self.player1
		#先攻後攻を決める（枚数の多いほうが先攻、同数ならばランダム）
		#self.first #先攻 #self.second #後攻
		if len(self.player1.field)>len(self.player2.field):
			self.first = self.player1
			self.second = self.player2
		elif len(self.player1.field)<len(self.player2.field):
			self.first = self.player2
			self.second = self.player1
		else:
			self.first = random.choice([self.player1, self.player2])
			self.second = self.first.opponent
		#playstateをPLAYINGにする。格段の意味は見いだせない
		for player in self.players:
			player.playstate = PlayState.PLAYING
		#turn_beginを実行（先攻、後攻の順）（イベントを発生させるため）
		BeginBattle(self.first).trigger(self)## trigger主はplayer
		BeginBattle(self.second).trigger(self)## trigger主はplayer
		#パラメータ設定
		self.current_player=self.first
		self.first.AttackIndex=0
		self.second.AttackIndex=0
		#ループ開始
		while True:
			#フィールドの表示
			self.printField()
			#一方が全滅したかどうかの判断（もし全滅していたら終戦処理へ）
			if len(self.first.field)==0 or len(self.second.field)==0:
				break
			#攻撃者
			attacker = self.current_player.field[self.current_player.AttackIndex]
			#被攻撃者
			taunts=[]
			for card in self.current_player.opponent.field:
				if card.taunt:
					taunts.append[card]
			if len(taunts)>0:
				defenders = taunts
			else:
				defenders = self.current_player.opponent.field
			defender=random.choice(defenders)
			#攻撃
			print("%s(%s) -> %s(%s) : "%(attacker, attacker.controller, defender, defender.controller))
			BG_RegularAttack(attacker, defender).trigger(attacker.controller)
			#死者が出る場合にその処理(deathrattle)
			Deaths().trigger(self)
			#攻撃ターンの交代(freezeとone_turn_effectはない)
			self.current_player.AttackIndex+=1
			if self.current_player.AttackIndex>= len(self.current_player.field):
				self.current_player.AttackIndex=0
			self.current_player = self.current_player.opponent
			if self.current_player.AttackIndex>= len(self.current_player.field):
				self.current_player.AttackIndex=0
			pass
		#バトル終了
		#self.state = State.COMPLETE
		#self.manager.step(self.next_step, Step.FINAL_WRAPUP)
		#self.manager.step(self.next_step, Step.FINAL_GAMEOVER)
		#self.manager.step(self.next_step)
		#引き分け
		if len(self.first.field)==0 and len(self.second.field)==0:
			return 0,0 #続行
		elif len(self.player1.field)==0:
			# 「セカンドのフィールドの残りカードのtech_levelの総和＋セカンドのTier」を求める
			damage = self.player2.Tier
			for card in self.player2.field:
				if hasattr(card,'tech_level'):
					damage += card.tech_level
				else:
					damage += card.cost# or 1?
			# ダメージを返す
			return damage, 0
		else:#if len(self.player2.field)==0:
			# 「ファーストのフィールドの残りカードのtech_levelの総和＋ファーストのTier」を求める
			damage = self.player1.Tier
			for card in self.player1.field:
				if hasattr(card,'tech_level'):
					damage += card.tech_level
				else:
					damage += card.cost# or 1?
			# ダメージを返す
			return 0, damage
		pass

	def printField(self):
		print("--------%s--------"%self.first.name)
		for card in self.first.field:
			print("%s:%s"%(self.first.name, self.card_stats(card)))
		print("--------%s--------"%self.second.name)
		for card in self.second.field:
			print("%s:%s"%(self.second.name, self.card_stats(card)))
		print("--------[over]--------")
	
	def card_stats(self, card):
		ret = ' %s'%(card)
		ret += '(%d/%d)'%(card.atk,card.health)
		if card.cant_play:
			ret += "(can't play)"
		if card.frozen:
			ret += "(frozen)"
		if card.taunt:
			ret += "(taunt)"
		if card.divine_shield:
			ret += "(divine_shield)"
		if card.windfury:
			ret += "(windfury)"
		if card.reborn:
			ret += "(reborn)"
		return ret


