print('================================')
print('Menghitung Total Tagihan Listrik')
print('================================\n')

gol = input(" Golongan = ")
if gol not in ['R1', 'R2', 'R3', 'B2', 'B3', 'I3', 'P1']:
    print("Data tidak valid")
    exit()    
    
daya = input(" Daya = ")
daya = int(daya)

match gol:
    case 'R1':
        if daya == 900:
            TARIF = 1352
        elif daya == 1300 or daya == 2200:
            TARIF = 1444.70
        else:
            print("Data invalid.")
            exit()

    case 'R2':
        if 3500 <= daya <= 5500:
            TARIF = 1699.53
        else:
            print("Data invalid.")
            exit()

    case 'R3':
        if daya >= 6600:
            TARIF = 1699.53
        else:
            print("Data invalid.")
            exit()

    case 'B2':
        if 6600 <= daya <= 200000:
            TARIF = 1444.70
        else:
            print("Data invalid.")
            exit()

    case 'B3':
        if daya > 200000:
            TARIF = 1114.74
        else:
            print("Data invalid.")
            exit()

    case 'I3':
        if daya >= 200000:
            TARIF = 1314.12
        else:
            print("Data invalid.")
            exit()

    case 'P1':
        if 6600 <= daya <= 200000:
            TARIF = 1523.28
        else:
            print("Data invalid.")
            exit()

    case _:
        print("Data tidak valid")
        exit()
        
pakai = input("Pemakaian = ")
pakai = int(pakai)
tagihan = (TARIF * pakai)
depan,koma = str(tagihan).split('.')
depan = int(depan)
depan = f"{depan:,}".replace(',','.')
koma = int(koma)
print(f'Pemakaian = Jumlah tagihan Anda sebesar : Rp{depan},{koma}')