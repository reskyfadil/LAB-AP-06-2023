def Palindrom(kata: str)->str:
  reverse = kata[::-1]
  jumlah = 0
  for i in range(len(kata)) :
    if kata[i] == reverse[i]:
      jumlah += 1
  if jumlah == len(kata):
    print("palindrom")
  else :
    print("bukan palindrom")

Palindrom("kasurrusak")
