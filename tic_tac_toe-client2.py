import sys
import socket

server = socket.socket()
host = socket.gethostname()
port = 9998


def spielerwahl(server):
    print("Willst du an diesem Computer oder auf einem Server")
    i = input("gegen einen zweiten Spieler spielen?(L/S)   ")
    print()
    if i is "s" or i is "S":
        aussage = "OK, du spielst jetzt auf einem Server"
        i = "S"
        server.connect((host, port))
        a = server.recv(1024)
        print(a.decode())
        a = server.recv(1024)
        print(a.decode())
    else:
        aussage = "OK, du spielst jetzt lokal"
        i = "L"
    print(aussage)
    feld(i)


def feld(i):
    spielfeld = []
    for x in range(3):
        zeile = []
        for y in range(3):
            zeile.append("-")
        spielfeld.append(zeile)
    print("\nSpielfeld\n")
    ausgabe(spielfeld)
    teamwahl(spielfeld, i)


def teamwahl(spielfeld, i):
    print("\nMusterwahl\n")
    if i == "S":
        starter = server.recv(1024)
        starter = starter.decode()
    if i == "L" or (i == "S" and starter == "You"):
        while 1:
            p_muster = input("Willst du X oder O haben?   ")
            if p_muster == ("x" or "X"):
                p_muster = "X"
                p2_muster = "O"
                break
            elif p_muster == ("o" or "O"):
                p_muster = "O"
                p2_muster = "X"
                break
            else:
                print("Ungültige Eingabe, versuche es nochmal!")
        user = "Spieler 1"
        if i == "S":
            server.send(str.encode(p_muster))
    else:
        user = "Spieler 2"
        p2_muster = server.recv(1024)
        p2_muster = p2_muster.decode()
        if p2_muster == "X":
            p_muster = "O"
        else:
            p_muster = "X"
    spiel(spielfeld, p_muster, p2_muster, user, i)


def spiel(spielfeld, p_muster, p2_muster, user, i):
    frei = None
    if user == "Spieler 1":
        user_muster = p_muster
    else:
        user_muster = p2_muster

    for x in range(len(spielfeld)):
        for y in range(len(spielfeld)):
            if spielfeld[x][y] == "-":
                frei = True
    if frei is True:
        if i == "L" or (i == "S" and user == "Spieler 1"):
            while 1:
                try:
                    p = (input("%s(%s), wo willst du dein %s haben? (x,y)   " % (user,user_muster,user_muster)))
                    if spielfeld[int(p[0])][int(p[2])] == "-":
                        spielfeld[int(p[0])][int(p[2])] = user_muster
                        if i == "S":
                            sendestring = (str(p[0]) + str(p[2]))
                            server.send(str.encode(sendestring))
                        break
                    else:
                        print("Auf diesem Feld ist schon jemand Wähle nochmal!")
                except:
                    print("Ungültige Eingabe, versuche es nochmal!")
        else:
            coords = server.recv(1024)
            coords = coords.decode()
            spielfeld[int(coords[0])][int(coords[1])] = p2_muster
        win(spielfeld, p_muster, p2_muster, user, user_muster, i)
    else:
        unentschieden()


def win(spielfeld, p_muster, p2_muster, user, user_muster, i):
    end = False
    ausgabe(spielfeld)
    for xl in range(len(spielfeld)):
        x = spielfeld[xl]
        if set(x) == set(list(user_muster)):
            end = True
        elif set(list(spielfeld[0][xl] + spielfeld[1][xl] + spielfeld[2][xl])) == set(list(user_muster)):
            end = True
        elif set(list(spielfeld[0][0] + spielfeld[1][1] + spielfeld[2][2])) == set(list(user_muster)):
            end = True
        elif set(list(spielfeld[0][2] + spielfeld[1][1] + spielfeld[2][0])) == set(list(user_muster)):
            end = True
    if end is True:
        print(("Das Spiel ist vorbei und %s(%s) hat Gewonnen!" % (user, user_muster)))
        server.close()
        sys.exit()
    else:
        if user == "Spieler 1":
            user = "Spieler 2"
        else:
            user = "Spieler 1"
        spiel(spielfeld, p_muster, p2_muster, user, i)


def unentschieden():
    print("Das Spiel ist vorbei und keiner hat gewonnen!")
    server.close()
    sys.exit()


def ausgabe(spielfeld):
        print()
        yl = 0
        sys.stdout.write((" "))
        for xl in range(len(spielfeld)):
            sys.stdout.write((" " + str(xl)))
        print()
        sys.stdout.write(("┌"))
        for xl in range(len(spielfeld) * 2 + 1):
            sys.stdout.write(("─"))
        sys.stdout.write(("┐"))
        print()
        for x in spielfeld:
            sys.stdout.write(("│"))
            for y in x:
                sys.stdout.write((" " + y))
            sys.stdout.write((" │" + str(yl)))
            print()
            yl += 1
        sys.stdout.write(("└"))
        for xl in range(len(spielfeld) * 2 + 1):
            sys.stdout.write(("─"))
        sys.stdout.write(("┘"))
        print()
        print()

spielerwahl(server)