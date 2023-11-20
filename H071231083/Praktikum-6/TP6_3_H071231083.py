angka = input("Masukkan beberapa angka : ").split()
angka = list(map(int, angka))

genap = []
ganjil = []
habis5 = []

for i in angka:
    if i % 2 == 0:
        genap.append(i)
    if i % 2 != 0 :
        ganjil.append(i)
    if i % 5 == 0:
        habis5.append(i)
print(f"\nAngka genap : {genap}\nAngka ganjil : {ganjil}\nAngka yang habis dibagi 5 : {habis5}")
