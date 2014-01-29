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
		print conns.clients.values()
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
		conns.send(conns.SERVER_STR, conn, "Welcome")

		conn.setblocking(0) #set the socket to non blocking
		#should allow checking for data, and continuing if none
		#preventing concurrent access
		lock.acquire()
		conns.clients[conn] = addr
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
			if msg[:3] == "/dc":
				#remove the client from the dict
				print "disconnecting client"
				for person in conns.clients.keys():
					conns.send(conns.SERVER_STR, person, conns.clients.get(con)[0] + " Disconnected")
				con.close()
				del conns.clients[con]
				#do not want to broadcast the /dc command so continue
				continue
			#loop through all clients and send the message out
			for person in conns.clients.keys():
				if person == con:
					#do not send the message back to the sender
					continue
				conns.send(conns.clients.get(con)[0], person, msg)
			
		lock.release()

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	main()
