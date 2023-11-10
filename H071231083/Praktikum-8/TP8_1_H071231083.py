import re

S = input("Masukkan String Anda : ")
x = re.match(r"[A-z2468]{40}[13579\s]{5}$", S)
if x:
    print("True")
else:
    print("False")
