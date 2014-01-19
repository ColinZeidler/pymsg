#author Colin Zeidler
from time import sleep
from threading import Thread, Lock
import socket
import conns

def main():
	print "Starting server"
	print clients
	print conns.PORT

	Thread(target=accept_cons).start()
	
	while True:
		sleep(2)
		lock.acquire()
		print "clients ",
		print clients.keys()
		lock.release()

	#end of server
	print "Server closed"
	
#accepts new connections and adds them to the server
def accept_cons():
	print "Started accepting"
	conns.sock.bind((conns.HOST, conns.PORT))
	while True: #change this so that the program can exit cleanly
		conns.sock.listen(1)
		conn, addr = conns.sock.accept()
		print "Connected to ", addr
		send(conns.sock, conn, "Welcome")
		#preventing concurrent access
		lock.acquire()
		clients[conn] = addr
		lock.release()

def send(sender, reciever, msg):
	reciever.send(sender.getsockname()[0] + ": " + msg)

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	clients = {}
	main()
