# -*- coding: utf-8 -*-
# [名前] getip.py
# [起動] python getip.py
# [仕様] 接続先のグローバルipを取得し標準出力する
#        ログを標準エラー出力に緑色で出力する
# [備考] シグナリングサーバ(server.py)を外部サーバー(sairilab.com:10007)であらかじめ起動させる必要がある

import socket
import sys

serverHost='sairilab.com'  #デフォルトシグナリングサーバー
localHost='0.0.0.0'
port=25001
localAddr=(localHost,port)
serverAddr=(serverHost,10007)
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(localAddr)
sys.stderr.write(OKGREEN + "[品川会場 getip.py] : UDPソケットのバインド (%s:%d)\n" % localAddr)
sock.sendto("ping",serverAddr)
sys.stderr.write("[品川会場 getip.py] : シグナリングサーバーへの問い合わせ.. (%s:%d)\n" % serverAddr)

targetIp,addr=sock.recvfrom(1024)

sys.stderr.write("[品川会場 getip.py] : 接続先グローバルアドレス = %s\n" % targetIp)
sys.stderr.write(ENDC)
sys.stdout.write("%s\n" % targetIp)

sock.close()


