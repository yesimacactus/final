# 10.11.45.248
import socket
from _thread import *
import sys

server = "192.168.1.37"
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
s.listen(2)
print("Waiting for a connection, Server Started")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

post = [(0,0), (100,100)]

# threaded function
    
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            # 2048 bits is amt of info we want to receive
            data = conn.recv(2048)
            # have to decode because hwen sending data between client to server, we hav to encode
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            # hav to encode info bc sending across server
            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    # closes connection so can rerun later
    conn.close()
    
currentPlayer = 0
# while loop to continously look for connections
while True:
    # accept accepts the connection and the connection is stored in the variable 
    conn, addr = s.accept()
    print("Connected to:", addr)

    # threading allows the loop to run without the function finishing executing, the threaded function can be a process in the backgorund and a llow the while loop to continue
    start_new_thread(threaded_client, (conn,))
