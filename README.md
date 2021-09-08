## fireplaceAharaLab

This is an application on a AI-platform fireplace for Hearthstone.
This needs python 3.8, hearthstone 5.23.4, and fireplace 0.1.

## 日本語によるwiki (wiki only in Japanese, sorry!)

https://github.com/aharalabMeiji/fireplaceAharaLab/wiki/

## インストールの仕方

https://github.com/aharalabMeiji/fireplaceAharaLab/wiki/%E3%81%AF%E3%81%98%E3%82%81%E3%81%8B%E3%81%9F (日本語)

## マストではないが、チューンアップしておいたほうがよい項目

* カード名を日本語表示にする方法

> fireplace.cardsフォルダのファイル\_\_init\_\_.py のline 95
>
>     def initialize(self, locale="jaJP"):
>

* ログ表示をやめる方法

> fireplaceフォルダのファイルlogging.py の　line 18あたり
>
>     #logger.addHandler(ch)

## start.pyの見方

https://github.com/aharalabMeiji/fireplaceAharaLab/wiki/start.py-%E3%81%AE%E8%A6%8B%E6%96%B9%E3%80%82
