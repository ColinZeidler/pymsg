#author Colin Zeidler
from time import sleep
from threading import Thread, Lock
import socket, sys
import conns

HOST = 'localhost'

def main():
	connect(HOST)
	print conns.sock.getsockname()
	Thread(target=listen).start()
	while not conns.FLAG:
		msg = raw_input()
		if not conns.FLAG:
			send(msg)
	conns.sock.close()

def connect(server):
	conns.sock.connect((server, conns.PORT))

	msg = conns.sock.recv(128)
	print msg
	pass

def send(msg):
	conns.sock.send(msg)
	if msg[:3] == "/dc":
		conns.sock.close()
		conns.FLAG = True

def listen():
	while not conns.FLAG:
		msg = conns.sock.recv(128)
		if msg[:3] == "/dc":
			conns.sock.close()
			conns.FLAG = True
			print "Server offline, press enter to exit"
		else:
			print msg

if __name__ == "__main__":
	if len(sys.argv) >= 2:
		HOST = sys.argv[1]
	else:
		HOST = raw_input("server address: ")
		if HOST == "":
			HOST = "localhost"
	#do the normal stuff
	main()
