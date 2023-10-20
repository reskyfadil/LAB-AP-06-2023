dictio = {"nama":"", "umur":"","alamat":""}
print("Selamat datang untuk memulai silahkan input data anda")
dictio["nama"] = input("Input nama : ").title()
dictio["umur"] = int(input("Input umur : "))
dictio["alamat"] = input("Input alamat : ")
while True:
    print(f'{"="*45}\nSelamat datang {dictio["nama"]} silahkan pilih opsi\n{"="*45}\n1.Detail Anda\n2.Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar\n{"="*45}')

    pilihan = int(input("Input Opsi: "))

    match pilihan:
        case 1:
            print(f'{"="*45}\nData anda adalah :\nNama : {dictio["nama"]}\nUmur : {dictio["umur"]}\nAlamat : {dictio["alamat"]}') 
        case 2:
            dictio["nama"] = input("Silahkan input nama baru: ").title()
            print("Data anda sukses di perbarui")
        case 3:
            dictio["umur"] = input("Silahkan input umur baru: ")
            print("Data anda sukses di perbarui")
        case 4:
            dictio["alamat"] = input("Silahkan input alamat baru: ")
            print("Data anda sukses di perbarui")
        case 5:
            print(f"Selamat Tinggal {dictio['nama']}")
            break
        case _:
            break