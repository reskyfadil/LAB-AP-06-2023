def karakter(s):
    karakter_pertama = s[0]
    indeks_tengah = len(s) // 2
    karakter_terakhir = s[-1]

    if len(s) % 2 == 0:
        karakter_tengah = s[indeks_tengah -1 : indeks_tengah +1]
    else:
        karakter_tengah = s[indeks_tengah]
    return karakter_pertama + karakter_tengah + karakter_terakhir

s = input("Masukkan kata : ")
print(karakter(s))