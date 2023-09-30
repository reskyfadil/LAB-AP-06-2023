try:
    while True:
        derajat = float(input())  

        total_detik = int((derajat / 360) * 86400)
        jam = (total_detik // 3600 + 6) % 24  
        menit = (total_detik // 60) % 60  
        detik = total_detik % 60  
        waktu = f"{jam:02d}:{menit:02d}:{detik:02d}"  

        if 6 <= jam < 12:
            sapa = "Selamat pagi"
        elif 12 <= jam < 15:
            sapa = "Selamat siang"
        elif 15 <= jam < 18:
            sapa = "Selamat sore"
        else:
            sapa = "Selamat malam"

        print(sapa)  
        print(waktu)  
except :
    print("End of File")