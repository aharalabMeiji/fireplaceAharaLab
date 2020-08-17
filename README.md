# fireplaceAharaLab

This is an application on a AI-platform fireplace for Hearthstone.
This needs python 3.8, hearthstone 5.23.4, and fireplace 0.1.

# 日本語による説明

* python 3.8 for x64 をインストールします。

* pip install hearthstone でhearthstone と hearthstone-dataをインストールします。

* fireplaceをgithubからダウンロードして、cmdでそのフォルダを開き、pip install . を実行します。\
（ただし、pipにパスが通っていることが必要。通常であれば、\
C:\Users\----\AppData\Local\Programs\Python\Python38\Scripts\
にパスが通っていれば大丈夫。）

* fireplaceAharaをダウンロードして、VisualStudio用のプロジェクトからstart.pyを実行すれば動きます。

* 作業内を変更したい場合には、start.pyを編集してください。。

# マストではないが、チューンアップしておいたほうがよい項目

* カード名を日本語表示にする方法

    #fireplace.cards.\_\_init\_\_.py line 95\
    def initialize(self, locale="jaJP"):

* ゲンゾーまわりのトラブル（3枚カードを引かせる、という動作中に、playerとcardの混同が起きる。現バージョンではInvalidPlayフラグ対象。）

    #fireplace.actions.py ll.900-905\
        def do(self, source, target, amount):\

           if target not in target.game.players:\
                #raise InvalidAction("%r is not a player" % target)\
                target = target.controller#add this line\
            difference = max(0, amount - len(target.hand))

* fireplace.actions.py のline 1047まわり、MorphのtargetがNoneで呼び出されることがまれにある。（[魔力喰い]でなぜか起こる）対応不明
* ログ表示をやめる方法
>	#fireplace.logging.py line 18\
>		#logger.addHandler(ch)

# start.py周りの説明
>def main():\
>	from fireplace import cards\
>	cards.db.initialize()\
>	setup_play_game(createNew=1)#リーグ戦を行う。\
>	#set_up_one_game_with_human()#人vsCOM\
>	#investigate_card_pair()\
>	#find_card_pair(1)
* setup_play_game()#リーグ戦を行う（準備として、test_data--.csvを準備する必要がある。--は二桁の数字で、対象とするカードクラスの番号（3:HUNTER,4:MAGE,...）を二つ並べていれる）
createNew=1：新規プレーヤーを追加する\
createMorph=1：新規プレーヤー（現存プレーヤーを少し変更したもの）を追加する\
player1isNew=1:プレーヤ1として、最後に追加したプレーヤを指名する\
player2isNew=1:プレーヤ2として、最後に追加したプレーヤを指名する
* set_up_one_game_with_human()#人vs.COMで対戦を行う
* investigate_card_pair()#特定の2枚のカードのシナジーを調べる
* find_card_pair(1)#漠然とシナジーのあるカードを探索する（(1)は結果のみの表示のためのフラグ
