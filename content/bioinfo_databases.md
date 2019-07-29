Title: バイオインフォマティクスで使う（かもしれない）データベースまとめ
Date: 2019-06-06
Category: Bioinformatics
Tags: Bioinformatics, Database
Slug: bioinfo databases
Authors: Naoto Yamaguchi
Summary: バイオインフォマティクスで使うデータベースをまとめてみた
Status: draft


# 動機
世の中には優れたデータベースが多々ありますが、自分が解析する際、こういうデータが欲しい！と思った時にどこを探せば良いかわかっておくことは、解析手法を考え提案する上でも非常に重要だと思ったので、授業等で学んだ内容を中心に随時まとめたいと考えたからです。


# 一般的なデータベース
* [NCBI]()

* [Ensemble]()


# ヒトゲノムデータベース
* [gnomAD](http://gnomad.broadinstitute.org/)
最大級のアレルと遺伝子型のデータベース
Broad Institute @ MIT/Harvard

* [UK BioBank](https://www.ukbiobank.ac.uk/)
コホート研究　2006年より英国で500000人のボランティア(年齢40-69歳を)最低30年間追跡調査
1塩基変異検出(約50万ポイント、全エキソン5万人)
2138表現型(疾患、MRI画像等)
しっかりとしたセキュリティが担保されたサーバーを準備すれば、2000 Euros/projectでデータを購入することができ。
現在、最も進んだデータ共有ポリシーである。

* [All of US](https://allofus.nih.gov/)
2016年開始
オバマ政権時のPrecision Medicine Initiative(PMI)によりスタート

* [東北メディカルバンク](https://www.megabank.tohoku.ac.jp/)
2012年からのコホート研究
3500人の全ゲノム解読データを公開している

# 疾患関連
* [OMIM (Online Mendelian Inheritance in Man)](http://www.omim.org/)
メンデル性遺伝病のデータベース
病名を入力すると原因遺伝子変異を教えてくれる
また、劣性・優性遺伝病の例は年々増加しており、病気の原因が特定されたメンデル性遺伝病は[Wikipedia](https://en.wikipedia.org/wiki/Genetic_disorder)からも見ることができる


# タンパク質データベース
* [Uni Prot]()


# データベースではないけれど、データを集めている民間企業
* [23andMe](https://www.23andme.com/)
$99で多様な疾患を罹患するリスクを調べてくれるサービスで、ハプロタイプ別の祖先推定もでき、2017年に話題になった。
2017年8月のversion5のサービスでは、64万箇所のSNPを調べている。
100万人超のデータがある

このように人類遺伝学は保険産業と関連し商業化が進んでいる。これを可能にしたのは、マイヤーらが考案した、連鎖不平衡（Linkage Disequilibrium）を解析するアルゴリズムである。