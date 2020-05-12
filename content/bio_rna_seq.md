Title: RNA-seq解析
Date: 2019-09-19
Category: 生物学
Tags: 生物学, 解説, 授業まとめ
Slug: bio_rna_seq.md
Authors: Naoto Yamaguchi
Summary: RNA-seq解析の勉強
Status: draft

# 動機
RNA-seqをやる機会があったため

# 参考
鈴木穣（編）『NGSアプリケーション RNA-Seq 実験ハンドブック』

# RNA-seqとは

# 種類
## シークエンス条件による分類
* タグ数をカウントするもの
* 配列を決定するもの

## 解析対象分子種による分類

# RNA-seqの情報解析
## ワークフロー
ゲノム上にマッピング。このマッピングはスプライシングされた転写産物を参照ゲノム配列上に対して行うため、
その際、イントロンによるギャップの考慮が必要。



FASTQファイル ... 塩基配列と塩基精度がセットになったもの。HiSeq2500の付属ソフトウェアであるCASAVAが用いられ、BCLファイルからFASTQファイルが生成される。DBの登録などにはFASTQファイルを用いることが多い。

FASTQとGTF(標準遺伝子モデル)を入力として、TopHatがFASTQの結果を、参照ゲノム配列にマッピングを行いBAMファイルとして結果が出力される。
BAMファイルはバイナリファイルであるが、SAMtoolsを用いて内容を閲覧したりSAMファイルというテキストファイルに変換することが可能。

発言量の算出
Cufflinksというソフトウェアを用いる。BAMファイルを入力ファイルとして、その遺伝子のエキソン上にマッピングされるタグ数を数える。遺伝子上のタグ数を、そうタグ数及び遺伝子長で補正した、RPKM/FPKM(reads fragments per kilobase exon per million mapped reads)という単位により発現量を見積もる。
Cufflinksではスプライシングイアソフォームごとの発現量の算出も可能。複数の状態間での発現量比較には、CuffDiffやDESeqを用いる。

融合遺伝子の探索もできる。
可視化は、IGVやUCSC Genome Browserを用いておこなえる。

## 実際
* Homebrew, wgetのインストール
* Samtools, Bowtie2, Tophat, Cufflinksのインストール
    * `brew install homebrew/science/tophat`で`Error: homebrew/science was deprecated. This tap is now empty as all its formulae were migrated.`というエラー
    * [こちら](https://bi.biopapyrus.jp/rnaseq/mapping/tophat/)を参考にして、[sourceforge](http://sourceforge.net/projects/bowtie-bio/files/bowtie2/)からlatest version(今回は2.3.5.1)をダウンロード
        * homebrewでできた    
    * 同様に、[Samtools](https://github.com/samtools/samtools/releases/) は、[sourceforge](https://sourceforge.net/projects/samtools/files/samtools/)からlatest version(今回は1.9)をダウンロード
    * TopHat
    * [Cufflinks](https://github.com/cole-trapnell-lab/cufflinks)
        * [ここ](http://cole-trapnell-lab.github.io/cufflinks/install/)からプリコンパイルをダウンロードし、 `/usr/local/bin` に入れた
* これらのツールに加え
    * シークエンスデータ
    * ヒトiGenomeファイル
    * リボソームRNAの情報
    * IGVソフトウェアを利用
...?
とかやってたら、TopHat, Cufflinksの利用は推奨されたないとのこと...

```
HISAT, StringTie, Ballgown
ゲノムへのマッピングと発現量定量には TopHat+Cufflinks が有名ですが、すでに後継のパイプライン HISAT, StringTie, Ballgown が発表されています。

HISAT2はRNA-seqのリードをゲノムにマッピングするソフトウェアです。StringTieはRNA-seqのリードをリファレンスゲノムにマッピングしたあとでアセンブリをおこなうソフトウェアです。Cufflinksより性能がよいと報告されています。アセンブリを行わず、発現量推定だけを行うこともできます。Ballgownは発現変動解析をおこなうソフトウェアです。

* [HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml)
* [StringTie](https://ccb.jhu.edu/software/stringtie/index.shtml)
* [Ballgown](http://bioconductor.org/packages/release/bioc/html/ballgown.html)
* HISAT, StringTie, Ballgown を用いた [RNA-seqデータ解析のプロトコル論文](https://www.nature.com/articles/nprot.2016.095)
```
[詳しい追試はこちら](http://rnakato.hatenablog.jp/entry/2018/11/09/165200)

結局入れたのは

* HiSat2
[HISAT2 使い方 インストールとマッピング バイオインフォ道場](http://bioinfo-dojo.net/2018/02/20/hisat2-install_mapping/)
```
# hisat2 ダウンロード
$ wget ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.1.0-Linux_x86_64.zip .

# hisat2 解凍
$ unzip hisat2-2.1.0-Linux_x86_64.zip 

# 展開チェック
$ ls
hisat2-2.1.0

# パスを通す（例ではホームディレクトリを活用）
$ sudo ln -s ~/hisat2-2.1.0/hisat2 /usr/local/bin/

# 起動チェック
$ hisat2 -h
HISAT2 version 2.1.0 by Daehwan Kim (infphilo@gmail.com, www.ccb.jhu.edu/people/infphilo)
Usage: 
  hisat2 [options]* -x  {-1  -2  | -U  | --sra-acc } [-S ]
```





# RSEM, STAR
## STARのインストールでエラー
[こちら](http://rnakato.hatenablog.jp/entry/2018/12/26/142038)を参考に

```
$ wget https://github.com/alexdobin/STAR/archive/2.6.1d.tar.gz
$ tar -xzf 2.6.1d.tar.gz
$ cd STAR-2.6.1d/source
$ make STAR              # Linuxの場合
$ make STARforMacStatic  # Macの場合 
```
Macで`$ make STARforMacStatic`を実行したところ、
`clang: error: unsupported option '-fopenmp'`というエラーが出ました。
これは、make コマンドを実行した際のエラー内容が、clangを参照したときに発生するもので、-fopenmpというオプションをclangがサポートしてないために発生している。
似たような話は[こちら](https://qiita.com/ligerbolt/items/6e27c882838fdcc1a490)のコメント
コピーを忘れてしまったが、このmakeコマンド実行の際に、c++コマンドを実行しており、`which c++`で調べると、`/usr/bin/c++`であり、そのシンボリックリンクを`ls -la /usr/bin/c++`で調べると、確かに`clang++`であった。
そこで、c++コマンドを実行した時に、clangではなく`/usr/local/bin`にある`c++-4.9`を参照するようにシンボリックリンクを貼り直しました。
`ln -f -n -s /usr/local/bin/c++-4.9 /usr/bin/c++`
[これ]を参考に(https://tech.withsin.net/2015/09/18/directory-symboliclink/)

c++-4.9はg++-4.9やgcc-4.9を以前homebrewでインストールした時に入っていました。
話としては[この辺](https://qiita.com/Hiroki11x/items/261612c142da176bbba5)が近い

シンボリックリンクが貼られているかの確認は、
`ls -la /usr/local/bin/gcc`
などで確認できる。
gcc -v, g++ -vで確認

また、gcc -v を実行した際の出力結果が、下記のようにclangのversion情報となっているため



## RSEMのtutorial
データの取得
作業ディレクトリ`bowtie2-rsem/ref`で
Ensembleでマウスゲノムを取得
`wget ftp://ftp.ensembl.org/pub/release-82/fasta/mus_musculus/dna/Mus_musculus.GRCm38.dna.toplevel.fa.gz`
GTFファイルも取得
`wget ftp://ftp.ensembl.org/pub/release-82/gtf/mus_musculus/Mus_musculus.GRCm38.82.chr.gtf.gz`

```
gunzip ref/Mus_musculus.GRCm38.dna.toplevel.fa.gz
gunzip ref/Mus_musculus.GRCm38.82.chr.gtf.gz
rsem-prepare-reference --gtf ref/Mus_musculus.GRCm38.82.chr.gtf \
					     --bowtie2 --bowtie2-path /usr/local/bin/bowtie2 \
   				     ref/Mus_musculus.GRCm38.dna.toplevel.fa ref/mouse_ref
                        ```

[bowtie2-rsem] rsem-calculate-expression -p 8 --paired-end \                               18:00:05
                                        --bowtie2 --bowtie2-path bowtie2 \
                                        --estimate-rspd \
                                        --append-names \
                                        --output-genome-bam \
                                        data/SRR937564_1.fastq data/SRR937564_2.fastq \
                                        ref/mouse_ref exp/LPS_6h
bowtie2/bowtie2 -q --phred33 --sensitive --dpad 0 --gbar 99999999 --mp 1,1 --np 1 --score-min L,0,-0.1 -I 1 -X 1000 --no-mixed --no-discordant -p 8 -k 200 -x ref/mouse_ref -1 data/SRR937564_1.fastq -2 data/SRR937564_2.fastq | samtools view -S -b -o exp/LPS_6h.temp/LPS_6h.bam -
sh: bowtie2/bowtie2: No such file or directory

rsem-parse-alignments ref/mouse_ref exp/LPS_6h.temp/LPS_6h exp/LPS_6h.stat/LPS_6h exp/LPS_6h.temp/LPS_6h.bam 3 -tag XM
The SAM/BAM file declares less than one reference sequence!
"rsem-parse-alignments ref/mouse_ref exp/LPS_6h.temp/LPS_6h exp/LPS_6h.stat/LPS_6h exp/LPS_6h.temp/LPS_6h.bam 3 -tag XM" failed! Plase check if you provide correct parameters/options for the pipeline!

これで動かず...

ソフトウェアがbowtie2なのがいけない?


諦めてkallistoへ
```
brew install kallisto
```

kallisto indexにやたら時間かかる...
他のサーバーで試してみる


## AWSでやり直して
condaでやった
`https://pythonoum.wordpress.com/2018/10/16/linux%E3%81%A7%E3%81%AEbioinformatics%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89_01/`


quant
1hくらいかかった気がする...

AWSでRstudio Server使おうとした
ポート8787を解放しないとダメっぽい
https://www.randpy.tokyo/entry/2017/06/06/083000

RNA-seqのそもそもについて
データが正しいか確認


abundance.tsvでた
Rで解析
condaで入れたけど、sleuthのinstallできなかった。source()みたいなやつ
これは古いらしい
http://www.bioconductor.org/install/

rはcondaでも入ってるけど、brewで入れて、シンボリックリンク貼ってる状態
```
[kallisto] ls -la /usr/local/bin/R                                                         20:25:29
lrwxr-xr-x  1 naoto  admin  25  9 23 20:20 /usr/local/bin/R -> ../Cellar/r/3.6.1_1/bin/R
```
Rを3.6にした
これでBioconductorインストールできたと思ったら、
sleuthはR3.6では使えませんだとさ
自分のpcどうなってるかもうわからん...
そこでdocker使って、version変えてみる
https://github.com/rocker-org/rocker/wiki/Using-the-RStudio-image

https://hub.docker.com/r/rocker/rstudio/

```
[shims] docker run -it rocker/rstudio                                                      21:04:06
[s6-init] making user provided files available at /var/run/s6/etc...exited 0.
[s6-init] ensuring user provided files have correct perms...exited 0.
[fix-attrs.d] applying ownership & permissions fixes...
[fix-attrs.d] done.
[cont-init.d] executing container initialization scripts...
[cont-init.d] add: executing...
Nothing additional to add
[cont-init.d] add: exited 0.
[cont-init.d] userconf: executing...


ERROR: You must set a unique PASSWORD (not 'rstudio') first! e.g. run with:
docker run -e PASSWORD=<YOUR_PASS> -p 8787:8787 rocker/rstudio


[cont-init.d] userconf: exited 1.
[cont-finish.d] executing container finish scripts...
[cont-finish.d] done.
[s6-finish] syncing disks.
[s6-finish] sending all processes the TERM signal.
[s6-finish] sending all processes the KILL signal and exiting.
```
Rのversion3.6やった






## 流れ
.fastq = シークエンスファイル
.bam = マッピングファイル
.FPKM_tracking = 発現量情報ファイル















## ソフトウェア概観
### マッピング
* TopHat/TopHat2
* HISAT2
* STAR
* GSNAP

### 遺伝子発現解析
* Cufflinks/CuffDiff
* DESeq

### アセンブル
### 融合遺伝子探索
### 可視化ツール
* IGV
* UCSC Genome Browser