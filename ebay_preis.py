from bs4 import BeautifulSoup
import urllib.request
import time

website=input("Wie heißt die Website?   ")



database=file("test.txt")

preis="EUR 4.300,00"
zeit="17T 05Std"
zeit=str.replace(zeit," ","")
i=1

def aufrufen(database,website):
  t = urllib.request.urlopen(webseite)

  soup = BeautifulSoup(t, 'html.parser')

  a=soup.find(id="vi-cdown_timeLeft")
  b=soup.find(id="prcIsum")
  b=b.string

  a=str.replace(a.string,"	","")
  a=str.replace(a," ","")
  schreiben(b,database)

def schreiben(b,database):
  print(b)
  database.write(b)
  database.write("\n")

for i in range(0,10):
  time.sleep(2)
  aufrufen(database)
