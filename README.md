# fireplaceAharaLab

This is an application on a AI-platform fireplace for Hearthstone.
This needs python 3.8, hearthstone 5.23.4, and fireplace 0.1.

# 日本語によるwiki

https://github.com/aharalabMeiji/fireplaceAharaLab/wiki/

# 日本語による説明

* python 3.8 for x64 をインストールします。

* pip install hearthstone でhearthstone と hearthstone-dataをインストールします。

* fireplaceをgithubからダウンロードして、cmdでそのフォルダを開き、pip install . を実行します。\
>ただし、pipにパスが通っていることが必要。通常であれば、
>
>     C:\Users\----\AppData\Local\Programs\Python\Python38\Scripts\
>
>にパスが通っていれば大丈夫。

* fireplaceAharaをダウンロードして、VisualStudio用のプロジェクトからstart.pyを実行すれば動きます。

* 作業内を変更したい場合には、start.pyを編集してください。。

# マストではないが、チューンアップしておいたほうがよい項目

* カード名を日本語表示にする方法

> fireplace.cardsフォルダのファイル\_\_init\_\_.py のline 95
>
>     def initialize(self, locale="jaJP"):
>

* ログ表示をやめる方法

> fireplaceフォルダのファイルlogging.py の　line 18あたり
>
>     #logger.addHandler(ch)

# start.py周りの説明

    def main():

カード情報を読み込む

    from fireplace import cards
    cards.db.initialize()

+ 典型的なエージェント

人がキーボード入力できる(”Human"というプレーヤー名に、人プレーヤーを張り付けています。）

    Human=HumanAgent("Human1",HumanAgent.HumanInput,myClass=CardClass.HUNTER )

着手できるものの中からランダムに選択する(”Standard"というプレーヤー名に、ランダムプレーヤーを張り付けています。）

    Random=StandardAgent("Random",StandardAgent.StandardRandom, myClass=CardClass.HUNTER) 

MCTS によるターン内探索

    from agent_Miyaryo import MiyaryoAgent
    Miyaryo=MiyaryoAgent("Miyaryo",MiyaryoAgent.MiyaryoAI)

agent by Q-learning (TBA)

agent by DQN (TBA)

+ オプションつきのオリジナルエージェントも呼び出すことができる

たとえば、agent_Standard.pyにStandardStep1(game, option, debugLog)という関数を準備すると、次の式で呼び出すことができる。\
myClassは省略可\
StandardStep1 のように、オプション付きのオリジナルエージェントも呼び出すことができる。

    from agent_Standard import StandardStep1
    Vector=StandardVectorAgent("Vector",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8])

言葉で戦術を表して、それらを並べることによってエージェントを作る、という企画をやってみた。道具を豊富にすれば結構面白そう。というか、エージェントを作って、これより強くなければ仕方ないというかwww

    from agent_word_strategy import WS, agent_word_strategy
	WSplayer = Agent("WS", agent_word_strategy,\
		myOption=[WS.ミニョンで敵ヒーローの体力を削る, WS.呪文を使えるなら呪文, WS.ランダムにプレー],\
		myClass=CardClass.PRIEST)


ゲームを呼び出す関数。gameNumber回ゲームをする１セットを呼び出す。\
Human, Randomのところにエージェントの変数を入れればよい。\
プレーの内容を表示させたいときにはdebugLog=Tureにする

    #ゲームプレイ
    play_set_of_games(Human, Random, gameNumber=1, debugLog=False) 

+ 
