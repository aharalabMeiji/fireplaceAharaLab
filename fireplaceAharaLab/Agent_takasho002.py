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
         sum = 0
         enemyFace = 0
         while True:
              myCandidate = getCandidates(game)#実行できることがらをリストで取得
              if len(myCandidate)>0:
                  sum = self.sumFieldCardatc(game)
                 # print(sum)
                  
                  for choice in myCandidate:
                       tmpGame = copy.deepcopy(game)
                       #if choice.type==BlockType.PLAY and choice.card.type==CardType.MINION:
                       executeAction(tmpGame,choice,debugLog=False)
                       postAction(player)
                       choice.score = [game.current_player.opponent.hero.health,self.sumFieldCardatc(tmpGame)]
                       #choice.minionHealth = self.sumFieldCardatc(tmpGame)
                  myChoice = None
                  #print(choice.score[0])
                  if game.current_player.opponent.hero.health <=0:
                      if(game.turn %2 == 0):
                          print("先行勝ち!")
                      else:
                          print("後手勝ち！")
                      return                  
                  #if sum >= 10: #相手の盤面の打点計算
                   #   print("やばいわよ")
                      #打点を抑えるようにプレイ
                    #  for choice in myCandidate:
                     #   if sum > choice.score[1]:
                      #      myChoice = choice
                  else:
                    for choice in myCandidate:
                        if min > choice.score[enemyFace]:
                            min = choice.score[enemyFace]
                            myChoice = choice
                    if myChoice == None: ##相手の顔を減らせないとき
                        myChoice = random.choice(myCandidate)
                  executeAction(game,myChoice,debugLog=True)
                  postAction(player)
              else:
                   return
     def sumFieldCardatc(self,game : GameWithLog):
         sum = 0
         for card in game.current_player.opponent.field:
             sum = sum + card.atk
         return sum


class candidateKeisho(Candidate):
    def __init__(self, card, card2=None, type=BlockType.PLAY, target=None, turn=None):
        super().__init__(self, card, card2, type, target, turn)
        minionAtc = 0

