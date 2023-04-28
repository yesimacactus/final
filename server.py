# 10.11.45.248
import socket
from _thread import *
import sys

server = "10.11.45.248"
# usually 5555 port is open
port = 5555

# type of network and the ip string
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# try except, try lets u try for errors, except lets u handle hte errors
try:
    # looking for connections
    s.bind((server, port))
except socket.error as e:
    str(e)

# opens up the port for connections, if no arguments, unlimited connections
s.listen(3)