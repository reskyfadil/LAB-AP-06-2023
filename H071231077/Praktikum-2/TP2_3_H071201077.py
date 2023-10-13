gol = input("Golongan = ")
daya = int(input("Daya = "))
p = int(input("Pemakaian = "))

match gol, daya:
    case "R1", 900:
        tagihan = p * 1352
        print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 1300:
        tagihan = p * 1444.70
        print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 2200:
        tagihan = p * 1444.70
        print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R2", daya:
        if daya >= 3500 and daya <= 5500:
            tagihan = p * 1699.53
            print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("tidak valid!")
    case "R3", daya:
        if daya >= 6600:
            tagihan = p * 1699.53
            print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("tidak valid!")
    case "B2", daya:
        if daya >= 6600 and daya <= 200000:
            tagihan = p * 1444.70
            print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("tidak valid!")
    case "B3", daya:
        if daya > 200000:
            tagihan = p * 1114.74
            print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("tidak valid!")
    case "I3", daya:
        if daya >= 200000:
            tagihan = p * 1314.12
            print(f"Jumlah tagihan sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("tidak valid!")
    case "P1", daya:
        if daya >= 6600 and daya <= 200000:
            tagihan = p * 1523.28
            print(f"Jumlah tagihan anda sebesar : Rp{tagihan:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("tidak valid!")
    case _:
        print("tidak valid!")

