from fireplace import cards
from fireplace.game import Game

class BattleGrounds(Game):
	tavern=1

	
def BG_Agent(object):
	""" バトルグラウンドのエージェントのクラス
	エージェントを作るときはこのクラスを継承してください。"""
	def __init__(self, myName: str, myFunction, myOption: list, myClass: CardClass, rating ,E = 0, mulliganStrategy = None, choiceStrategy=None):
		self.name = myName
		self.func = myFunction
		self.option = myOption
		self.myClass = myClass
		self.rating = rating = 1500
		self.E = E 
		self.mulliganStrategy = mulliganStrategy
		self.choiceStrategy = choiceStrategy
		pass

	def __str__(self):
		return self.name

def BG_RandomAgent(BG_Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass
	def Random(self, game, option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		while loopCount<20:
			loopCount+=1
			myCandidate = getBGCandidates(game)
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				else:
					continue
			return ExceptionPlay.VALID


class BG_Game(Game):

	pass


def battlegroundMain():
	cards.db.BG_initialize()
	Agents=[
		BG_HumanAgent("Human1",BG_HumanAgent.HumanInput,choiceStrategy=HumanAgent.HumanInputChoice),
		BG_RandomAgent("Random1",BG_RandomAgent.Random)
		]
	# プールセットの決定
	# 無限ループ始まり
	# 組合せを決める
	# それぞれのムーブを行う。
	# 対戦
	# 対戦後処理
	# 無限ループ終わり
	pass




