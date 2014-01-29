#author Colin Zeidler
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
	
	while True:
		sleep(2)
		lock.acquire()
		print "clients ",
		print conns.clients.values()
		lock.release()

	#end of server
	print "Server closed"
	
#accepts new connections and adds them to the server
def accept_cons():
	print "Started accepting"
	try:
		conns.sock.bind((conns.HOST, conns.PORT))
	except:
		print "Unable to bind socket"
		sys.exit(0)
	while True: #change this so that the program can exit cleanly
		conns.sock.listen(1)
		conn, addr = conns.sock.accept()
		print "Connected to ", addr
		conns.send(conns.SERVER_STR, conn, "Welcome")

		conn.setblocking(0) #set the socket to non blocking
		#should allow checking for data, and continuing if none
		#preventing concurrent access
		lock.acquire()
		conns.clients[conn] = addr
		conns.nicks[conn] = addr[0]
		lock.release()

def msg_control():
	while True:
		sleep(0.05)
		lock.acquire()
		for con in conns.clients.keys():
			try:
				msg = con.recv(128)
			except:
				continue
			messages.parse_msg(msg, con)
#			send(nicks.get(con), person, msg)
		lock.release()

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	main()
