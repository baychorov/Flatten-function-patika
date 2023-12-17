#patika.dev python dersleri icin verilmis projedeki problemlerin cozumu. 

def flatter(lst):
  flatted_l = []
  for sublist in lst:
    if isinstance(sublist,list):
      flatted_l.extend(flatter(sublist))
    else:
      flatted_l.append(sublist)

  return flatted_l 

sample_l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatter(sample_l))
# isinstance() ve extend() metodlari sayesinde listenin icindeki alt listeler icinde iterasyon yapabildik
# ve her alt listeye girdigimizde kontrolun tekrar yapilmasini sagladik 
# eger girdigimiz alt liste bir elemansa dogrudan flat listemize ekledik 
# eger bir eleman degilse , alt listenin tekrardan flatter() fonksiyonuna girmis halini extend() metodu ile ekledik
# ve sonucu flatted_l listesi ile return ettik 

def reverser(lst):
  lst.reverse() 
  for i in range(len(lst)):
    if isinstance(lst[i],list):
      lst[i].reverse()
    else:
      pass
  return lst 


sample_list = [[1, 2], [3, 4], [5, 6, 7]]
print(reverser(sample_list))

#bu fonksiyonda reverse() ve isinstance() metodunu kullandik. her once ana listemizi tersine cevirip alt listeleri icinde gezdik 
#ve onlarida tersine cevirdik 

