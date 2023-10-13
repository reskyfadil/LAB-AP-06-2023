golongan = input("Golongan  = ")
daya = float(input("Daya = "))
pemakaian = float(input("Pemakaian = "))

match golongan:
    case "R1":
        if daya == 900:
            tagihan = pemakaian * 1352
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        elif daya == 1300:
            tagihan = pemakaian * 1444.70
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        elif daya == 2200:
            tagihan = pemakaian * 1444.70
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")
    case "R2":
        if 3500 <= daya <= 5500:
            tagihan = pemakaian * 1699.53
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")
    case "R3":
        if daya >= 6600:
            tagihan = pemakaian * 1699.53
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")
    case "B2":
        if 6600 <= daya <= 200000:
            tagihan = pemakaian * 1444.70
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")        
    case "B3":
        if daya > 200000:
            tagihan = pemakaian * 1114.74
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")
    case "I3":
        if daya >= 200000:
            tagihan = pemakaian * 1314.12 
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")
    case "P1":
        if 6600 <= daya <= 2000000:
            tagihan = pemakaian * 1523.28
            print(f"Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid")
    case _:
        print("Data tidak valid")                                




