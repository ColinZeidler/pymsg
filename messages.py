import conns
import socket, sys

commands = 	{'/dc':1,   #disconnect client from server,	/dc {reason/msg}
			'/stop':1,  #tell server to stop running,		/stop {passwd}
			'/join':1,  #join given channel,				/join {channel}
			'/leave':1, #leave given channel,				/leave {channel}
			'/to':2}    #send to given channel, 			/to {channel} {msg}
hasMsg = ['/dc', '/to']

def parse_msg(msg, con):
	strings = msg.split(" ")
	cmd = strings[0]
	if cmd in commands:
		if cmd == "/dc":
			server_dc(" ".join(strings[commands.get(cmd):]), con)
		elif cmd == "/stop":
			stop(strings[1])
		elif cmd == "/join":
			join(strings[1])
		elif cmd == "/leave":
			leave(strings[1])
		elif cmd == "/to":
			pass
	else: #msg does not contain a command
		for person in conns.clients.keys():
			if person == con:
				continue
			conns.send(conns.clients.get(con)[0], person, msg)

def server_dc(msg, con):
	print "disconnecting client"
	broadcast_all(conns.SERVER_STR, conns.clients.get(con)[0] + " Disconnected")
	con.close()
	del conns.clients[con]

def stop(passwd):
	if passwd == conns.PASS:
		broadcast_all("/dc ", "")
		conns.sock.close()
		sys.exit(0)

def join(room):
	pass

def leave(room):
	pass

def to(room, msg):
	pass


def broadcast_all(sender, msg):
	for person in conns.clients.keys():
		conns.send(sender, person, msg)
