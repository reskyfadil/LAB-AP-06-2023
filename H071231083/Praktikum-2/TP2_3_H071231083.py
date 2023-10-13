#Input data
golongan = input("Golongan = ")
daya = int(input("Daya = "))
pemakaian = int(input("pemakaian = "))

#Tipe Golongan
R1 = 1352
R1_1 = B2 = 1444.70
R2 = R3 = 1699.63
B3 = 1114.74
I3 = 1314.72
P1 = 1523.28
 
#Menggunakan match case untuk memeriksa golongan
match golongan:
    case "R1":
        if daya == 900:
           t = pemakaian * R1
           print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        elif daya == 1300 or daya == 2200:
            t = pemakaian * R1_1
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case "R2":
        if daya >=3500 and daya <=5500:
            t = pemakaian * R2
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case "R3":
        if daya >=6600:
            t = pemakaian * R3
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case "B2":
        if daya >=6600 and daya <=200000:
            t = pemakaian * B2
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case "B3":
        if daya >200000:
            t = pemakaian * B3
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case "I3":
        if daya >=200000:
            t = pemakaian * I3
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case "P1":
        if daya >=6600 and daya <=200000:
            t = pemakaian * P1  
            print(f"jumlah tagihan anda sebesar : Rp{t:,.1f}".replace(",", "x").replace(".", ",").replace("x", "."))
        else:
            print("daya tidak sesuai!")
    case _: 
        print("data tidak valid!")