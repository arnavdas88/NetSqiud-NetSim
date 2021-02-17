import socket
import random
import threading
import time

class Telnet:
    def __init__(self, name=None, host = None, port = None):
        self.sock = socket.socket()
        self.port = port if port is not None else random.randint(10000, 20000)
        self.host = host if host is not None else socket.gethostname()
        self.connection = None
        self.name = name if name is not None else None
        print(f"{self.host}:{self.port}")
        
    def __call__(self, callback = None):
        thread = threading.Thread(target=self.listener, args=(callback, ))
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def client(self, ):
        host = self.host
        port = self.port
        self.sock.connect((host, port))
        print(self.sock.recv(1024))
        while True:
            self.sock.send(bytes(input(' > '), 'utf-8'))

    def listener_push(self, message):
        if self.connection is not None:
            self.connection.send(bytes(message, 'utf-8'))
        
    def listener(self, callback = None):
        host = self.host
        port = self.port
        self.sock.bind((host,port))
        self.sock.listen(5)
        self.connection, addr = self.sock.accept()
        if self.name is None:
            self.connection.send(b"Server approved connection\n")
        else:
            self.connection.send(b"Server approved connection\n\n")
            self.connection.send(bytes(f"[Connected to {self.name}]\n\n", "utf-8"))
        print("Connection accepted from " + repr(addr[1]) +"\n")
        while True:
            msg = self.connection.recv(1024)
            print(str(repr(addr[1])) + ": " + str(msg))
            if callback is not None:
                callback(str(msg.decode()[0:-2]))
            if msg.decode()[0:-2] == "exit":
                self.connection.close()
                break
            # self.listener_push()

