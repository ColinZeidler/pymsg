#handling all of the connection methods
import socket

HOST = ''
PORT = 60000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_STR = "Server"
clients = {}
