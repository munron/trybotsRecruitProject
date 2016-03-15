# -*- coding: utf-8 -*-
# [名前] getip.py
# [起動] python getip.py
# [仕様] 接続先のグローバルipを取得する
# [備考] シグナリングサーバ(server.py)を外部サーバー(sairilab.com:10007)であらかじめ起動させる必要がある

import socket
import sys

serverHost='sairilab.com'  #デフォルトシグナリングサーバー
localHost='0.0.0.0'
port=25001
localAddr=(localHost,port)
serverAddr=(serverHost,10007)


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
print "binded UDP socket to %s:%d" % localAddr

sock.sendto("ping",serverAddr)
print "send packet to %s:%d" % serverAddr

targetIp,addr=sock.recvfrom(1024)
print "%s" % targetIp

sock.close()


