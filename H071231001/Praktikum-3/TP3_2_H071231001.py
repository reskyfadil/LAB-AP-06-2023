try:
    h = int(input("Masukkan Harga Barang = "))
    b = int(input("Masukkan Nilai Uang yang dibayarkan = "))
except ValueError:
    print("Masukkan harus berupa angka")

print()

kembalian = b - h
uang = 0
sisa = 0

for i in range(1, 8) :
    match (i) :
        case 1 :
            uang = kembalian // 100000
            print(uang , " uang Rp. 100.000")
            
        case 2 :
            sisa = kembalian - (uang * 100000)
            uang = sisa // 50000
            print(uang , " uang Rp. 50.000")
            
        case 3 :
            sisa = sisa - (uang * 50000)
            uang = sisa // 20000
            print(uang , " uang Rp. 20.000")
            
        case 4 :
            sisa = sisa - (uang * 20000)
            uang = sisa // 10000
            print(uang , " uang Rp. 10.000")
            
        case 5 :
            sisa = sisa - (uang * 10000)
            uang = sisa // 5000
            print(uang , " uang Rp. 5.000")
            
        case 6 :
            sisa = sisa - (uang * 5000)
            uang = sisa // 2000
            print(uang , " uang Rp. 2.000")
            
        case 7 :
            sisa = sisa - (uang * 2000)
            uang = sisa // 1000
            print(uang , " uang Rp. 1.000")
            
            