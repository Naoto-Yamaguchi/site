Title: OpenMPによる並列処理メモ
Date: 2019-06-24
Category: Programming
Tags: Programming, C
Slug: openmp
Authors: Naoto Yamaguchi
Summary: OpenMP環境構築、コマンド等

# 動機
OpenMPを用いた並列コンピューティングの実装課題に取り組む際に、環境構築がよくわからなかったこと、また、OpenMPを使う際に、スレッド数やプロセス数についてよくわからないことがあったので、軽くわかったことを書いてみました。
また、OpenMPの並列化の際、いくつのスレッドが立っているのか、いくつのコアを使っているのかを調べる必要があったためです。

# OpenMP環境構築
環境構築方法は基本、そのマシンによって異なります。私のMacbookでできた方法を記載しています。

```
gcc4.9以上じゃないとopenmpは使えない模様
$ brew install llvm
(llvmはコンパイラ基盤らしい）
$ open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg
でできると言われたが、これはfile does not existとなり、/Library/Developer/CommandLineTools/以下にはPackagesというディレクトリがなかった。
そのため、一旦これはやめて、
$ brew reinstall gcc
$ brew install gcc49
で
$ g++-4.9 -std=c++11 -fopenmp <ファイル名>.cpp
とすればできた
環境は個々人によるので、これでできるかはわかりません
```


# thread数、process数、コア数を調べる、ハイパースレッティング
CPU型番はこのコマンドで調べられる
こちらを参考にした。
http://no213015e.hatenablog.com/entry/2018/02/07/223914

$｀sysctl machdep.cpu.brand_string｀
｀machdep.cpu.brand_string: Intel(R) Core(TM) i5-6360U CPU @ 2.00GHz｀ 
これで、検索エンジンで「Intel Core i5-6360U」などと調べると、そのプロセッサの情報を見ることができます。今回は[こちら](https://ark.intel.com/content/www/jp/ja/ark/products/91156/intel-core-i5-6360u-processor-4m-cache-up-to-3-10-ghz.html)を参考にしました。
そのプロセッサの情報に、メモリの種類という項目があり、3種類程しか載っておらず、最大メモリ帯域も決まった値が記載されていました。私は、メモリとプロセッサは独立に決められると思っていたのですが、プロセッサに合うメモリというのがある程度決まっていて、そのスペックもほぼ決まっているのでしょうか。そのプロセッサが対応できるメモリの種類、サイズ、転送速度を記載しているという認識で良いのでしょうか。ここは、まだ自分が理解できていない部分です。

# コマンド

以下のコマンドで、ハードウェアの情報の一部を見ることができます。
```
$ system_profiler SPHardwareDataType
Hardware:

    Hardware Overview:

      Model Name: MacBook Pro
      Model Identifier: MacBookPro13,1
      Processor Name: Intel Core i5
      Processor Speed: 2 GHz
      Number of Processors: 1
      Total Number of Cores: 2
      L2 Cache (per Core): 256 KB
      L3 Cache: 4 MB
      Memory: 8 GB
      Boot ROM Version: MBP131.0205.B11
      SMC Version (system): 2.36f96
      Serial Number (system): C02TJ0Q7GVC8
      Hardware UUID: 0B84C404-0239-5964-883A-B5BBB085C4C7

```

また、物理CPUのMAX数
```
$ sysctl -n hw.physicalcpu_max             
2
```
論理CPUのMAX数も見ることができます。
```
$ sysctl -n hw.logicalcpu_max
4
```

これらからわかることは、このMacbookには1つのプロセッサー(四角いチップ)があり、その中に2つのコアが入っていて（これは物理的なコア）、各コアが仮想的に2コアとして動くことで、最大論理コア数は4になっているということです。


なぜ、こういうことを調べたかというと、
MacBookの「このMacについて」を調べたり、ネットで型番を調べても、コア数は2という記載だったのにも関わらず、OpenMPを用いたプログラムで、`omp_get_num_procs()`というコア数を返してくれる関数を実行した際の返り値が、4であったことに疑問を持ったためです。
これはCPUのハイパースレッティングにより、1つのコアを擬似的に2つにすることで、プログラム側からは4つのコアがあるように見えていたためだと考えられます。