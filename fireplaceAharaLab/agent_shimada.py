import random
from utils import *
     
class ShimadaAgent(Agent):    
     def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000, mulliganStrategy=None ):
          super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
     def ShimadaAI(self, game: Game, option=[], gameLog=[], debugLog=False):
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
     def ShimadaMulligan(self, choiceCards):
         # make cost 1 cards left
         print("%s mulligan turn"%(self.name))
         cards_to_mulligan = []
         for num in range(len(choiceCards)):
             if choiceCards[num].cost > 1:
                cards_to_mulligan.append(choiceCards[num])
         return cards_to_mulligan
            


