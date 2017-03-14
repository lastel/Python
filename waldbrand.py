import random
import sys


class Waldbrand:

    def wald(self, quadrat):
        spielfeld = []
        for i in range(quadrat):
            zeile = []
            for x in range(quadrat):
                a = random.randint(1, 2)
                if a == 1:
                    zeile.append("A")
                else:
                    zeile.append(".")
            spielfeld.append(zeile)
        print("\nSpielfeld\n")
        self.ausgabe(spielfeld)
        self.brand(self, spielfeld, quadrat)

    def brand(self, spielfeld, quadrat):
        for x in spielfeld:
            for y in range(len(x)):
                if x[y] == "A":
                    z = random.randint(1, 4)
                    if z == 1:
                        x[y] = "?"
        print("\nBrandstiftung\n")
        ausbreitungen = 0
        self.ausgabe(spielfeld)
        self.ausbreitung(self, spielfeld, ausbreitungen)

    def ausbreitung(self, spielfeld, ausbreitungen):
        braende = []
        wechsel = False
        ausbreitungen += 1
        for x in range(len(spielfeld)):
            for y in range(len(spielfeld)):
                if spielfeld[x][y] == "?":
                    braende.append((x, y))
        for feuer in braende:
            spielfeld[feuer[0]][feuer[1]] = "o"
            if feuer[0] - 1 >= 0:
                if spielfeld[feuer[0] - 1][feuer[1]] == "A":
                    spielfeld[feuer[0] - 1][feuer[1]] = "?"
                    wechsel = True
            if feuer[0] + 1 < len(spielfeld):
                if spielfeld[feuer[0] + 1][feuer[1]] == "A":
                    spielfeld[feuer[0] + 1][feuer[1]] = "?"
                    wechsel = True
            if feuer[1] - 1 >= 0:
                if spielfeld[feuer[0]][feuer[1] - 1] == "A":
                    spielfeld[feuer[0]][feuer[1] - 1] = "?"
                    wechsel = True
            if feuer[1] + 1 < len(spielfeld):
                if spielfeld[feuer[0]][feuer[1] + 1] == "A":
                    spielfeld[feuer[0]][feuer[1] + 1] = "?"
                    wechsel = True
        if wechsel is True:
            print(("\nAusbreitung %s\n" % ausbreitungen))
            self.ausgabe(spielfeld)
            self.ausbreitung(self, spielfeld, ausbreitungen)
        else:
            pass

    def ausgabe(liste_all):
        for l in liste_all:
            for e in l:
                sys.stdout.write((e))
                sys.stdout.write((" "))
            print()