Title: アセンブリメモ
Date: 2019-06-06
Category: 生物学
Tags: DIY, Shojinmeat, cell-based-meat
Slug: culture medium
Authors: Naoto Yamaguchi
Summary: 培養液について調べてみた。
Status: draft


# 動機
実際に培養を始めるにあたって、培養液についてきちんとしっておかないとと思ったので。


# 参考


# レジスタ
* rsp: スタックポインタ
    * スタックトップのメモリアドレス
    * push命令でデクリメント、poo命令でインクリメントされる。
* rbp: ベースポインタ
    * 関数内においてスタック領域を扱う処理の基準となるメモリアドレス。
関数の先頭で次の処理を行う。
1. 呼び出し元のrbpをスタックにpushする
2. rspをrbpに代入する

関数内部では、rbpを基準にしてスタック領域を扱う。

関数の最後で次の処理を行う。
1. rbpをrspに代入
2. 


グリーンダカラの成分

# 今後
RedBullでもできる？
