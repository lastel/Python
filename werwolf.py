import sys
import time

#anzahl = int(input("Anzahl der Spieler? "))
Werwolf = []
Vampir = []
Amor = []
Dorfbewohner = []
Seherin = []
Auge = []
Hexe = []
listen = [Werwolf,Vampir,Amor,Dorfbewohner,Seherin,Auge,Hexe]
listen2 = []
listenddd = ["Der","Der","Der","Der","Die","Das","Die"]
listenstr = ["Werwolf","Vampir","Amor","Dorfbewohner","Seherin","Auge","Hexe"]
listenstrpl = ["Werwölfe","Vampire","Amor","Dorfbewohner","Seherin","Auge","Hexe"]
listensp = [1, 1, 0, 1, 0, 0, 0]
listenstrpl2 = []
Verliebte = []
listendddklein = []
nacht = 1

#for i in range(anzahl):
#    input("")

for i in listenddd:
    x = i.lower()
    listendddklein.append(x) 

x = 0
for liste in listen:
    i = 0
    while 1:
        i += 1
        if listensp[x] == 1:
            name = input("Wie heißt %s %s? " % (listenstr[x], i))
        else:
            name = input("Wie heißt %s %s? " % (listendddklein[x],listenstr[x]))
        if name:
            liste.append(name)
            if listensp[x] == 0:
                break
        else:
            break
    x += 1

i = 0
for liste in listen:
    if liste:
        listen2.append(liste)
        listenstrpl2.append(listenstrpl[i])
    i += 1

listen = listen2
del listen2
listenstrpl = listenstrpl2
del listenstrpl2

for i in range(0,len(listen)-1):
    if (listensp[i]):
        sp = "sind"
        ddd = "Die"
    else:
        sp = "ist"
        ddd = listenddd[i]
    print("%s %s %s: %s" % (ddd, listenstrpl[i], sp, listen[i]))

if Amor:
    Verliebtenzahl = int(input("Wie viele Verliebte soll es geben? "))
    print("Der Amor erwacht und zeigt mir %s Verliebte! " % Verliebtenzahl)
    for i in range(Verliebtenzahl):
        Verliebter = input("%s. Verliebter " % str(i+1))
        Verliebte.append(Verliebter)
    

boese = 0
opfer = 0
if Werwolf:
    boese += 1 
if Vampir:
    boese += 1 
    

while 1:
    if Werwolf:
        if nacht == 1:
            print("Die Werwölfe erwachen und sehen sich!")
            zeit = int(len(Werwolf)*5)
            time.sleep(zeit)
        else:
            print("Die Werwölfe erwachen!")
            wopfer = input("Wen möchten die Werwölfe reißen? ")
        print("Die Werwölfe schlafen wieder ein")
    if Vampir:
        if nacht == 1:
            print("Die Vampire erwachen und sehen sich!")
            zeit = int(len(Vampir)*5)
            time.sleep(zeit)
        else:
            print("Die Vampire erwachen!")
            vopfer = input("Wen möchten die Vampire beißen? ")
        print("Die Vampire schlafen wieder ein")
    if Seherin:
        print("Die Seherin erwacht und darf sehen!")
        sehopfer = input("Wen möchte die Seherin sehen? ")
        i = 0
        for liste in listen:
            for spieler in liste:
                if spieler == sehopfer:
                    fraktion = listenstr[i]
            i += 1
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
        
    nacht += 1
    opfer = 0
