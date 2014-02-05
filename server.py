#author Colin Zeidler
from time import sleep
from threading import Thread, Lock
import socket, sys
import conns, messages, User, Room

def main():
	print "Starting server"
	print conns.clients
	print conns.PORT

	Thread(target=accept_cons).start()
	Thread(target=msg_control).start()
	
	while True:
		if conns.FLAG:
			break
		sleep(2)
		lock.acquire()
		print "clients ",
		print conns.clients.values()
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
	while True: #change this so that the program can exit cleanly
		if conns.FLAG:
			break
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
#this needs to be continued
		conns.clients.append(User(conn, addr))
#		conns.clients[conn] = addr
#		conns.nicks[conn] = addr[0]

		messages.broadcast_all(conns.SERVER_STR, conns.nicks.get(conn) + " connected")
		lock.release()
	print "done listening for conns"

def msg_control():
	while True:
		if conns.FLAG:
			break
		sleep(0.05)
		lock.acquire()
		for con in conns.clients.keys():
			try:
				msg = con.recv(128)
			except:
				continue
			messages.parse_msg(msg, con)
		lock.release()
	print "done listening for msgs"

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	main()
