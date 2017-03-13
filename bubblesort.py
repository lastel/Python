class Bubblesort:
  def sortiere(self,liste):
    for i in range(len(liste)-1):
      for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
          liste[i],liste[i+1] = liste[i+1],liste[i]
      print(liste)
    return liste