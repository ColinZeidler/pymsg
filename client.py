#author Colin Zeidler
from time import sleep
from threading import Thread, Lock
import socket
import conns

HOST = 'localhost'

def main():
	print "Hello world"
	connect(HOST)

def connect(server):
	conns.sock.connect((server, conns.PORT))

	msg = conns.sock.recv(128)
	print msg
	pass

def listen():
	pass

if __name__ == "__main__":
	#do the normal stuff
	main()
