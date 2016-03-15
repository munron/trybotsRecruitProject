

#!/bin/sh

#接続先グローバルipの取得
ip=`python getip.py|tail -1`
echo "接続先グローバルip[ $ip ]"

sleep 3

#映像バイナリ(h.264)を受け取りmplayerでデコードして再生
python receiver.py $ip|gst-launch-1.0 filesrc location=/dev/stdin ! h264parse ! avdec_h264 ! videoconvert ! autovideosink


