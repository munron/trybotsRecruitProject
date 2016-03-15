# [名前] receiverH264.sh
# [起動] sh receiverH264.sh
# [仕様] UDP hole punchingによるコネクション確立後、H264データをgstreamerによって再生する
# [備考] streaming.pyより後のタイミングで起動させる必要がある
#!/bin/sh

ip=`python getip.py`
sleep 3
python receiver.py $ip|gst-launch-1.0 filesrc location=/dev/stdin ! h264parse ! avdec_h264 ! videoconvert ! autovideosink


