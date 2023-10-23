data_pengguna = {}

if not data_pengguna:
    print("Selamat datang untuk memulai silahkan input data anda")
    nama = input("Input Nama : ")
    umur = input("Input Umur : ")
    alamat = input("Input Alamat : ")

    data_pengguna["nama"] = nama
    data_pengguna["umur"] = umur
    data_pengguna["alamat"] = alamat

def detail():
    print("Data anda adalah")
    print("Nama: ",data_pengguna["nama"])
    print("Umur: ",data_pengguna["umur"])
    print("Alamat: ",data_pengguna["alamat"])
    
while True:
    print("\n")
    print("="*50)
    print("Selamat datang", data_pengguna["nama"],"silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda ")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*50)
    print("\n")
    input_opsi = int(input("Input Opsi: "))
    print("\n")
    match input_opsi :
        case 1:
            detail()
        case 2:
            nama1 = input("Silahkan input nama baru: ")
            data_pengguna["nama"] = nama1
            print("Data anda sukses diperbarui")
        case 3:
            umur1 = input("Silahkan input umur baru: ")
            data_pengguna["umur"] = umur1
            print("Data anda sukses diperbarui")
        case 4:
            alamat1 = input("Silahkan input alamat baru: ")
            data_pengguna["alamat"] = alamat1
            print("Data anda sukses diperbarui")
        case 5:
            print("="*50)
            print("Selamat Tinggal ", data_pengguna["nama"])
            break
        case _:
            print("Input yang anda masukkan salah")