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

* ゲンゾーまわりのトラブル

> 3枚カードを引かせる、という動作中に、playerとcardの混同が起きる。現バージョンではInvalidPlayフラグ対象。\
> ファイルfireplace.actions.py のll.900-905あたり
>
>     def do(self, source, target, amount):
>         if target not in target.game.players:
>             #raise InvalidAction("%r is not a player" % target)
>             target = target.controller#add this line\
>         difference = max(0, amount - len(target.hand))

* fireplace.actions.py のline 1047まわり、MorphのtargetがNoneで呼び出されることがまれにある。（[魔力喰い]でなぜか起こる）対応不明

* ログ表示をやめる方法

> ファイルfireplace.logging.py の　line 18あたり
>
>     #logger.addHandler(ch)

# start.py周りの説明

    def main():

カード情報を読み込む

    from fireplace import cards
    cards.db.initialize()

典型的なエージェント

    from utils import Agent,play_set_of_games
    from hearthstone.enums import CardClass
    Human=Agent("Human",None,myClass=CardClass.MAGE)
    StandardRandom=Agent("Standard",None) # Classを指定しないとHUNTER
    Maya=Agent("Maya",None)

オプションつきのオリジナルエージェントも呼び出すことができる\
これはagent_Standard.pyにStandardStep1(game, option, debugLog)という関数を準備すると、次の式で呼び出すことができる。\
myClassは省略可\
StandardStep1 のように、オプション付きのオリジナルエージェントも呼び出すことができる。

    from agent_Standard import StandardStep1,StandardWeight
     StandardPlayer=Agent("GhostCat", StandardStep1,\
         myOption=StandardWeight([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),\
         myClass=CardClass.WARRIOR)

ゲームを呼び出す関数。gameNumber回ゲームをする１セットを呼び出す。\
Human, StandardRandomのところにエージェントの変数を入れればよい。\
プレーの内容を表示させたいときにはdebugLog=Tureにする

    #ゲームプレイ
    play_set_of_games(Human, StandardRandom, gameNumber=1, debugLog=True) 
StandardStep1のリーグ戦\
パラメータをcsvファイルに保存しておいて、そのエージェントたちを対戦させる。以下はオプション\
createNew=1：新規プレーヤーを追加する\
createMorph=1：新規プレーヤー（現存プレーヤーを少し変更したもの）を追加する\
player1isNew=1:プレーヤ1として、最後に追加したプレーヤを指名する\
player2isNew=1:プレーヤ2として、最後に追加したプレーヤを指名する

    #StandardStep1のリーグ戦
    from league_match import play_league
    play_league(matchNumber=1)

特定の2枚が並んでいるときのシナジーを確かめる関数（プレーヤーはMCTSのほうがいいようだ。）

    from card_pair import investigate_card_pair, find_card_pair
    investigate_card_pair()

並んでデッキに入っているとシナジーが発生するような2枚を漠然と探す関数

    find_card_pair(1)
