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
		print clients.values()
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
		clients[conn] = addr
		lock.release()

def send(sender, reciever, msg):
	reciever.send(sender + ": " + msg)

def msg_control():
	while True:
		sleep(0.05)
		lock.acquire()
		for con in clients.keys():
			try:
				msg = con.recv(128)
			except:
				print "Err: no data to read"
				lock.release()
				continue
			if msg[:3] == "/dc":
				#remove the client from the dict
				print "disconnecting client"
				del clients[con]
			else:
				#loop through all clients and send the message out
				#for person in client.keys():
				
				pass
		lock.release()

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	clients = {}
	main()
