# trybots_controller
遊泳テスト支援ツール
![link](https://github.com/muro-tani/trybots_controller/blob/master/ui.png)  

##構成  
###クライアントサイド  
####index.ejs  
メインUI,css,javascript  
ロボットのコントロール機能  
各サーボモーターのパラメーター調整機能  
リアルタイムログ表示機能  
サーバーとの通信機能  

###サーバーサイド  
####controller.js 
クライアントとの通信機能  
クライアントからパラメーターを受信しsetting.txtを書き換える  

####servo.py  
標準入力からシグナルを受け取りその値に応じて
サーボモータを制御する。  
setting.txtからパラメータを読み取っている  

Raspberry-pi側の実装  
頭   : GPIO17  
尻尾 : GPIO22    
足   : GPIO27  

###設定ファイル  
####setting.txt
前進時,潜水時,左旋回時、右旋回時の頭、尻尾、足に対応する
サーボモーターの角度が記録されている  

##実行方法
###環境構築  
npm install socket.io  
npm install ejs  
###実行  
$nodejs controller.js|python server.py  
(nodejsでサーバーを起動、その出力をモーター制御するpythonスクリプトに渡している)  
ブラウザ(chrome推奨)でhttp://<raspberrypiのローカルipアドレス>:1337へアクセスする  

