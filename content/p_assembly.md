Title: アセンブリメモ
Date: 2019-06-06
Category: プログラミング
Tags: アセンブリ
Slug: assembly
Authors: Naoto Yamaguchi
Summary: アセンブリメモ
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





# C++の標準ライブラリのdebugのための環境構築
[やり方](https://doss.eidos.ic.i.u-tokyo.ac.jp/html/gdb_step_into_libraries.html)

https://superuser.com/questions/159310/bash-line-7-dpkg-command-not-found-said-centos

These steps worked for me on CentOS 7:

Install epel using the following command: sudo yum -y install epel-release
Refresh repo by typing the following commad: sudo yum repolist
Install the dpkg rpm packages: sudo yum install dpkg-devel dpkg-dev
For more information: http://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/



```
実行ファイルを実行した時に使うであろう、ファイルを表示
$ ldd 04

あるファイルを提供しているパッケージ名を表示
$ dpkg -S /lib/x86_64-linux-gnu/libc.so.6
やったけど、
dpkg-query: no path found matching pattern

見つからないのは、そのパッケージ自体がインストールされていないのが原因か。
え、じゃあcのファイルはどうしてる？
```

インストール
[Stack Overflow](https://superuser.com/questions/159310/bash-line-7-dpkg-command-not-found-said-centos)
1. Install epel using the following command: sudo yum -y install epel-release
2. Refresh repo by typing the following commad: sudo yum repolist
3. Install the dpkg rpm packages: sudo yum install dpkg-devel dpkg-dev


ヘッダーファイルは、`.user/include/stdio.h`から見られる。
https://qiita.com/DQNEO/items/4e5c2eca2761ec08b922

ヘッダーファイルの実態は、glibにある
https://qiita.com/kure/items/d88b5b81efe38ead0ea2


[自分がコンパイルしていないライブラリの中をGDBで追跡する](https://doss.eidos.ic.i.u-tokyo.ac.jp/html/gdb_step_into_libraries.html)

[assembly – gdbを使って逆アセンブルされたライブラリをデバッグする](https://codeday.me/jp/qa/20190307/327856.html)

[「Hello World！」の主役printf()の内部動作をデバッガGDBで追う (3/3)](https://www.atmarkit.co.jp/ait/articles/1703/01/news167_3.html)

[x86-64プロセッサのスタックを理解する](https://qiita.com/tobira-code/items/75d3034aed8bb9828981)

`I get “dpkg-query: no path found matching pattern” How to solve this?
`
これは普通にパッケージがなかったから。