import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "YOUR LOCAL IPV4"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    # when connect to server, returns start position 
    def getPos(self):
        return self.pos
    
    # when connect, sends info to the server that way can confirm connection
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    # send info to srever
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)