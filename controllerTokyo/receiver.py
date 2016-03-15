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
port=30000
localAddr=(localHost,port)
remoteAddr=(remoteHost,port)
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
sys.stderr.write(WARNING)
sys.stderr.write("[東京会場 receiver.py] : UDPソケットをバインド (%s:%d)\n" % localAddr)

#UDP hole punchingの処理
#本来ならばこのパケットは接続先のルーターに阻まれるはずであるが
#streaming.pyによってルーターが記録した経路でパケットが届く
sock.sendto("Hi!! this is receiver",remoteAddr)
sys.stderr.write("[東京会場 receiver.py] : 接続要求.. (%s:%d)\n" % remoteAddr)
sys.stderr.write(ENDC)
#受信したデータを雑に吐き出す
while True:
    sys.stdout.write(sock.recv(4096))
