import random
from utils import *
     
import random
from utils import *
     
class takashoAgent(Agent):    
     def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
          super().__init__(myName, myFunction, myOption, myClass, rating )
     def takasho002AI(self, game: GameWithLog, option=[], gameLog=[], debugLog=False):
         player = game.current_player
         min = 30
         while True:
              myCandidate = getCandidates(game)#実行できることがらをリストで取得
              if len(myCandidate)>0:
                  sum = sumFieldCardatc(game)
                  print(sum)
                  
                  for choice in myCandidate:
                       tmpGame = copy.deepcopy(game)
                       #if choice.type==BlockType.PLAY and choice.card.type==CardType.MINION:
                       executeAction(tmpGame,choice,debugLog=False)
                       postAction(player)
                       choice.score = game.current_player.opponent.hero.health
                       choice.minionHelth = game.current_player.opponent.field.card.atk
                  myChoice = None
                  
                  if sum >= 7: #相手の盤面の打点計算
                      print("やばいわよ")
                      #打点を抑えるようにプレイ
                      for choice in myCandidate:
                        if sum > choice.minionHelth:
                            myChoice = choice

                  else:
                    for choice in myCandidate:
                        if min >= choice.score:
                            min = choice.score
                            myChoice = choice
                  executeAction(game,myChoice,debugLog=True)
                  postAction(player)
                  if game.current_player.opponent.hero.health ==0:
                      print("かち！")
                      return

              else:
                   return
     def sumFieldCardatc(game):
         for card in game.current_player.opponent.field:
             sum = sum + card.atk
         return sum