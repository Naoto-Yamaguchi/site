Title: バイオインフォマティクスで使う（かもしれない）シークエンスまとめ
Date: 2019-06-06
Category: Bioinformatics
Tags: Bioinformatics, Sequence
Slug: bioinfo_sequence
Authors: Naoto Yamaguchi
Summary: バイオインフォマティクスで使うデータベースをまとめてみた
Status: draft


# 動機
様々なseqが出てきて混乱してきたのと、どういうシークエンス方法があってそれによって何を解析できるかを知っておくことは重要だと考えた


# 何を読むか
* DNA-seq
こういう風には呼ばないと思いますが
    * Deep-seq
        何回も繰り返して読む

* RNA-seq
mRNAをcDNAにして相補鎖を合成。PCRで増幅して読む。発現量がわかる。
RPKMとかの指標を用いて発現量を定量化する。

* ChIP-seq
ある注目しているタンパク質がゲノムのどの部分に結合しているかを解析。注目しているタンパク質に対する抗体を用意する必要がある。DNAに結合しているタンパク質のゲノム上の位置を正確に知ることができ、例えばヒストンの結合密度を測ることで、ゲノムのどこがヘテロクロマチンで、どこがユークロマチンになっているかわかる(?)
須谷先生の例がわかりやすいが、日本列島からてんとう虫を見つけるようなもの。

* ATAC-seq
ChIP-seqの簡易版。操作が簡単らしく、最近流行りで、データ量も増えているらしい。

メチル化修飾
エピゲノム解析は？


# 何で読むか
* ショートリードシーケンサ
    * illumina

* ロングリードシーケンサ
    * PacBio
    * Oxford Nanopore
    




    生物情報基礎論Ⅱレポート 鈴木先生
(2018-12-29) J4-170226 山口尚人

1.	イルミナ型の次世代シークエンサーについて、「クラスターPCR」、「リバーシブルダイターミネーター」について説明せよ。

・クラスターPCR （ブリッジPCR）
PCRをフローセル上でおこなうことで、クラスター状にDNA分子を増幅させる方法である。
以下のステップで行われる
①	ランダムに切断されたDNA断片の両端に2種類のアダプターを結合させる。
②	1本鎖に変性させたDNAを、フローセルと呼ばれるスライドグラスの基盤上に吸着させる。フローセル上には、2種類のアダプターの相補鎖が固定されているので、DNA断片の固定されていない側のアダプターは、フローセル上の相補的なアダプターと結合できる。
③	dNTPsとDNAポリメラーゼを加えてDNA鎖を伸長させて、2本鎖を形成させる。この形成の際に、2本鎖がフローセル上でブリッジを形成する。
④	新しく形成されたDNA2本鎖を1本鎖に変性させることで、1本鎖DNA断片が2本できる。同様に結合、伸長、変性を繰り返すことで局所的に1本鎖DNA断片が増幅しフローセル上に多数のクラスターが形成される。
以上のようにして、DNAを増幅させる方法である。

・リバーシブルダイターミネーター
Sequencing-by-synthesis法（SBS法)の中で用いられるReversible Termination sequencingでプライマーの伸長を可逆的に止めて塩基を同定するために用いられる物質のことである。蛍光標識されたヌクレオチド（A, T, G, Cの4種類）の3‘末端の保護基がターミネーターとして働き、DNA合成が1塩基ずつストップしながら行われる。シークエンスでは、4種類の可逆的ターミネーター、プライマー、DNAポリメラーゼを添加して、1塩基合成反応を行い、画像に写る蛍光の種類で取り込まれた塩基を判定する。可逆的に止めることで、蛍光標識ヌクレオチドとターミネーターを除去することができ、再度ヌクレオチドを取り込み、シークエンスをおこなえて、効率的な解析が可能になる。
類似の方法として、サンガー法がある。Reversible Termination sequencing法とサンガー法の違いは、ヌクレオチドとして、前者は、プライマーの伸長を止めるために修飾されたdNTP（デオキシリボヌクレオシド三リン酸）を使うのに対して、後者は、不可逆的にプライマーの伸長を止めるために、ddNTP（ジデオキシリボヌクレオシド三リン酸）を使う点である。前者の方法で、可逆的ターミネーターとして使うものとしては2種類あげられ、五炭糖の3’が修飾され3’-ORとなって3’がブロックされているものと、3’-OHはそのままで、塩基の先につく、蛍光標識とそのリンカーが可逆的ターミネーターになっているものがある[6]。


2.	プロモーター、エンハンサー、発現抑制領域に特徴的なヒストン修飾を２種類あげよ。
プロモーター: H3K4me2, H3K27ac
エンハンサー: H3K4me1, H3K27ac
発現抑制領域: H3K9me3, H3K27me3


3.	ChIP-Seq解析の手法について説明せよ。
ChIP-Seqは、Chromatin immunoprecipitation & Sequencingの略で、クロマチン免疫沈降法にシーケンスを組み合わせたものである。
ChIP-Seqは、抗原抗体反応を利用して、ゲノム中でタンパク質とDNAが結合している部分を検出する方法であり、シーケンサーを用いてゲノムワイドにおこなうことで、DNAメチル化やヒストン修飾などのエピジェネテック修飾、転写因子の結合部位の同定を網羅的におこなうことができる。

以下のようなステップでおこなう。
①	生細胞内で、DNAに結合している目的のタンパク質をホルムアルデヒド等を用いて共有結合によってDNAに固定（架橋結合）する。
②	細胞を溶解させ、DNAを断片化する
③	断片化したタンパク質-DNA複合体を目的のタンパク質に特異的な抗体で免疫沈降させる
④	タンパク質-DNA複合体を脱架橋してDNAを精製する。
⑤	ハイブリダイゼーションに必要な量までDNA断片をPCRで増幅させる。
⑥	シークエンスを行う
⑦	クオリティコントロール
シークエンスのデータを元に、クオリティの低い塩基・リードを除去する
⑧	マッピング、ピークコール
シークエンスをおこなった、DNA断片の配列と全ゲノムとを比較、照合すること（マッピング）で、タンパク質と結合しているDNAがゲノム上のどの位置にあるか解析できる。このような作業をピークコールという。
⑨	アノテーション
ピークコールなどで得られた情報に加え、既知の遺伝子情報に基づいて、タンパク質が結合したDNA配列がどのように遺伝子発現を制御するのか調べる。

DNA精製の後、シーケンサーではなく、マイクロアレイを利用した同様の解析方法であるChIP-chip法と比べ、1度に扱える解析量やピークの解像度、感度の点で優れている。
ChIP-seqのデータをマイクロアレイ、もしくはRNA-seqの情報と組み合わせれば、遺伝子発現パターンに関わる転写調節因子を明らかにすることもできる。
	

参考文献
[1] “08. BridgPCR”. binf snipcademy.
https://binf.snipcademy.com/lessons/ngs-techniques/bridge-pcr, (参照 2018-12-29)
[2] “What is the illumina method of DNA sequencing?”. yourgenome.
https://www.yourgenome.org/facts/what-is-the-illumina-method-of-dna-sequencing, (参照 2018-12-29)
[3] “次世代DNAシーケンシングの原理”. InfoBio.
https://www.yourgenome.org/facts/what-is-the-illumina-method-of-dna-sequencing, (参照 2018-12-29)
[4] “ブリッジPCR”. 実験医学online.
https://www.yodosha.co.jp/jikkenigaku/keyword/1044.html, (参照 2018-12-29)
[5] “Illumina Sequencing Technology”. YouTube.
https://www.youtube.com/watch?v=womKfikWlxM#action=share, (参照 2018-12-29)
[6] Fei Chen, Mengxing Dong, Meng Ge, Lingxiang Zhu, Lufeng Ren, Guocheng Liu, Rong Mu, “The History and Advances of Reversible Terminators Used in New Generations of Sequencing Technology”. Genomics, Proteomics & Bioinformatics, Volume 11, Issue 1, February 2013, Pages 34-40
[7] “イルミナシーケンステクノロジー”. イルミナ株式会社.
https://jp.illumina.com/content/dam/illumina-marketing/apac/japan/documents/pdf/technote_illumina_sequencing_technology-j.pdf, (参照 2018-12-29)

[8] 倉田哲也（2009）「ChIP-seq法によるクロマチンと転写因子のゲノムワイド解析」, 『蛋白質 核酸 酵素』Vol.54 No.10, pp1248-1255, 
http://lifesciencedb.jp/dbsearch/Literature/get_pne_cgpdf.php%3Fyear%3D2009%26number%3D5410%26file%3DQmnHPLUSClqmhhb1STkxKXgXg%3D%3D, (参照 2018-12-29)
[9] “ChIP-Seq”. biopapyrus.
https://bi.biopapyrus.jp/hts/chipseq/, (参照 2018-12-29)
[10] B.Alberts et al. (2017)『細胞の分子生物学 第6版』（中村桂子ほか訳） ニュートンプレス.
