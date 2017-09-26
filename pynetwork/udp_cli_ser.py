#! /usr/bin/python
# Program to run client and server on udp protocol

import socket, sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

maxi=65535
port=1060

if sys.argv[1] == "server":
	s.bind(("127.0.0.1",port))
	print "Listening at", s.getsockname()
	while True:
		data, address = s.recvfrom(maxi)
		print "The client at", address, "says",repr(data)
		s.sendto("Your data was %d bytes" %len(data),address)

elif sys.argv[1] == "client":
	print "Address before sending", s.getsockname()
	s.sendto("This is the message i'm sending",("127.0.0.1",port))
	print "Address after sending", s.getsockname()
	data, address = s.recvfrom(maxi)
	print "The server", address, "says", repr(data)

else:
	print "Usage ./udp_cli_ser.py server|client"