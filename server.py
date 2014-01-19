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
	Thread(target=msg_control).start()
	
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
		send(conns.sock.getsockname()[0], conn, "Welcome")

		conn.setblocking(0) #set the socket to non blocking
		#should allow checking for data, and continuing if none
		#preventing concurrent access
		lock.acquire()
		clients[addr] = conn
		lock.release()

def send(sender, reciever, msg):
	reciever.send(sender + ": " + msg)

def msg_control():
	msg = conns.sock.recv(128)
	if msg[:3] == "/dc":
		#remove the client from the dict
		pass
	else:
		#loop through all clients and send the message out
		#for person in client.keys():
			
		pass

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	clients = {}
	main()
