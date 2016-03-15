
#!/bin/sh

#接続先グローバルipを取得
ip=`python getip.py|tail -1`

echo "接続先グローバルip"
echo $ip

#カメラモジュールからh.264エンコードされたバイナリを受け取り送信
raspivid -n -t 0 -w 600 -h 450 -vf -o -|python streaming.py $ip
