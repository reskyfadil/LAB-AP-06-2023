list_angka=list(map(int,input("Masukkan beberapa angka: ").split()))

genap=[]
ganjil=[]
habis_dibagi_lima=[]

for angka in list_angka:
    if angka%2==0:
        genap.append(angka)
    else:
        ganjil.append(angka)
    if angka%5==0:
        habis_dibagi_lima.append(angka)
        
print(f"Angka Genap: {genap}")
print(f"Angka Ganjil: {ganjil}")
print(f"Angka yang habis dibagi 5: {habis_dibagi_lima}")