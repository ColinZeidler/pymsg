import conns
import socket, sys

commands = 	{'/dc':1,   #disconnect client from server,	/dc {reason/msg}
			'/stop':1,  #tell server to stop running,		/stop {passwd}
			'/join':1,  #join given channel,				/join {channel}
			'/leave':1, #leave given channel,				/leave {channel}
			'/to':2,    #send to given channel, 			/to {channel} {msg}
			'/setnick':1}

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
		elif cmd == "/setnick":
			set_nick(strings[1], con)
		elif cmd == "/to":
			pass
	else: #msg does not contain a command
		for person in conns.clients.keys():
			if person == con:
				continue
			conns.send(conns.nicks.get(con), person, msg)

def server_dc(msg, con):
	print "disconnecting client"
	broadcast_all(conns.SERVER_STR, conns.nicks.get(con) + " Disconnected")
	con.close()
	del conns.clients[con]

def stop(passwd):
	if passwd == conns.PASS:
		broadcast_all("/dc ", "")
		conns.FLAG = True

def join(room):
	pass

def leave(room):
	pass

def to(room, msg):
	pass

def set_nick(name, con):
	prevName = conns.nicks.get(con)
	conns.nicks[con] = name
	print "set nickname to:", name
	broadcast_all(conns.SERVER_STR, prevName + " changed name to " + name) 


def broadcast_all(sender, msg):
	for person in conns.clients.keys():
		conns.send(sender, person, msg)
