#author Colin Zeidler
from time import sleep
from threading import Thread, Lock

def main():
	print "Starting server"
	print clients

	Thread(target=accept_cons).start()
	
	while carryon:
		sleep(2)
		lock.acquire()
		print "clients ",
		print clients
		lock.release()

	#end of server
	print "Server closed"
	

def accept_cons():
	print "Started accepting"
	counter = 0
	while counter < 50:
		sleep(0.4)
		print "adding client"
		#preventing concurrent access
		lock.acquire()
		clients.append(counter)
		lock.release()
		print "counter ", 
		print counter
		counter+= 1
	carryon = False

def send(sender, reciever, msg):
	#todo
	pass

if __name__ == '__main__':
	#do the normal stuff
	lock = Lock()
	clients = []
	carryon = True
	main()
