import random
import sys
import getpass

nowins=0
pwins=0
cwins=0

def uinput(text):
  return getpass.getpass(text)

def gewinner(p,c):
  if p==c:
    winner="n"
  elif(
    (p=="Stein" and (c=="Schere" or c=="Streichholz" or c=="Feuer")) or
    (p=="Papier" and (c=="Stein" or c=="Brunnen" or c=="Wasser")) or
    (p=="Schere" and (c=="Papier" or c=="Streichholz" or c=="Wasser")) or
    (p=="Brunnen" and (c=="Schere" or c=="Stein" or c=="Wasser")) or
    (p=="Streichholz" and (c=="Papier" or c=="Brunnen" or c=="Wasser")) or
    (p=="Feuer" and (c=="Schere" or c=="Papier" or c=="Streichholz")) or
    (p=="Wasser" and (c=="Stein" or c=="Brunnen" or c=="Feuer"))
  ):
    winner="p"
  else:
    winner="c"

  return winner

print("Willst du mit einer Erweiterung spielen?(0 für nein)")
print("Wenn ja, mit welcher Erweiterung? Bitte eine ganze Zahl.")
erw=int(input("1 für Brunnen und Streichholz und 2 für Brunnen, Streichholz, Feuer und Wasser.   "))
Elemente=["Schere","Stein","Papier"]
if erw >= 1:
  Elemente.append("Brunnen")
  Elemente.append("Streichholz")
if erw == 2:
  Elemente.append("Feuer")
  Elemente.append("Wasser")
cop=input("Willst du gegen einen zweiten Spieler statt gegen den Computer spielen? (j/n)   ")
if cop == "j":
  pn="Spieler1"
  cn="Spieler2"
else:
  pn="Spieler"
  cn="Computer"
runden=int(input("Wie viele Runden muss man gewinnen?   "))

while 1:
  if erw == "0":
    p=int(uinput("%s, Nimmst du Schere(1), Stein(2) oder Papier(3)?   " % pn))
    if cop == "j":
      c=int(uinput("Spieler2, Nimmst du Schere(1), Stein(2) oder Papier(3)?   "))
    else: 
      c=random.randint(1,3)
  elif erw == "1":
    p=int(uinput("%s, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4) oder Streichholz(5)?   " % pn))
    if cop == "j":
      c=int(uinput("Spieler2, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4) oder Streichholz(5)?   "))
    else:
      c=random.randint(1,5)
  else:
    p=int(uinput("%s, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4), Streichholz(5), Feuer(6) oder Wasser(7)?   " % pn))
    if cop == "j":
      c=int(uinput("Spieler2, Nimmst du Schere(1), Stein(2), Papier(3), Brunnen(4), Streichholz(5), Feuer(6) oder Wasser(7) ?   "))
    else:
      c=random.randint(1,7)

  print(Elemente,p,c)
  p=Elemente[p-1]
  c=Elemente[c-1]
  
  winner=gewinner(p,c)
  
  if winner == "p":
    winner=pn
    pwins+=1
  elif winner == "c":
    winner=cn
    cwins+=1
  else:
    winner="keiner"
    nowins+=1

  print("%s hat %s gewählt und %s hat %s gewählt und desswegen hat %s die Runde gewonnen." %(pn,p,cn,c,winner))
  print("%s hat nun %s mal gewonnen und %s %s mal. Es muss %s mal gewonnen werden." %(pn,pwins,cn,cwins,runden))
  if pwins >= runden:
    ewinner=pn
    break
  elif cwins >= runden:
    ewinner=cn
    break

print("Damit hat %s das Spiel gewonnen." % ewinner)
