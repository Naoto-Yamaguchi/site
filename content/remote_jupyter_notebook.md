Title: Jupyter Notebookをリモートサーバーで利用し、ローカルのブラウザで確認する"
Date: 2019-02-20
Category: Python
Tags: Python SSh
Slug: remote_jupyternotebook
Authors: Naoto Yamaguchi
Summary: Jupyter Notebook利用の備忘録<img src="https://paper-attachments.dropbox.com/s_8FAC27AC251845FE76C63F0EAF156DF8B3F4D3C17D70B16D9D9AEE81A162B247_1559630601567_jupyter.png">

### 動機

データ分析で大量のデータを扱う際、ローカルの  コンピューターではなく  リモートサーバーにダウンロードなどを行うことがありました。そのデータを分析するために、Jupyter Notebook を利用したかったのですが、 ローカルで使えるだけではデータを参照できないので、データがおかれているリモートサーバーで  使えるようにする必要がありました。やりたいことは以下のような感じです。
http://starpentagon.net/analytics/remote_jupyter_notebook/

### 参考

サムネイル画像は[こちら](https://en.wikipedia.org/wiki/Project_Jupyter)より引用

### Step1: リモートサーバーに Jupyter Notebook をインストール

リモートサーバーにおける権限などに注意する必要があります。おそらく

```
$ pip install jupyter --user
```

で十分ですが、自分は anaconda をインストールしました。このページの Linux でのインストール方法を参考にしました。
https://qiita.com/t2y/items/2a3eb58103e85d8064b6
https://stackoverflow.com/questions/38080407/how-can-i-install-the-latest-anaconda-with-wget

```
$ wget http://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
$ bash Anaconda3-4.2.0-Linux-x86_64.sh
#PATHの設定
~/.bash_profileに
export PATH=/home/yamaguchi/anaconda3/bin:PATH
#を追記
$ source ~/.bash_profile
```

### Step2: サーバー側の設定

基本的にこちらを参考にしました。
http://starpentagon.net/analytics/remote_jupyter_notebook/

```
$ ipython3
> from notebook.auth import passwd
> passwd()
# ここでパスワードを入力し、出力されたsha1値をコピー
> quit()
```

~/.jupyter/jupyter_notebook_config.py を変更。なければ、

```
$ jupyter notebook --generate-config
```

~/.jupyter/jupyter_notebook_config.py を開き

```
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.password = u'sha1:XXXXXXX' # 先ほど記録したsha1値を記載
```

以下のように設定。

これにて設定終了。 自分の場合、一旦 ssh 接続を切って、

```
ssh -L 8888:localhost:8888 <username>@<ip address>
```

で再度リモートサーバーに接続し、

```
jupyter notebook
```

を実行し、起動。

クライアント側のブラウザから、
`http://localhost:8888`にアクセス。jupyter notebook ぽい画面が表示され、sha1 値  生成時に入力したパスワード入力すると、認証が成功し、クライアント側のブラウザからリモートサーバー上で動く Jupyter Notebook を利用できます。

### 参考

https://qiita.com/Miggy/items/5466a2c1e968602f3ebe
