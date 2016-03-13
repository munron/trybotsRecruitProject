# -*- coding: utf-8 -*-
# [名前] receiver-debug.py
# [起動] python receiver-debug.py "使用ポート"
# [仕様] グローバルipの取得 - UDP hole punching - 映像の受信

import socket
import sys
import time

param=sys.argv
serverHost='sairilab.com'   #デフォルトシグナリングサーバー
localHost='0.0.0.0'
port=int(param[1])
serverAddr=(serverHost,10007)
localAddr=(localHost,port)

#----------------シグナリング処理-----------------------------
signalingSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
signalingSock.bind(localAddr)
print "binded UDP socket to %s:%d" % localAddr

signalingSock.sendto("ping",serverAddr)
print "send packet to %s:%d" % serverAddr

targetIp,addr=signalingSock.recvfrom(1024)
print "target Ip %s" % targetIp

signalingSock.close()
remoteAddr=(targetIp,port)
#-------------------------------------------------------------

time.sleep(3)

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
print "binded UDP socket to %s:%d" % localAddr

#UDP hole punchingの処理
#本来ならばこのパケットは接続先のルーターに阻まれるはずであるが
#streaming.pyによってルーターが記録した経路でパケットが届く
sock.sendto("Hi!! this is receiver",remoteAddr)
print "sended packet to %s:%d" % remoteAddr

#受信したデータを雑に吐き出す
while True:
    sys.stdout.write(sock.recv(65535))


