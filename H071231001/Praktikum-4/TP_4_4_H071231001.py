#A adalah kucing A
#B adalah kucing B
#C adalah tikus

def catAndMouse(A:int,B:int,C:int)->str :
  if abs(C-B)<abs(C-A):
    print("Cat B")
  elif abs(C-B)>abs(C-A):
    print("Cat A")
  elif abs(C-B)==abs(C-A) :
    print("Mouse C")

catAndMouse(1,5,4)