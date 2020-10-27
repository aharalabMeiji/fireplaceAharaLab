import random
from utils import *
     
class takasho002(Agent):    
     def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
          super().__init__(myName, myFunction, myOption, myClass, rating )
     def agent_takasho002(self, game: Game, option=[], gameLog=[], debugLog=False):
         player = game.current_player
         while True:
              myCandidate = getCandidates(game)#実行できることがらをリストで取得
              if len(myCandidate)>0:
                   myChoice = random.choice(myCandidate)#ランダムに一つ選ぶ
                   if myChoice.type ==ExceptionPlay.TURNEND:#何もしないを選択したとき
                       return
                   executeAction(game, myChoice, debugLog=debugLog)#選択したものを実行
                   postAction(player)#後処理
              else:
                   return