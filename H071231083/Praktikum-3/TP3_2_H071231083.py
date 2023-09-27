harga_barang = int(input())
uang = int(input())

kembalian = uang - harga_barang
if kembalian < 0:
    print("uang kurang!")
else:
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    for x in range(0, 7):
        jumlah = kembalian // (pecahan[x])
        kembalian = kembalian - jumlah * (pecahan[x])
        print(f"{jumlah} uang sejumlah Rp.{pecahan[x]}")