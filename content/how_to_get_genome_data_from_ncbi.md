Title: NCBIからゲノムデータを取得する方法
Date: 2019-02-22
Category: Bioinfo
Tags: Bioinfo, 生物情報, NCBI
Slug: how_to_get_genome_data_from_ncbi
Authors: Naoto Yamaguchi
Summary: ゲノムデータ取得<br><img src="https://paper-attachments.dropbox.com/s_8FAC27AC251845FE76C63F0EAF156DF8B3F4D3C17D70B16D9D9AEE81A162B247_1559630593492_ncbi.png" width=150 height=150>

### 動機

NCBI からゲノムデータを取ってきたい時どうすれば良いかわからなかった。ftp を知らなかったけど、ダウンロードできました！

### 参考

サムネイル画像は[こちら](https://en.wikipedia.org/wiki/National_Center_for_Biotechnology_Information)より引用

### Step1: 取得したいデータの ftp パスを手に入れる

NCBI にどういうデータがどういう風に  あるかよくわかっていませんが、とりあえず自分がやった範囲では、ftp パスを用いて、圧縮された fna ファイルを  ダウンロードし、解凍しました。(解凍せずに中身を見ようとして、文字コードエラーが出たので注意！)
解凍せずに扱おうとしたところ、

```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1
```

というエラーとお友達になれました。

zip ファイルの解凍は、

```
$ gunzip
```

でできました。

流れとしては、例えば、~/data/に GCF_000010525.1.fna.gz というファイル名でダウンロードする場合、

```
$ wget -O ~/data/GCF_000010525.1.fna.gz ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/010/525/GCF_000010525.1_ASM1052v1/GCF_000010525.1_ASM1052v1_cds_from_genomic.fna.gz
$ gunzip
```

これで GCF_000010525.1.fna ファイルを見たり読み込ませたりして解析に用いることができます！

自分はこれしかやったことがないので、他にも試してみて、追記したいと思います。
