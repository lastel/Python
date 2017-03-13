
class Quicksort:
  def finde_mitte(self,liste):
    if len(liste)%2 == 0:
      mitte=int(len(liste)/2)-1
      print("Gerade")
    else:
      mitte=int(len(liste)/2)
      print("Ungerade")
    melement=liste[mitte]
    return melement

  def sortiere(self,liste):
    pivot=self.finde_mitte(self,liste)
    links=[]
    rechts=[]
    for i in range(len(liste)):
      if liste[i] == pivot:
        pass
      elif liste[i] <= pivot:
        links.append(liste[i])
      else:
        rechts.append(liste[i])
    
