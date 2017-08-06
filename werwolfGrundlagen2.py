import sys
import time

#anzahl = int(input("Anzahl der Spieler? "))

#Spieler aus dem Spiel entfernen
def sterben(name):
    i = 0
    for liste in listen:
        x = 0
        for e in liste:
            if e == name:
                del listen[i][x]
            x += 1
        i += 1
    i = 0
    for e in Spieler:
        if e == name:
            del Spieler[i]
        i += 1

def spielende():
    if Spieler == []:
        print("Es hat keiner gewonnen.")
        sys.exit()
    elif Spieler == list(Werwolf):
        print("Die Werwölfe haben gewonnen.")
        sys.exit()
    elif Spieler == list(Vampir):
        print("Die Vampire haben gewonnen.")
        sys.exit()
    elif Werwolf == [] and Vampir == []:
        print("Das Dorf hat gewonnen.")
        sys.exit()
    

#Listen erstellen
Werwolf = []
Vampir = []
Amor = []
Dorfbewohner = []
Seherin = []
Auge = []
Hexe = []
#Doppelliste listen erstellen
listen = [Werwolf,Vampir,Amor,Dorfbewohner,Seherin,Auge,Hexe]
listen2 = []
listenddd = ["Der","Der","Der","Der","Die","Das","Die"]
listenstr = ["Werwolf","Vampir","Amor","Dorfbewohner","Seherin","Auge","Hexe"]
listenstrpl = ["Werwölfe","Vampire","Amor","Dorfbewohner","Seherin","Auge","Hexe"]
Spieler = []
listensp = [1, 1, 0, 1, 0, 0, 0]
listenstrpl2 = []
Verliebte = []
listendddklein = []
nacht = 1

#for i in range(anzahl):
#    input("")

#Eine Form von "listenddd" kleingeschrieben erstellen
for i in listenddd:
    x = i.lower()
    listendddklein.append(x) 

#Spieler Fraktionen zuteilen
x = 0
for liste in listen:
    i = 0
    while 1:
        doppelt = False
        i += 1
        if listensp[x] == 1:
            name = input("Wie heißt %s %s? " % (listenstr[x], i))
        else:
            name = input("Wie heißt %s %s? " % (listendddklein[x],listenstr[x]))
        if name:
            for e in Spieler:
                if name == e:
                    doppelt = True
            if doppelt != True:
                liste.append(name)
                Spieler.append(name)
                if listensp[x] == 0:
                    break
            else:
                print("Der Name \"%s\" wurde 2 mal verwendet, versuche es nochmal!" % name)
                i -= 1
        else:
            break
    x += 1

#Entfernen der unbenutzten Rollen
'''
i = 0
for liste in listen:
    if liste:
        listen2.append(liste)
        listenstrpl2.append(listenstrpl[i])
    i += 1

#Zurückbenennen der gerade umbenannten Listen (ohne Datenmüll zu hinterlassen)
listen = listen2
del listen2
listenstrpl = listenstrpl2
del listenstrpl2
'''

#Debug Modus (Mit anpassung von Singular-Plural und Der-Die-Das)
for i in range(0,len(listen)-1):
    if (listensp[i]):
        sp = "sind"
        ddd = "Die"
    else:
        sp = "ist"
        ddd = listenddd[i]
    print("%s %s %s: %s" % (ddd, listenstrpl[i], sp, listen[i]))

#Verlieben
if Amor:
    while 1:
        Verliebtenzahl = input("Wie viele Verliebte soll es geben? ")
        try:
            Verliebtenzahl = int(Verliebtenzahl)
            if Verliebtenzahl >= 2 and Verliebtenzahl <= 5:
                break
            else:
                print("Bitte gib eine Zahl zwischen 2 und 5 ein")
        except:
            print("Ungültige Eingabe!")
    print("Der Amor erwacht und zeigt mir %s Verliebte! " % Verliebtenzahl)
    i = 0
    while i < Verliebtenzahl:
        Verliebter = input("%s. Verliebter? " % str(i+1))
        if Verliebter in Spieler:
            if Verliebter in Verliebte:
                print("%s ist schon im Liebespaar" % Verliebter)
            else:
                Verliebte.append(Verliebter)
                i += 1
        else:
            print("Ungültiger Name")
    
#Erkennung ob man zu der Hexe "Das Opfer" oder "Die Opfer" sagen muss ohne zu verraten, dass eine Böse Fraktion Ausgestorben ist
boese = 0
opfer = 0
if Werwolf:
    boese += 1 
if Vampir:
    boese += 1 
    
#Nacht
while 1:
    gestorben = []
    wopfer = None
    vopfer = None
    hopfer = None
    print(Spieler)
    print("Das Dorf schläft ein")
    if Werwolf:
        if nacht == 1:
            print("Die Werwölfe erwachen und sehen sich!")
            zeit = int(len(Werwolf)*5)
            #time.sleep(zeit)
        else:
            print("Die Werwölfe erwachen!")
            while 1:
                wopfer = input("Wen möchten die Werwölfe reißen? ")
                if wopfer in Spieler:
                    if wopfer in Werwolf:
                        print("Dieser Spieler ist selbst ein Werwolf und kann nicht gerissen werden!")
                    else:
                        break
                else:
                    print("Ungültiger Name!")
        print("Die Werwölfe schlafen wieder ein")
    if Vampir:
        if nacht == 1:
            print("Die Vampire erwachen und sehen sich!")
            zeit = int(len(Vampir)*5)
            #time.sleep(zeit)
        else:
            print("Die Vampire erwachen!")
            while 1:
                vopfer = input("Wen möchten die Vampire beißen? ")
                if vopfer in Spieler:
                    if vopfer in Vampir:
                        print("Dieser Spieler ist selbst ein Vampir und kann nicht gebissen werden!")
                    else:
                        break
                else:
                    print("Ungültiger Name!")
        print("Die Vampire schlafen wieder ein")
    if Seherin:
        print("Die Seherin erwacht und darf sehen!")
        while 1:
            sehopfer = input("Wen möchte die Seherin sehen? ")
            i = 0
            if sehopfer in Spieler:
                for liste in listen:
                    for spieler in liste:
                        if spieler == sehopfer:
                            fraktion = listenstr[i]
                    i += 1
                break
            else:
                print("Ungültiger Name!")
        print(fraktion)
        print("Die Seherin hat ihr Zeichen bekommen und schläft wieder ein!")
    if Auge and nacht == 1:
        print("Das Auge erwacht und ich zeige dem Auge die Seherin")
        print(Seherin)
    if Hexe and nacht != 1:
        opfer += boese
        if opfer == 1:
            spl = "das"
        else:
            spl = "die"
        print("Die Hexe erwacht und sieht %s Opfer" % spl)
        hopfer = None
        print("Die Hexe schläft wieder ein!")

    print("Das Dorf erwacht!")
    if wopfer:
        sterben(wopfer)
        gestorben.append(wopfer)
    if vopfer:
        sterben(vopfer)
        gestorben.append(vopfer)
    if hopfer:
        sterben(hopfer)
        gestorben.append(hopfer)
    gestorben = set(gestorben)
    opfer = len(gestorben)
    if opfer == 0:
        print("Und es ist niemand gestorben")
    elif opfer == 1:
        print("Und es ist %s gestorben" % gestorben)
    else:
        print("Und es sind %s gestorben" % gestorben)
    spielende()
        
    nacht += 1
    opfer = 0
