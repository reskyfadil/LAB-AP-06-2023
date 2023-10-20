input = input("Masukkan beberapa angka: ")
angka = list(map(int, input.split()))

ganjil = []
genap = []
habis_dibagi_5 = []

for number in angka:
    if number % 2 == 1: 
        ganjil.append(number)
    if number % 2 == 0:
        genap.append(number)
    if number % 5 == 0:
        habis_dibagi_5.append(number)

print("Angka Genap:", genap)
print("Angka Ganjil:", ganjil)
print("Angka yang Habis Dibagi 5:", habis_dibagi_5)