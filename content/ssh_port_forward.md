Title: SSHのポートフォワード（トンネリング）とは？
Date: 2019-03-31
Category: SSH
Tags: SSH, portforward
Slug: ssh_port_forward
Authors: Naoto Yamaguchi
Summary: SSHポートフォーワードとは（未完）<br><img src="https://paper-attachments.dropbox.com/s_8FAC27AC251845FE76C63F0EAF156DF8B3F4D3C17D70B16D9D9AEE81A162B247_1559630562939_port_forwarding.png">

### 動機

SSH ポートフォワードを使っていた時に、SCP でファイルを送信したかったため。

### 参考

サムネイル画像は[こちら](https://cookbook.fortinet.com/port-forwarding-60/)より引用

[SSH ポートフォワード（トンネリング）を使って、遠隔地から LAN 内のコンピュータにログインする](https://www.clear-code.com/blog/2014/9/12.html)
[Turbolinux 11 Server: ユーザーガイド 第 21 章 SSH（Secure SHell）サーバー](https://www.turbolinux.co.jp/products/server/11s/user_guide/x9016.html)

### SSH ポートフォワードとは？

> ある特定のコンピュータの特定のポート番号に対して送られる通信内容を、別のコンピュータの特定のポート番号への接続として転送すること。インターネットと LAN の間でルーターは日常的にこれをこなしているが、SSH のポートフォワード機能を使うと、様々な設定でポートフォワードをすることができる。

今回は、ある LAN の中にある PC から別の LAN の中にある PC に SSH 接続しており、そのコンピュータ間でファイル転送をおこないたいというモチベーションがありました。

* インターネット上の中継サーバを使う方法
* LAN 内の中継サーバを使う方法

の 2 通りがあります。

### 実際にやってみた

すみません、まとめたら載せます。

<!-- zsh: no matches found
[ss](http://d.hatena.ne.jp/eitya/20110707/1310023383)
[]https://shirusu-ni-tarazu.hatenablog.jp/entry/2013/01/18/034233
全然関係ないところでエラー

[](https://qiita.com/kyrya/items/121fc54ae4c9c10c0e8b)
を参考に
`scp -o 'ProxyCommand ssh aca10555ym@as.abci.ai nc %h %p' lstm_human_antigen.ipynb aca10555ym@es:/groups2/gca50068/yamaguchi`
やってみたけど、
sh_exchange_identification ってエラー
[](https://qiita.com/uutarou10/items/f8391965adc6b4c312d1)
そもそも IP アドレスが違う説確認する

tmux ってなに

abci-gate した状態で
[~] scp -r -P 10022 [送りたいディレクトリ][usrname]@localhost:[送り先のディレクトリ]
でできた -->
