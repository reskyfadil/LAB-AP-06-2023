# 1 hari = 360 derajat
# 1 hari = 24 jam
# 1 jam = 3600
# 24 jam = 3600 * 24
# 24 jam/hari = 86400 detik
# 1 derajat = 86400 / 360 
# 1 derajat = 240 detik


while True:
    try :
        derajat = float(input("Masukkan nilai = "))

        if derajat < 0 or derajat > 360:
            print("Masukkan nilai yang valid (0-360) = ")
            continue

        detik_per_derajat = int(derajat * 240)
        menit = (detik_per_derajat // 60) % 60
        detik = detik_per_derajat % 60
        jam = int((detik_per_derajat // 3600 + 6) % 24)

        hasil = f"{jam:02}:{menit:02}:{detik:02}"
        print(hasil)

        if 0 <= jam < 12:
            print("Selamat pagi")
        elif 12 <= jam < 18:
            print("Selamat sore")
        else:
            print("Selamat malam")
    
    except:
        print("Masukkan Angka")
        break
    
































