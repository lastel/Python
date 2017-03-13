
class Quicksort:
  def finde_mitte(self,liste):
    if len(liste)%2 == 0:
      mitte=int(len(liste)/2)-1
    else:
      mitte=int(len(liste)/2)
    melement=liste[mitte]
    return melement

  def sortiere(self,liste):
    if len(liste) > 1:
      pivot=self.finde_mitte(self,liste)
      links=[]
      rechts=[]
      for el in liste:
        if el == pivot:
          pass
        elif el <= pivot:
          links.append(el)
        else:
          rechts.append(el)
      return self.sortiere(self,links) + [pivot] + self.sortiere(self,rechts)
    return liste