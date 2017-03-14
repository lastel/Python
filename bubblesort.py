class Bubblesort:
  def sortiere(self,liste):
    wechsel=False
    for i in range(len(liste)-1):
      if liste[i] > liste[i+1]:
        liste[i],liste[i+1] = liste[i+1],liste[i]
        wechsel=True
    if wechsel != True:
      print(liste)
    else:
      self.sortiere(self,liste)