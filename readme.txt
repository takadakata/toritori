#動作環境
os : ubuntu16.04
code : python3.5
browser : Firefox56.0

#実行に必要なインストールするもの
tshark
	apt-get install tshark
xvfb
	apt-get install xvfb
pyvirtualdisplay
	pip3 install pyvirtualdisplay
selenium
	pip3 install selenium
geckodriver
	https://github.com/mozilla/geckodriver/releasesからダウンロー
ド・解凍し，url_crawle.pyと同じディレクトリに置く


#実行方法
・アクセスするURLを記述したurllist.txtを用意
・python3 url_crawl.pyで実行
・同ディレクトリ内にsample1.pcapのようなpcapファイルが作成される
・アクセスしたURLはcrawled.tsvに出力される


#動作概要
1．urllist.txtからURLのリストを取得し，スタックに入れる．
2．スタックからURLを取り出し，そのURLに対してアクセスする．
3. アクセスしてから n 秒間（初期値は60）の通信データ（pcap）を収集・保存
する．
4. 通信データを保存後，アクセスしたWebサイトのリンク先を取得し，スタック
に追加する．max_depth（初期値は1）を変更することで任意の深さまでページ内
のリンク先を辿ることができる．
5. スタックが空になるまで2～4を繰り返す．

#公開物
・readme.txt : このファイル
・url_crawl.py : Webサイトアクセス時のpcap収集ツール
・urllist.txt : 収集するWebサイトのURLリスト
・crawled.tsv : 収集結果
・pcapフォルダ : 収集した通信データ（urllist.txtで収集したデータ）


#作成
高田　長井
