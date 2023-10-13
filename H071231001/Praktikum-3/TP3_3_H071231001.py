while True:
    try :
        posisi = float(input("Masukkan derajat posisi matahari : "))
        if posisi < 0:
            break
        elif posisi > 360:
            posisi -= 360
        detik = (posisi / 360) * 24 * 3600
        jam = (detik // 3600) + 6 
        if jam >= 24:
            jam %= 24
        detik %= 3600
        menit = detik // 60
        detik %= 60
        if 6 <= jam < 10:
            print('Selamat Pagi')
        elif 10 <= jam < 15:
            print('Selamat Siang')
        elif 15 <= jam < 18:
            print('Selamat Sore')
        elif 18 <= jam < 24 or 0 <= jam <6:
            print('Selamat Malam') 

        print(f'{jam:02.0f}:{menit:02.0f}:{detik:02.0f}')   
    except ValueError :
        print("End Of File")
    break