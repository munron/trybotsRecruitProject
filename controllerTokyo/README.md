# trybotsリクルートプロジェクト
##概要  
NAT下にある端末間で映像の転送を行う 　
![link](http://sairilab.com/munro/data/udp_hole_punching.png)  

1 : 互いのグローバルipをシグナリング鯖を介して取得する  
2 : このパケットはルーターBに阻まれpcまで届かない  
3 : このパケットは2によってルーターに記録された経路情報によってraspiに届く  
4 : 以降相互に通信することが可能になる  
備考 : プログラムでは簡略化を図るためUDP通信を行うポートを25000に固定している  
####server.py  
シグナリング処理を受け持つ。外部のグローバルから参照できるサーバー上で起動させる  
今回はsairilab.com:10007(自宅鯖)を利用している  
[起動] : python server.py  
####getip.py  
通信に必要不可欠である接続先のグローバルipを取得するプログラム  
シグナリングサーバー(sairilab.com:10007)に問い合わせて接続先グローバルipを受けっとている  
[起動] : python getip.py  

####streaming.py  
raspi(送信)側のプログラム  
UDP hole punchingを行い。コネクションを確立後、標準入力から読み取ったデータ(映像バイナリ)を送信する  
[起動] : python streaming.py {接続先グローバルip}  

####receiver.py  
pc(受信)側のプログラム  
UDP hole punchingによるコネクション確立後、データを受信し標準出力に吐き出す  
[起動] : python receiver.py {接続先グローバルip}  

####streaming.sh  
raspi側の起動スクリプト  
[起動] : sh streamig.sh  

####receiver.py  
pc側の起動スクリプト  
[起動] : sh receiver.sh  

####streaming-debug.py
raspi側デバッグ用プログラム  
[起動] : python  streaming-debug.py {使用ポート}  

####receiver-debug.py  
pc側デバッグ用プログラム  
[起動] : python receiver-debug.py {使用ポート}  

## 環境構築    
受信した映像データをデコードして画面に出力する処理をgstreamerに丸投げします  
###ubuntu  
$ apt-get install gstreamer1.0  

###mac  
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"  
$ brew update  
$ brew install gstreamer gst-libav gst-plugins-ugly gst-plugins-base gst-plugins-bad gst-plugins-good  
receiver.sh最終行のxvimagesinkをautovideosinkに書き換える  
## インストールできてるか確認  
$ which gst-launch-1.0  

## ソースコードダウンロード
$ git clone https://gist.github.com/d65f5222ba29778d4ba0.git trybots  
$ cd trybots  

## 実行  
####サーバーサイド(sairilab.com:10007)  
$python server.py  

####送信側(raspberrypi側)  
$ sh streaming.sh  

####受信側(pc側)  
$ sh receiver.sh
