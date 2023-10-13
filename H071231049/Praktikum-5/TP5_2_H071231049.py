inputannya = input("Masukkan kata : ")
panjang = len(inputannya)
if panjang % 2 == 0:
    genap = inputannya[0] + inputannya[len(inputannya)//2-1] + inputannya[len(inputannya)//2] + inputannya[-1]
    print(genap)
else:
    ganjil = inputannya[0] + inputannya[len(inputannya)//2] + inputannya[-1]
    print(ganjil)

