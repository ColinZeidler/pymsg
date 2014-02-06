#author Colin Zeidler
from User import User
from Room import Room
from time import sleep
from threading import Thread, Lock
import socket, sys
import conns, messages

def main():
	print "Starting server"
	print conns.clients
	print conns.PORT

	Thread(target=accept_cons).start()
	Thread(target=msg_control).start()
	
	while not conns.FLAG:
		sleep(2)
		lock.acquire()
		print "clients ",
		print len(conns.clients.values())
		lock.release()

	for person in conns.clients.keys():
		person.close()
	conns.sock.close()
	#end of server
	print "Server closed"
	
#accepts new connections and adds them to the server
def accept_cons():
	print "Started accepting"
	try:
		conns.sock.bind((conns.HOST, conns.PORT))
	except:
		print "Unable to bind socket"
		conns.FLAG = True
	conns.sock.setblocking(0)
	while not conns.FLAG: #change this so that the program can exit cleanly
		sleep(0.05)
		try:
			conns.sock.listen(1)
			conn, addr = conns.sock.accept()
		except:
			continue
		print "Connected to ", addr
		conns.send(conns.SERVER_STR, conn, "Welcome")

		conn.setblocking(0) #set the socket to non blocking
		#preventing concurrent access
		lock.acquire()
		conns.clients[conn] = User(conn, addr)
		#notify all users that some one has joined
		messages.broadcast_all(conns.SERVER_STR, 
			conns.clients.get(conn).name + " connected")
		lock.release()
	print "done listening for conns"

def msg_control():
	while not conns.FLAG:
		sleep(0.05)
		lock.acquire()
		#loop over every connected client
		for con in conns.clients.keys():
			#check if there is a message from the current client
			try:
				msg = con.recv(128)
			except:
				continue
			#send the message to the message parser
			messages.parse_msg(msg, con)
		lock.release()
	print "done listening for msgs"

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	main()
