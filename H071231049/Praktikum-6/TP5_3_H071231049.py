angka = list(map(int, input("Masukkan beberapa angka : ").split()))

ganjil = [i for i in angka if i % 2 == 1]
genap = [i for i in angka if i % 2 == 0]
bisa_dibagi_5 = [i for i in angka if i % 5 == 0]

print("Angka genap :",genap)
print("Angka ganjil :",ganjil)
print("Angka yang habis dibagi 5 :",bisa_dibagi_5)
       
    

      
      