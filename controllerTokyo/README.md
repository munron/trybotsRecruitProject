#東京側  

##構成  
###映像受信スクリプト  
h264バイナリを受信 -> Gstreamerで表示  
###センサー送信スクリプト  
シリアル通信でセンサー値取得(JSON) -> 送信  

##起動  

###映像受信  
$cd ~/trybotsRecruitProject/controllerTokyo
$sh reveiverH264.sh  

###センサー値送信  
$cd ~/trybotsRecruitProject/controllerTokyo  
//品川会場側の起動を待つ  
$sh streaminfSensor.sh  <シリアルポート名>  
//例 $sh streaminfSensor.sh /dev/tty.usbmodem1461  



