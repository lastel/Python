import socket
import random

r = random(1, 2)

c1 = socket.socket()
c2 = socket.socket()
host = socket.gethostname()
port = 9999
port2 = 9998
c1.bind((host, port))
c2.bind((host, port2))

c1.listen(5)
c2.listen(5)