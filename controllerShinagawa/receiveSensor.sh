

#!/bin/sh

#接続先グローバルipの取得
ip=`python getip.py|tail -1`
echo "[receiveSensor.sh] : 接続先グローバルip[ $ip ]" >&2

sleep 3

#センサーデータを受信して標準出力
python receiver.py $ip


