Title: MacOSで使っていたGCCはGCCではなかった話（他のコマンドもまた然り）
Date: 2019-06-24
Category: Programming
Tags: Programming, C
Slug: gcc_on_mac
Authors: Naoto Yamaguchi
Summary: Macに勝手に騙されてました。
Status: draft

# 動機
あるプログラムの実行時間を計測するには、timeコマンドが良いということで、`time 実行ファイル名`のような形で、実行時間計測をおこなっていたのですが、出てくる表示が、timeコマンドの使い方を説明している記事とは異なることに気がつきました。具体的には以下の通りです。
