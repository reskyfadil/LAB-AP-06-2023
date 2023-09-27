while True:
    try:
        derajat = float(input(""))
        total_detik = int(derajat * 240 + 21600) % 86400
        jam = total_detik // 3600
        menit = total_detik % 3600 // 60
        detik = total_detik % 60

        if 6 <= jam < 12:
            print("Selamat pagi")
        elif 12 <= jam < 15:
            print("Selamat siang")
        elif 15 <= jam < 18:
            print("Selamat sore")
        else:
            print("Selamat malam")
        print(f"{jam:02}:{menit:02}:{detik:02}")
    except:
        print("End of file")
        break