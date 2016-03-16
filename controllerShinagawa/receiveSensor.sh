
#!/bin/sh
#[名前] : receiveSensor.sh
#[起動] : sh receiveSensor.sh
#[仕様] : センサーデータ受信 -> サーボ制御

ip=`python getip.py`
sleep 3
python receiver.py $ip


