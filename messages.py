commands = 	{'/dc':2,   #disconnect client from server,	/dc {reason/msg}
			'/stop':2,  #tell server to stop running,		/stop {passwd}
			'/join':2,  #join given channel,				/join {channel}
			'/leave':2, #leave given channel,				/leave {channel}
			'/to':3}    #send to given channel, 			/to {channel} {msg}
hasMsg = ['/dc', '/to']

def parse_msg(msg):
	strings = msg.split(" ")
	cmd = strings[0]
	if commands.get(cmd) < len(strings) and cmd in hasMsg:
		msg = " ".join(strings[commands.get(cmd)-1:])
	else:
		msg = strings[-1:]
	print strings[:commands.get(cmd)-1], msg
