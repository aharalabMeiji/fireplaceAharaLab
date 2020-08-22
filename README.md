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

    Human=Agent("Human",None,myClass=CardClass.MAGE)

着手できるものの中からランダムに選択する(”Standard"というプレーヤー名に、ランダムプレーヤーを張り付けています。）

    Random=Agent("Standard",None) # Classを指定しないとHUNTER

agent by MCTS (TBA)

agent by Q-learning (TBA)

agent by DQN (TBA)

+ オプションつきのオリジナルエージェントも呼び出すことができる

たとえば、agent_Standard.pyにStandardStep1(game, option, debugLog)という関数を準備すると、次の式で呼び出すことができる。\
myClassは省略可\
StandardStep1 のように、オプション付きのオリジナルエージェントも呼び出すことができる。

    from agent_Standard import StandardStep1
    weight=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    StandardPlayer=Agent("GhostCat", StandardStep1,myOption=weight, myClass=CardClass.WARRIOR)

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

+ StandardStep1のリーグ戦\

パラメータをcsvファイルに保存しておいて、そのエージェントたちを対戦させる。以下はオプション\
createNew=1：新規プレーヤーを追加する\
createMorph=1：新規プレーヤー（現存プレーヤーを少し変更したもの）を追加する\
player1isNew=1:プレーヤ1として、最後に追加したプレーヤを指名する\
player2isNew=1:プレーヤ2として、最後に追加したプレーヤを指名する

    #StandardStep1のリーグ戦
    from league_match import play_league
    play_league(matchNumber=1)

特定の2枚が並んでいるときのシナジーを確かめる関数（プレーヤーはMCTSのほうがいいようだ。）

    from card_pair import investigate_card_pair
    investigate_card_pair()

並んでデッキに入っているとシナジーが発生するような2枚を漠然と探す関数

    from card_pair import find_card_pair
    find_card_pair(1)
