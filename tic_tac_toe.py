import sys


def feld():
    spielfeld = []
    for x in range(3):
        zeile = []
        for y in range(3):
            zeile.append("-")
        spielfeld.append(zeile)
    print("\nSpielfeld\n")
    ausgabe(spielfeld)
    teamwahl(spielfeld)


def teamwahl(spielfeld):
    print("\nMuster Wahl\n")
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
            print("Ungültige eingabe, versuche es nochmal!")
    user = "Spieler 1"
    spiel(spielfeld, p_muster, p2_muster, user)


def spiel(spielfeld, p_muster, p2_muster, user):
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
        while 1:
            try:
                p = (input("%s(%s), wo willst du dein %s haben? (x,y)   " % (user,user_muster,user_muster)))
                if spielfeld[int(p[0])][int(p[2])] == "-":
                    spielfeld[int(p[0])][int(p[2])] = user_muster
                    break
                else:
                    print("Auf diesem Feld ist schon jemand Wähle nochmal!")
            except:
                print("Ungültige eingabe, versuche es nochmal!")
        win(spielfeld, p_muster, p2_muster, user, user_muster)
    else:
        unentschieden()


def win(spielfeld, p_muster, p2_muster, user, user_muster):
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
        sys.exit()
    else:
        if user == "Spieler 1":
            user = "Spieler 2"
        else:
            user = "Spieler 1"
        spiel(spielfeld, p_muster, p2_muster, user)


def unentschieden():
    print("Das Spiel ist vorbei und keiner hat gewonnen!")


def ausgabe(spielfeld):
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

feld()