#!/bin/sh
# [名前] streamingH264.sh
# [起動] sh streamingH264.sh
# [仕様] UDP hole punchingを行い。コネクションを確立後、標準入力から読み取ったデータ(映像バイナリ)を送信する

ip=`python getip.py`

raspivid -n -t 0 -w 600 -h 450 -vf -o -|python streaming.py $ip
