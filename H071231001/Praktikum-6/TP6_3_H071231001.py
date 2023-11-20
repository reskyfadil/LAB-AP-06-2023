angka = list(map(int,input("masukkan beberapa angka : ").split()))
ganjil = []
genap = []
habis5 = []
for i in angka:
    if i%2==0:
        genap.append(i)
    else:
        ganjil.append(i)
    if i%5==0:
        habis5.append(i)
print(f"Angka Genap: {genap}")
print(f"Angka Ganjil: {ganjil}")
print(f"Angka yang habis dibagi 5: {habis5}")