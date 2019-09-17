Title: Dockerでgdb環境構築
Date: 2019-06-05
Category: Docker
Tags: Docker, Programming
Slug: docker_gdbenv
Authors: Naoto Yamaguchi
Summary: Dockerでgdb環境を構築した備忘録<br><img src="https://paper-attachments.dropbox.com/s_8FAC27AC251845FE76C63F0EAF156DF8B3F4D3C17D70B16D9D9AEE81A162B247_1559697621860_docker.png">

# 動機対象

学校の課題で、dえC++と機械語の命令を比較しながら、メモリアクセスを少なくし、実行クロック数の少ない命令で目的の計算をすることでという速いアルゴリズムを設計できるようになろう！というものがありました。そこで、gdbデバッガで、機械語リストを出力させるということをやったのですが、Mac OS Sierraでは、gdbコード署名用の証明書の作成が必要とのことで、面倒そうでした。そこで、DockerでCentOSコンテナを立てて、gdb環境を整えることで、その代わりとすることにしました！

# 参考

[DockerをMacOSにinstall](https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81)
DockerでCentOSコンテナを立ち上げる

[CentOSにvimをインストール](https://qiita.com/muniere/items/0569d05d470c5d3dc51b)

[こちら](https://qiita.com/SOJO/items/9d6a65f3da941c49da36)も参考になる


この途中、`./configure`のところで、
`configure: error: no acceptable C compiler found in $PATH`
と出たが、これはgccがインストールされていなかったからだった。[以下](https://qiita.com/tmak_tsukamoto/items/b1c1f04d2a2ac527887c)に記載の同様のエラーだったため、gccのインストールで解決

[g++をyumでインストール](https://blog.sioyaki.com/entry/2017/04/10/101610)



gdb使ってみたら

    (gdb) b main
    Breakpoint 1 at 0x4007e8: file a.cpp, line 6.
    (gdb) run
    Starting program: /root/01/a.out
    warning: no loadable sections found in added symbol-file system-supplied DSO at 0x7ffff7ffa000
    
    Breakpoint 1, main () at a.cpp:6
    6                cout << 1 << endl;
    Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.212.el6_10.3.x86_64 libgcc-4.4.7-23.el6.x86_64 libstdc++-4.4.7-23.el6.x86_64
    

となったので、
[debuginfoのinstall](https://corgi-lab.com/linux/debug-with-gdb/)
[こちら](https://stackoverflow.com/questions/10389988/missing-separate-debuginfos-use-debuginfo-install-glibc-2-12-1-47-el6-2-9-i686)も、Missing separate debuginfosについて


# 目次
* DockerでCentOSコンテナを立ち上げる
* CentOSにgdbをインストール
* CentOSにvimをインストール
* CentOSにg++, debuginfoをインストール

# DockerでCentOSコンテナを立ち上げる 
* centosイメージのダウンロード
```
docker pull centos
```
* コンテナの起動
```
docker run -d --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" --name gdb centos:centos6.9 /bin/bash
```
-dオプションをつけてバックグラウンドで起動しないとうまくいかなかったので注意。

* 起動しているコンテナの確認
```
docker ps
```
停止しているものも確認したい場合は`-a`をつける

```
docker exec -it gdb /bin/bash
```
でbashを起動し、中に入れる

# CentOSにgdbをインストール
* gdbのインストール
```
yum install gdb
```
これでできた！と思って、ファイルを作ってデバッグしてみようと思ったらvimがインストールされてなかった。

#CentOSにvimをインストール
* vimをインストールするのに必要なパッケージが入っているかを以下のコマンドで確認。"list installed"はインストール済みのパッケージ一覧を表示。
```
$ yum list installed | grep mercurial
$ yum list installed | grep ncurses-devel
$ yum list installed | grep make         
$ yum list installed | grep gcc 
```
* インストールされていない場合はそれぞれインストール。
```
$ yum install mercurial
$ yum install ncurses-devel
$ yum install make
$ yum install gcc
```

* vimのインストール
```
$ cd /usr/local/src
$ sudo hg clone https://bitbucket.org/vim-mirror/vim vim
$ cd vim
$ ./configure --with-features=huge --enable-multibyte --disable-selinux
$ make
$ make install
```

必要があれば、[こちら](https://qiita.com/meio/items/08143eacd174ac0f7bd5)を参考に、日本語文字化けしないように、`~/.vimrc`の設定をしておきましょう。


# CentOSにg++, debuginfoをインストール
これで、vimが使えるので、C++ファイルの作成をしました。コンパイルしようとしたところ、g++をインストールしていないことに気がついたので、
```
$ yum install gcc-c++
```
でインストールし、
```
$ g++ -g a.cpp
```
-gオプションをつけて、gdbデバック用にコンパイル。
```
$ gdb ./a.out
```
で実行して、
```
$ b main
$ run
```
したところ、
```


    (gdb) b main
    Breakpoint 1 at 0x4007e8: file a.cpp, line 6.
    (gdb) run
    Starting program: /root/01/a.out
    warning: no loadable sections found in added symbol-file system-supplied DSO at 0x7ffff7ffa000
    
    Breakpoint 1, main () at a.cpp:6
    6                cout << 1 << endl;
    Missing separate debuginfos, use: debuginfo-install glibc-2.12-1.212.el6_10.3.x86_64 libgcc-4.4.7-23.el6.x86_64 libstdc++-4.4.7-23.el6.x86_64
    
```
となったので、
debuginfoをインストール
```
$ yum install yum-utils
$ debuginfo-installglibc-2.12-1.212.el6_10.3.x86_64 libgcc-4.4.7-23.el6.x86_64 libstdc++-4.4.7-23.el6.x86_64 
```

これで、gdbでデバッグできるようになりました！
参考にさせていただいた記事、ありがとうございます。

# Dockerコンテナをcommitしてみる
gdbという名前のコンテナで動かしていたものを、gdbenvというイメージとして保存します。
```
$ docker commit gdb gdbenv
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gdbenv              latest              c7e81afda91c        22 seconds ago      1.34GB
```
で、`gdbenv`という名前のイメージができていることを確認。
今後ここからイメージを起動して使うことができます。
Docker Hubにimageを公開すれば他の人も利用可能になります。公開にはDockerのアカウントを作成する必要があるみたいです。


# commitしたimageからコンテナを利用→エラー
* commitしたgdbenvというイメージから、gdbenvという名前のコンテナを起動して、bashを動かした。
```
$ docker run --name gdbenv -it -d gdbenv /bin/bash
$ docker exec -it gdbenv /bin/bash
```
これでgdbででバックしようとしたら、

```
(gdb) b main
Breakpoint 1 at 0x4007e8: file a.cpp, line 6.
(gdb) run
Starting program: /root/01/a.out
warning: Error disabling address space randomization: Operation not permitted
1
2
During startup program exited normally.
```

となったので、調べてみると、
gdbはシステムコールを使ってデバッグしているので、Dockerのコンテナを起動する際に、
* --cap-add=SYS_PTRACE: コンテナ内からのgdbによるptrace(2)を許可
* --security-opt="seccomp=unconfined": コンテナ内からのシステムコールの発行に制限を掛けない
の2つのオプションを追加する必要があるようです。（初めのCentOSのイメージからコンテナ起動するときに使ったコマンドと同じ。てっきり忘れていました。
[こちら](https://www.cyamax.com/entry/2018/02/09/070000)を参考にさせていただきました。

```
$ docker run --cap-add=SYS_PTRACE --security-opt="seccomp=unconfined" --name gdbenv -it -d gdbenv /bin/bash
$ docker exec -it gdbenv /bin/bash
```
このようすることで、うまくできました。


# このimagesをDocker Hubにpushする
[これ](https://qiita.com/umi/items/d4b5a68263ad0444693b)を参考に
[Docker Hub](https://hub.docker.com/explore/)にアカウント登録して、
そのアカウントで、ターミナルからログイン
```
$ docker login
Username: nyamaguchi
Password: 
```

pushしたいイメージに、`docker tag` コマンドで`<アカウント名><リポジトリ名>:<タグ名>` というタグを付加。
```
$ docker images                                                                          13:34:35
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gdbenv              latest              c7e81afda91c        27 hours ago        1.34GB
$ docker tag c7e81afda91c nyamaguchi/gdbenv:latest
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
gdbenv              latest              c7e81afda91c        27 hours ago        1.34GB
nyamaguchi/gdbenv   latest              c7e81afda91c        27 hours ago        1.34GB
```
これをリモートリポジトリへとpush
```
$ docker push nyamaguchi/gdbenv:latest
```

# Docker Hubからpullする
centosにgdb, vim, g++をinstallしたこのイメージを私がDocker Hubのパブリックリポジトリにpushしたので、`docker pull`で自分のローカル環境に持ってくることができます。
```
$ docker pull nyamaguchi/gdbenv
```
でこのimageでも利用可能になります。
ほぼ使い道ないかもしれませんが、もしよかったら使ってみてください。

`docker search gdbenv`で検索できるはずですが、なぜか見つかりませんでした。
