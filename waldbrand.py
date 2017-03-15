import random
import sys
import time


class Waldbrand:

    def wald(self, quadrat):
        wartezeit = (0.5)
        time.sleep(wartezeit)
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
        self.brand(self, spielfeld, wartezeit)

    def brand(self, spielfeld, wartezeit):
        time.sleep(wartezeit)
        for x in spielfeld:
            for y in range(len(x)):
                if x[y] == "A":
                    z = random.randint(1, 4)
                    if z == 1:
                        x[y] = "?"
        print("\nBrandstiftung\n")
        ausbreitungen = 0
        self.ausgabe(spielfeld)
        self.ausbreitung(self, spielfeld, ausbreitungen, wartezeit)

    def ausbreitung(self, spielfeld, ausbreitungen, wartezeit):
        time.sleep(wartezeit)
        braende = []
        wechsel = False
        abgebrannt = None
        ausbreitungen += 1
        for x in range(len(spielfeld)):
            for y in range(len(spielfeld)):
                if spielfeld[x][y] == "?":
                    braende.append((x, y))
                if spielfeld[x][y] == "A":
                    abgebrannt = False
        if abgebrannt is not False:
            self.ende(spielfeld)
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
            self.ausbreitung(self, spielfeld, ausbreitungen, wartezeit)
        else:
            wachstuemer = 0
            self.wachsen(self, spielfeld, wachstuemer, wartezeit)

    def wachsen(self, spielfeld, wachstuemer, wartezeit):
        time.sleep(wartezeit)
        baeume = []
        wachstuemer += 1
        wechsel = False
        for x in range(len(spielfeld)):
            for y in range(len(spielfeld)):
                if spielfeld[x][y] == "a":
                    spielfeld[x][y] = "A"
                    wechsel = True
                if spielfeld[x][y] == "A":
                    baeume.append((x, y))
        if len(baeume) < 20:
            for baum in baeume:
                if baum[0] - 1 >= 0:
                    if spielfeld[baum[0] - 1][baum[1]] == ".":
                        spielfeld[baum[0] - 1][baum[1]] = "a"
                        wechsel = True
                if baum[0] + 1 < len(spielfeld):
                    if spielfeld[baum[0] + 1][baum[1]] == ".":
                        spielfeld[baum[0] + 1][baum[1]] = "a"
                        wechsel = True
                if baum[1] - 1 >= 0:
                    if spielfeld[baum[0]][baum[1] - 1] == ".":
                        spielfeld[baum[0]][baum[1] - 1] = "a"
                        wechsel = True
                if baum[1] + 1 < len(spielfeld):
                    if spielfeld[baum[0]][baum[1] + 1] == ".":
                        spielfeld[baum[0]][baum[1] + 1] = "a"
                        wechsel = True
        if wechsel is True:
            print(("\nWachstum %s\n" % wachstuemer))
            self.ausgabe(spielfeld)
            self.wachsen(self, spielfeld, wachstuemer, wartezeit)
        else:
            self.brand(self, spielfeld, wartezeit)

    def ausgabe(spielfeld):
        for x in spielfeld:
            for y in x:
                sys.stdout.write((y))
                sys.stdout.write((" "))
            print()

    def ende(spielfeld):
        self.ausgabe(spielfeld)
        print("\n\n\nGame Over")
        print("Der Wald ist komplett abgebrannt")
        sys.exit()