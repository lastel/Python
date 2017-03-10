import random

listenlänge=10
liste1=[]
liste2=[]
score=0

def listen(liste1,liste2):
  for i in range(0,listenlänge):
    liste1.append(i+1)
  for i in range(0,len(liste1)):
    a=random.choice(liste1)
    liste1.remove(a)
    liste2.append(a)

listen(liste1,liste2)
zahl1=(liste2[0])
print(zahl1)
liste2.remove(zahl1)

def punkteberechnung(score,input1,zahl1,zahl2):
  if (zahl1>zahl2 and input1==">") or (zahl1<zahl2 and input1=="<"):
    score+=1
    print("Damit krigst du einen Punkt")
  else:
    print("Damit krigst du keinen Punkt")
  return score

def spiel(liste2,zahl1,score):
  input1=input("Denkst du, dass die nächste Zahl größer oder kleiner als diese Zahl ist(</>)?   ")
  zahl2=liste2[0]
  print(zahl2)
  if zahl1<zahl2:
    vergleich="größer"
  else:
    vergleich="kleiner"
  print("Die letzte Zahl war %s und nächste Zahl ist %s also %s" %(zahl1,zahl2,vergleich))
  score=punkteberechnung(score,input1,zahl1,zahl2)
  zahl1=zahl2
  liste2.remove(zahl2)
  return liste2,zahl1,score

while len(liste2) > 0:
  rückgabe=spiel(liste2,zahl1,score)
  liste2=rückgabe[0]
  zahl1=rückgabe[1]
  score=rückgabe[2]


print("Du hast %s Punkte"% score)
