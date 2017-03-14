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
        for l in spielfeld:
            for e in range(len(l)):
                if l[e] == "A":
                    z = random.randint(1, 4)
                    if z == 1:
                        l[e] = "?"
        print("\nBrandstiftung\n")
        ausbreitungen = 0
        self.ausgabe(spielfeld)
        self.ausbreitung(self, spielfeld, quadrat, ausbreitungen)

    def ausbreitung(self, spielfeld, quadrat, ausbreitungen):
        wechsel = False
        ausbreitungen += 1
        k_spielfeld = spielfeld
        for lz in range(len(spielfeld)):
            l = spielfeld[lz]
            k_l = l
            for e in range(len(l)):
                if l[e] == "?":
                    l[e] = "."
                if e - 1 > 0:
                    if k_l[e] == "A" and k_l[e - 1] == "?":
                        l[e] = "?"
                        wechsel = True
                if e + 1 < len(spielfeld):
                    if k_l[e] == "A" and k_l[e + 1] == "?":
                        l[e] = "?"
                        wechsel = True
                if len(l) - 1 > 0:
                    if k_l[e] == "A" and k_spielfeld[lz - 1][e] == "?":
                        l[e] = "?"
                        wechsel = True
                if len(l) + 1 < len(spielfeld):
                    if k_l[e] == "A" and k_spielfeld[lz + 1][e] == "?":
                        l[e] = "?"
                        wechsel = True
        if wechsel is True:
            print(("\nAusbreitung %s\n" % ausbreitungen))
            self.ausgabe(spielfeld)
            self.ausbreitung(self, spielfeld, quadrat, ausbreitungen)
        else:
            pass

    def ausgabe(liste_all):
        for l in liste_all:
            for e in l:
                sys.stdout.write((e))
                sys.stdout.write((" "))
            print()