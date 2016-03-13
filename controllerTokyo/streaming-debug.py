# -*- coding: utf-8 -*-
#[名前] streaming-debug.py
#[起動] python streaming-debug.py "使用ポート"
#[仕様] グローバルipの取得 - UDP hole punching - 映像の送信 

import socket
import sys

param=sys.argv
serverHost='sairilab.com'  #デフォルトシグナリングサーバー
localHost='0.0.0.0'
port= int(param[1])
serverAddr=(serverHost,10007)
localAddr=(localHost,port)

#-------------------シグナリング処理--------------------------
signalingSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
signalingSock.bind(localAddr)
print "binded UDP socket to %s:%d" % localAddr

signalingSock.sendto("ping",serverAddr)
print "send packet to %s:%d" % serverAddr

targetIp,addr=signalingSock.recvfrom(1024)
print "target Ip %s" % targetIp

signalingSock.close()
remoteAddr=(targetIp,port)
#--------------------------------------------------------------


print "Accessing to %s:%d" % remoteAddr

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

#標準入力から読み取ったデータを送信
while True:
   buf = sys.stdin.read(1024)
   sock.sendto(buf,remoteAddr)
