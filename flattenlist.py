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
