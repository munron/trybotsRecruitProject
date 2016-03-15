# -*- coding: utf-8 -*-
# [名前] streaming.py
# [起動] python streaming.py "接続先グローバルip"
# [仕様] UDP hole punchingを行い。コネクションを確立後、標準入力から読み取ったデータ(映像バイナリ)を送信する

import socket
import sys

param=sys.argv
remoteHost=param[1]
localHost='0.0.0.0'
port=30000
localAddr=(localHost,port)
remoteAddr=(remoteHost,port)
YELLOW='\033[93m'
ENDC='\033[0m'

sys.stderr.write(YELLOW)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
sys.stderr.write("[品川会場 streaming.py] : UDPソケットをバインド (%s:%d)\n" % localAddr)

#UDP hole punchingの処理
#この送信は送信先ルーターに阻まれ受信はされない
#しかしルーターに接続記録が残るため以降データを受信することが可能となる
sock.sendto("UDP hole punching",remoteAddr)
sys.stderr.write("[品川会場 streaming.py] : UDP Hole Punchingパケットの送信 (%s:%d)\n" % remoteAddr)

data,addr = sock.recvfrom(1024)
sys.stderr.write("[品川会場 streaming.py] : パケットを受信 [%s]:%s\n" % (data,addr))
sys.stderr.write("接続が確立しました\n")
sys.stderr.write(ENDC)

#標準入力から読み取ったデータを送信
while True:
   buf = sys.stdin.read(1024)
   sock.sendto(buf,remoteAddr)
