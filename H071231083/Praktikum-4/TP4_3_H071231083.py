def terbesar(a):
    max_angka = a[0]
    for angka in a:
        if angka > max_angka:
            max_angka = angka
    return max_angka

angka = [1, 2, 4, 6, 9, 3, 1, 9, 10]
print(terbesar(angka))