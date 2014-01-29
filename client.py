#author Colin Zeidler
from time import sleep
from threading import Thread, Lock
import socket, sys
import conns

HOST = 'localhost'

def main():
	print "Hello world"
	connect(HOST)
	print conns.sock.getsockname()
	Thread(target=listen).start()
	while True:
		msg = raw_input()
		send(msg)
		pass

def connect(server):
	conns.sock.connect((server, conns.PORT))

	msg = conns.sock.recv(128)
	print msg
	pass

def send(msg):
	conns.sock.send(msg)
	if msg[:3] == "/dc":
		conns.sock.close()
		sys.exit(0) #should find a better way to quit...
	pass

def listen():
	while True:
		msg = conns.sock.recv(128)
		print msg

if __name__ == "__main__":
	#do the normal stuff
	main()
