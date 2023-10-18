def nilai_terbesar(a):
    paling_besar=a[2]
    for angka in a:
        if angka > paling_besar:
            paling_besar = angka
    return paling_besar

a = [-3, -45, -22, -10, 1]
print(nilai_terbesar(a))