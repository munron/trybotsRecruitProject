

#!/bin/sh

#接続先グローバルipの取得
ip=`python getip.py|tail -1`
echo "接続先グローバルip[ $ip ]"

sleep 3

#センサーデータを受信して標準出力
python receiver.py $ip


