#! /usr/bin/python3

#Remove ''' below to enable program using urllib

'''
import urllib.request,sys


try:
	rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
	print ("Provide a legitimate RFC number")
	sys.exit()

try:
	url = "http://www.ietf.org/rfc/rfc{}.txt" .format(rfc_number)
	rfc_raw = urllib.request.urlopen(url).read()
	rfc=rfc_raw.decode()
	print (rfc)
except (urllib.error.HTTPError):
	print("Error 404 caused due to using number {}".format(rfc_number))
	sys.exit()

'''

import sys, socket # This program requires user to build get messages, and sockets

try:
	rfc_number = int(sys.argv[1])

	host="www.ietf.org"
	port=80
	sock = socket.create_connection((host,port))

	req = (
		"GET /rfc/rfc{}.txt HTTP/1.1\r\n"
		"Host:{}:{}\r\n"
		"User-Agent:Python{}\r\n"
		"Connection:close\r\n"
		"\r\n"
		)
	req=req.format(rfc_number,host,port,sys.version_info[0])
	sock.sendall(req.encode('ascii'))
	rfc_raw = bytearray()


	while True:
		buf = sock.recv(4096)
		if not len(buf):
			break
		rfc_raw += buf
	rfc = rfc_raw.decode('utf-8')
	print (rfc)
except (ValueError, IndexError):
	print ("Provide a legitimate RFC number")
	sys.exit()