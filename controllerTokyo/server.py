# -*- coding: utf-8 -*-
#[名前] server.py
#[起動] python server.py
#[仕様] 2台のクライアントの接続情報(グローバルip)をシグナリングする
#[備考] sairilab.com:10007で運用(ポート開放済み)

import socket
import sys

localHost='0.0.0.0'
port=10007
localAddr=(localHost,port)


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)

while True:
  data1,addr1 = sock.recvfrom(1024)
  print "message from [%s]:%s" % (data1,addr1[0])
  pc1Addr=(addr1[0],port)

  data2,addr2 = sock.recvfrom(1024)
  print "message from [%s]:%s" % (data2,addr2[0])
  pc2Addr=(addr2[0],port)

  sock.sendto(addr2[0],pc1Addr)
  sock.sendto(addr1[0],pc2Addr)



