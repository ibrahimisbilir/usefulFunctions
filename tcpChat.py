#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import socket
from threading import Thread

server=socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sohbet_alive = True

def sohbet():
  global sohbet_alive
	while sohbet_alive:
		rec=''
		rec=server.recv(1024)
		print rec

try:
	os.system("clear")
	ip=raw_input("Enter the server ip address\n")
	port=int(raw_input("Enter the server port number\n"))
	server.connect((ip,port))
	print 'connected'
	listen=Thread(target=sohbet)
	listen.daemon=True
	listen.start()
	while True:
		send=raw_input("Please enter your message\n")
		if send == 'close':
			sohbet_alive=False
			server.shutdown(socket.SHUT_RDWR)
			server.close()
			break
		else:
			server.send(send)
	exit()

except KeyboardInterrupt:
	server.close()
	exit()
