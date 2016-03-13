# -*- coding: utf-8 -*-
# [名前] receiver.py
# [起動] python receiver.py "接続先グローバルip"
# [仕様] UDP hole punchingによるコネクション確立後、データを受信し標準出力に吐き出す
# [備考] streaming.pyより後のタイミングで起動させる必要がある


import socket
import sys

param=sys.argv
remoteHost=param[1]
localHost='0.0.0.0'
port=25000
localAddr=(localHost,port)
remoteAddr=(remoteHost,port)

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
