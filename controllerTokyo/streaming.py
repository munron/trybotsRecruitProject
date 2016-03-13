# -*- coding: utf-8 -*-
# [名前] streaming.py
# [起動] python streaming.py "接続先グローバルip"
# [仕様] UDP hole punchingを行い。コネクションを確立後、標準入力から読み取ったデータ(映像バイナリ)を送信する
# [備考] receiver.pyより前のタイミングで起動させる必要がある


import socket
import sys

param=sys.argv
remoteHost=param[1]
localHost='0.0.0.0'
port=25000
localAddr=(localHost,port)
remoteAddr=(remoteHost,port)

print "Accessing to %s:%d" % (remoteHost,port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
print "binded UDP socket to %s:%d" % localAddr

#UDP hole punchingの処理
#この送信は送信先ルーターに阻まれ受信はされない
#しかしルーターに接続記録が残るため以降データを受信することが可能となる
sock.sendto("UDP hole punching",remoteAddr)
print "sended hole punching packet to %s:%d" % remoteAddr

data,addr = sock.recvfrom(1024)
print "message from [%s]:%s" % (data,addr)
print "接続が確立しました"
print "localhost:1337 にアクセスしてください"

#標準入力から読み取ったデータを送信
while True:
   buf = sys.stdin.readline()
   sock.sendto(buf,remoteAddr)
