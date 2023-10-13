try:
    x = int(input("Masukkan Input = "))
except ValueError:
    print("Masukkan harus berupa angka")

angka0 = 0
angka1 = 1
jumlah = 0

i = 0

while i < x:
    i += 1
    angka0 = angka1
    angka1 = jumlah
    print(jumlah, end=" ")
    jumlah = angka0 + angka1