def maksimum(daftar):
    try:
        angka_terbesar = daftar[0]

        for angka in daftar:
            if angka > angka_terbesar:
                angka_terbesar = angka
        return angka_terbesar

    except IndexError as err:
        print(err)

# print(maksimum(1,2,4,6,9,3,1,9,10))
# print(maksimum(0,1,90,430,23,212,34))
print(maksimum(list(map(int, input().split(',')))))                