from fireplace.game import Game
from fireplace.deepcopy import deepcopy_game
from fireplace.actions import BeginTurn
import random
from hearthstone.enums import PlayState

class BG_Battle(Game):
	def __init__(self, bars):
		self.game1=deepcopy_game(bars[0], bars[0].current_player,0)
		self.game2=deepcopy_game(bars[1], bars[1].current_player,0)
		self.player1 = self.game1.current_player
		self.player2 = self.game2.current_player
		super().__init__([self.player1, self.player2])
		pass
	def battle(self):
		#エージェントのデータからバトルフィールドの設定をする。
		#for card in self.game1.current_player.field:
		#	card.controller = self.player1 #????
		#	card.zone = Zone.PLAY #????
		#for card in self.game2.current_player.field:
		#	card.controller = self.player2 #????
		#	card.zone = Zone.PLAYER #????
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
		BeginTurn(self.first).trigger(self)## trigger主はplayer?
		BeginTurn(self.second).trigger(self)
		#パラメータ設定
		self.current_player=self.first
		self.first.AttackIndex=0
		self.second.AttackIndex=0
		# フィールド表示
		self.printField()
		#ループ開始
		while True:
			#一方が全滅したかどうかの判断（もし全滅していたら終戦処理へ）
			if len(self.first.field)==0 or len(self.second.field)==0:
				break
			#攻撃者
			attacker = self.current_player.field[self.current_player]
			#被攻撃者
			taunts=[]
			for card in self.current_player.opponent.field:
				if card.taunt:
					taunts.append[card]
			if len(tanuts)>0:
				defenders = taunts
			else:
				defenders = self.current_player.opponent.field
			defender=random.choice(defenders)
			#攻撃
			RegularAttack(attacker, defender)
			#死者が出る場合にその処理(deathrattle)
			self.current_player.end_turn()
			#攻撃ターンの交代(freezeとone_turn_effectはない)
			self.current_player.AttackIndex+=1
			if self.current_player.AttackIndex>= len(self.current_player.field):
				self.current_player.AttackIndex=0
			self.current_player = self.current_player.opponent
			pass
		#引き分け
		if len(self.first.field)==0 and len(self.second.field)==0:
			return 0,0 #続行
		elif len(self.player1.field)==0:
			# 「セカンドのフィールドの残りカードのtech_levelの総和＋セカンドのTier」を求める
			damage = self.player2.Tier
			for card in self.player2.field:
				damage += card.tech_level
			# ダメージを返す
			return damage, 0
		else:#if len(self.player2.field)==0:
			# 「ファーストのフィールドの残りカードのtech_levelの総和＋ファーストのTier」を求める
			damage = self.player1.Tier
			for card in self.player1.field:
				damage += card.tech_level
			# ダメージを返す
			return 0, damage
		pass

	def printField(self):
		print("--------%s--------"%self.first.name)
		for card in self.first.field:
			print("%s:%s(%d/%d)"%(self.first.name, card, card.atk, card.health))
		print("--------%s--------"%self.second.name)
		for card in self.second.field:
			print("%s:%s(%d/%d)"%(self.second.name, card, card.atk, card.health))
		print("--------[over]--------")
	

