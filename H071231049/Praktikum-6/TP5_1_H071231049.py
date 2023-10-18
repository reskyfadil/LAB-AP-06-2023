data = {
    "Nama" : input("Input Nama   = "),
    "Umur" : input("Input Umur   = "),
    "Alamat" : input("Input Alamat = ")
}
while True:
    print(50*"="+"\n Selamat datang",data["Nama"],"silakan pilih opsi\n"+50*"=")
    pilih = """
1. Detail anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
    """
    print(pilih)
    print(50*"=")
    pilihan = input('Input opsi : ')
    print(50*"=")

    if (pilihan == "1"):
       data_diri = f"""Data anda adalah
Nama   = {data["Nama"]}
Umur   = {data["Umur"]}
Alamat = {data["Alamat"]}"""
       print(data_diri)
    elif (pilihan == "2"):
        nama_baru = input("Silakan input nama baru : ")
        data["Nama"] = nama_baru
        print("Data anda sukses diperbarui")
    elif (pilihan == "3"):
        umur_baru = input("Silakan input umur baru : ")
        data["Umur"] = umur_baru
        print("Data anda sukses diperbaru")
    elif (pilihan == "4"):
        alamat_baru = input("Silakan input alamat baru : ")
        data["Alamat"] = alamat_baru
        print("Data anda sukses diperbarui")
    elif (pilihan == "5"):
        print("Selamat Tinggal",data["Nama"])
        break
    else:
        print("Opsi tidak ditemukan, silakan pilih opsi 1-5\n"+50*"=")