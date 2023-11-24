import os
import re

class DataPengguna:
    def __init__(self):
        self.data = {'Nama': '', 'Email': '', 'Password': ''}

    def data_kosong(self):
        return all(value == '' for value in self.data.values())

    def tampilkan_detail(self):
        if self.data_kosong():
            print('Data saat ini kosong')
        else:
            for kunci, nilai in self.data.items():
                print(f'{kunci}: {nilai}')

    def ubah_nama(self):
        if self.data_kosong():
            print('Data saat ini kosong')
        else:
            nama_baru = input('Masukkan nama baru: ')
            self.data['Nama'] = nama_baru
            print('Nama berhasil diubah')

    def simpan_data(self):
        if self.data_kosong():
            print('Data saat ini kosong')
        else:
            namafile = input('Masukkan nama file tanpa (.txt): ') + '.txt'
            if os.path.exists(namafile):
                with open(namafile, 'a') as file:
                    for key, value in self.data.items():
                        file.write(f'|{key}: {value}\n')
                    file.write(f"+{'='*50}\n")

            else:
                with open(namafile, 'w') as file:
                    file.write(f"+{'='*50}\n")
                    file.write(f"|Data yang tersimpan\n")
                    file.write(f"+{'='*50}\n")
                
                    for key, value in self.data.items():
                        file.write(f'|{key}: {value}\n')
                    file.write(f"+{'='*50}\n")

    def data_baru(self):
        self.data['Nama'] = input("Masukkan Nama: ")
        while True:
            email = input("Masukkan Email: ")
            if re.match(r"[a-z0-9._%+-]+@student.unhas.ac.id$", email):
                break
            else:
                print("Email yang Anda masukkan salah. Silakan coba lagi.")
        self.data['Email'] = email

        while True:
            password = input("Masukkan Password: ")
            if (8 <= len(password) <= 20 and 
                any(char.isupper() for char in password) and 
                any(char.islower() for char in password) and 
                any(char.isdigit() for char in password)):
                break
            else:
                print("Password tidak memenuhi syarat. Silakan coba lagi.")
        self.data['Password'] = password
        print("Data berhasil dibuat")


def main():
    user_data = DataPengguna()

    while True:
        print(f"{'='*50}")
        print("Menu:")
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Jumlah Data pada File")
        print("4. Simpan Data pada File")
        print("5. Buat Data Baru")
        print("6. Keluar")
        print(f"{'='*50}")
        pilihan = input('Pilih menu yang Anda inginkan: ').lower()
        if pilihan == '1':
            user_data.tampilkan_detail()
        elif pilihan == '2':
            user_data.ubah_nama()
        elif pilihan == '3':
            nama_file = input("Masukkan nama file tanpa format (.txt): ") + '.txt'
            if not os.path.exists(nama_file):
                print(f"{'='*50}")
                print(f"Tidak terdapat file dengan nama {nama_file[:-4]}")
                print("Jumlah data pada file berjumlah 0")
            else:
                with open(nama_file, mode="r") as cari_data:
                    pattern_jumlah = re.findall(r"\|Nama: ", cari_data.read())
                    print(f"{'='*50}")
                    print("File Ditemukan")
                    print(f"Jumlah data pada file berjumlah {len(pattern_jumlah)}")
        elif pilihan == '4':
            user_data.simpan_data()
        elif pilihan == '5':
            user_data.data_baru()
        elif pilihan == '6':
            print('Sampai Jumpa Lagi')
            break
        else:
            print('Pilihan tidak valid. Masukkan pilihan yang benar (1-6).')

if __name__ == "__main__":
    main()