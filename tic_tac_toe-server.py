import socket
import random

r = int(random.randint(1, 2))
c1 = socket.socket()
c2 = socket.socket()
host = socket.gethostname()
port = 9999
port2 = 9998
c1.bind((host, port))
c2.bind((host, port2))
c1.listen(5)
c2.listen(5)

if r == 1:
    beginner = "Client 1"
else:
    beginner = "Client 2"


def start(c1, c2, r, beginner):
    v1, addr = c1.accept()
    print("Client 1 joined the Game")
    v1.send(str.encode("You are Client 1"))
    v2, addr2 = c2.accept()
    print("Client 2 joined the Game")
    v2.send(str.encode("You are Client 2"))
    v1.send(str.encode("The game starts and %s is the beginner" % beginner))
    v2.send(str.encode("The game starts and %s is the beginner" % beginner))
    if r == 1:
        v1.send(str.encode("You"))
        v2.send(str.encode("Other"))
        wahl = v1.recv(1024)
        wahl = wahl.decode()
        v2.send(str.encode(wahl))
        user = "Spieler 1"
        spiel(v1, v2, user)
    else:
        v1.send(str.encode("Other"))
        v2.send(str.encode("You"))
        wahl = v2.recv(1024)
        wahl = wahl.decode()
        v1.send(str.encode(wahl))
        user = "Spieler 2"
        spiel(v1, v2, user)


def spiel(v1, v2, user):
    while 1:
        if user == "Spieler 1":
            a = v1.recv(1024)
            a = a.decode()
            v2.send(str.encode(a))
            user = "Spieler 2"
        else:
            a = v2.recv(1024)
            a = a.decode()
            v1.send(str.encode(a))
            user = "Spieler 1"

start(c1, c2, r, beginner)