utang = int(input("Masukkan jumlah : "))
bayar = int(input("Masukkan jumlah : "))
kembalian = bayar - utang

k100 = 0
k50 = 0
k20 = 0
k10 = 0
k5 = 0
k2 = 0
k1 = 0

while kembalian != 0:
    if kembalian - 100000 >= 0:
        k100 += 1
        kembalian -= 100000
    elif kembalian - 50000 >= 0:
        k50 += 1
        kembalian -= 50000
    elif kembalian - 20000 >= 0:
        k20 += 1
        kembalian -= 20000
    elif kembalian - 10000 >= 0:
        k10 += 1
        kembalian -= 10000
    elif kembalian - 5000 >= 0:
        k5 += 1
        kembalian -= 5000
    elif kembalian - 2000 >= 0:
        k2 += 1
        kembalian -= 2000
    elif kembalian - 1000 >= 0:
        k1 += 1
        kembalian -= 1000
    else:
        break
if kembalian < 0:
    print("Uang tidak cukup")
else:
    print(f'{k100} uang sejumlah Rp. 100000')
    print(f'{k50} uang sejumlah Rp. 50000')
    print(f'{k20} uang sejumlah Rp. 20000')
    print(f'{k10} uang sejumlah Rp. 10000')
    print(f'{k5} uang sejumlah Rp. 5000')
    print(f'{k2} uang sejumlah Rp. 2000')
    print(f'{k1} uang sejumlah Rp. 1000')            