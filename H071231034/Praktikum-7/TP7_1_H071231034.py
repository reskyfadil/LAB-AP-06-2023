import os
from datetime import datetime
import random

def trx_baru(n, x, t): # 'n' untuk parameter ID; 'x' untuk parameter list data produk; dan 't' untuk parameter total harga produk
    if len(x) == 0: # Jika 'x' kosong alias user tidak tambah produk, maka list data produk dikosongkan
        data_produk = []
    else: # Jika user tambah produk, maka list produk sama dengan list data produk sebelumnya (rekursi)
        data_produk = x
    data_tr = [] # List data transaksi akan selalu dikosongkan

    print(f"{'=' * 50}")
    nama_produk = input('Masukkan nama produk        : ').capitalize()
    while True:
        try:
            harga_produk = input('Masukkan harga produk       : ')
            if len(str(harga_produk)) < 3 or harga_produk[0] == '0': # Memastikan harga minimal ratusan, berupa integer, dan tidak dimulai dari nol
                raise Exception('\nHarga produk invalid!\n')
            harga_produk = int(harga_produk)
            break
        except ValueError:
            print('\nHarga produk invalid!\n')
        except Exception as ex:
            print(ex)
    while True:
        try:
            jumlah_produk = input('Masukkan jumlah produk      : ')
            if jumlah_produk[0] == '0':
                raise ValueError
            jumlah_produk = int(jumlah_produk)
            print(f"{'=' * 50}")
            break
        except ValueError:
            print('\nJumlah produk invalid!\n')
    harga_total = int(harga_produk * jumlah_produk) # Total harga setiap produk
    TOTAL = t; TOTAL += harga_total ; RpTOTAL = f'Rp{TOTAL}'# Total harga semua produk

    nama_no_spasi = nama_kasir.replace(' ','') # Nama untuk ID
    tgl_dan_waktu = datetime.now().strftime("%d/%m/%y %H:%M") # Tanggal dan waktu untuk tabel
    if len(nama_no_spasi) <= 3: # ID dari nama jika panjang nama kasir kurang atau sama dengan tiga karakter.
        ID_nama = nama_no_spasi.upper()
    else:
        ID_nama = (nama_no_spasi[0] + nama_no_spasi[len(nama_no_spasi) // 2] + nama_no_spasi[-1]).upper() # ID dari nama kasir jika panjang nama kasir lebih dari tiga karakter
    ID_tgl_waktu = datetime.now().strftime("%m%y%d%H%M") # ID dari tanggal dan waktu
    ID_angka = str(random.randint(100, 999)) # ID dari tiga angka acak
    if len(n) == 1:
        ID = ID_nama + ID_tgl_waktu + ID_angka # ID jika user telah melakukan transaksi
    else:
        ID = n # ID jika user ingin tambah produk

    data_produk.append([nama_produk, f'Rp{harga_produk}', jumlah_produk, f'Rp{harga_total}']) # Menampung data produk dari user
    data_tr.append([tgl_dan_waktu, ID, f'Rp{TOTAL}']) # Menampung data riwayat transaksi user
    
    while True:
        try:
            tp = input('Tambah produk? (y / t)      : ').lower() # Menentukan apakah user ingin tambah produk
            if tp == 't':
                print(f"{'=' * 50 }\n" + 'TRANSAKSI BERHASIL'.center(50) + f"\n{'=' * 50 }")
                nama_folder = 'Invoices' # Membuat nama dir / folder
                file_path = f'{nama_folder}/{ID}.txt' # Membuat file path (tempat beserta nama file)
                if os.path.exists(nama_folder) == False: # Cek apakah dir / folder sudah ada
                    os.mkdir(nama_folder) # Membuat dir baru
                with open(file_path, 'a') as fh: # Open file
                    # Membuat tabel untuk invoices
                    fh.write('\n' + f"TOKO {nama_kasir.upper()}".center(66)) 
                    fh.write(f"\n{'=' * 66}\nNama kasir         : {nama_kasir}\nWaktu transaksi    : {tgl_dan_waktu}\n{'=' * 66}")
                    fh.write('\n\n' + 'Daftar Produk'.center(66) + '\n')
                    fh.write(f"""
    {'=' * 58}
    |        Nama        |    Harga   | Jumlah |    Total    |
    {'=' * 58}""") # Format head table Daftar Produk
                    for i in range(len(data_produk)):
                        nama = data_produk[i][0][:15] + '...' if len(data_produk[i][0]) > 15 else data_produk[i][0][:15]
                        fh.write(f"\n    | {nama:<18} |" + f" {data_produk[i][1]:>10} |" + f" {data_produk[i][2]:^6} " + f"| {data_produk[i][3]:>11} |")
                    fh.write('\n' + f"{'=' * 58}".center(66))
                    fh.write('\n' + f'    |       TOTAL                              | {RpTOTAL:>11} |' + '\n')
                    fh.write(f"{'=' * 58}".center(66) + f"\n\n{'=' * 66}\n" + 'TERIMA KASIH TELAH BERBELANJA'.center(66) + f"\n{'=' * 66}")

                trx_file = 'trx_history.txt' # Membuat file untuk riwayat transaksi
                if os.path.exists(trx_file) == False: # Cek apakah file sudah ada
                    # Membuat tabel riwayat transaksi jika file belum ada
                    with open(trx_file, 'a') as tr:
                        tr.write(f"""
{'=' * 80}
|                              RIWAYAT TRANSAKSI                               |
{'=' * 80}
| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |
{'=' * 80}
""") # Format tabel riwayat transaksi jika filenya belum ada
                        for i in range(len(data_tr)):
                            tr.write(f"""
| {data_tr[i][0]:^20} | {data_tr[i][1]:^20} | {data_tr[i][2]:>30} |
{'=' * 80}""")
                    break
                else: # Membuat tabel riwayat transaksi jika file belum ada
                    with open(trx_file, 'a') as tr:
                        for i in range(len(data_tr)):
                            tr.write(f"""
| {data_tr[i][0]:^20} | {data_tr[i][1]:^20} | {data_tr[i][2]:>30} |
{'=' * 80}""") # Format tabel riwayat transaksi jika file sudah ada
                    break
            elif tp == 'y':
                trx_baru(ID, data_produk, TOTAL) # Jika user ingin menambahkan produk, maka terjadi rekursi dengan menggunakan ID dan list data produk sebelumnya
                break
            else: # Memastikan user hanya menginput opsi 'y' atau 't'
                raise Exception(f"{'=' * 50}\nHanya ada opsi 'y' dan 't'!\n")
        except Exception as ex:
            print(ex)

def cek_trx():
    while True:
        try:
            id = input(f"{'=' * 50}\nMasukkan ID transaksi       : ")
            file_path = f'Invoices/{id}.txt'
            if os.path.exists(file_path): # Mencari file berdasarkan ID yang dimasukkan
                print(f"{'_' * 66}")
                with open(file_path, 'r') as fh:
                    print(fh.read())
                print(f"{'_' * 66}")
                break
            else: 
                raise Warning(f"{'=' * 50}\nID invalid!\n")
        except Warning as wr:
            print(wr)

print(f"{'=' * 50}\n" + "SELAMAT DATANG".center(50) + f"\n{'=' * 50}")
while True:
    try:
        nama_kasir = input("Masukkan nama kasir         : ").title()
        if (nama_kasir.replace(' ','').replace('.','')).isalpha() == False: # Memastikan tidak ada karakter selain huruf, spasi, dan tanda titik
            raise Exception('\nNama harus huruf!\n')
        elif len(nama_kasir) == 0: # Mematikan nama kasir tidak kosong
            raise Warning('\nNama tidak boleh kosong!\n')
        print('=' * 50)
        break
    except Warning as war:
        print(war)
    except Exception as ex:
        print(ex)
while True:
    try:
        print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
        print('=' * 50)
        opsi = input('Masukkan opsi pilihan Anda  : ')
        if opsi == '1':
            trx_baru('1', '', 0)
        elif opsi == '2':
            cek_trx()
        elif opsi == '3':
            print(f"{'=' * 50}\n" + 'SAMPAI JUMPA'.center(50) + f"\n{'=' * 50}")
            break
        else:
            raise Warning(f"{'=' * 50}\nOpsi invalid!\n")
    except Warning as wr:
        print(wr)