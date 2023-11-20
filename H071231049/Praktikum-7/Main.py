import os
import datetime as dt
import random

def Garis():
    print('='*70)

def createHistory():
    with open ('history', 'a') as file:
        file.write(f"{'='*70}\n")
        file.write(f"|{'RIWAYAT TRANSAKSI':^68}|\n")
        file.write(f"{'='*70}\n")
        file.write(f"|{'Waktu':^18}|{'ID Transaksi':^24}|{'Nominal Transaksi':<24}|\n")
        file.write(f"{'='*70}\n")
        file.close()

def addHistory(waktu, id, nominal):
    with open('history','a') as file:
        file.write(f"|{waktu:^18}|{id:^24}|{'Rp'+ nominal:^24}|\n")
        file.write(f"{'-'*70}\n")

def atasanStruk(nama, waktu):
    data.write(f"{'HAMSSS STORE':^70}\n\n")
    data.write(f"{'='*70}\n")
    data.write(f"Nama kasir \t\t: {nama}\n")
    data.write(f"Waktu transaksi \t: {waktu}\n")
    data.write(f"{'='*70}\n")
    data.write(f"{5*''}|{'Nama':^23}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^12}|\n")
    data.write(f"{60*'=':^70}\n")

def addStruk(nama, harga, jumlah ,total):
    data.write(f"{5*''}|{nama:^23}|{harga:^12}|{jumlah:^8}|{total:>12}|\n")

def bawahanStruk(total_belanja):
    data.write(f"{60*'=':^70}\n")
    data.write(f"{''*5}|{'TOTAL':^23}{' '*22}|{'Rp' + str(total_belanja):>12}|\n")
    data.write(f"{60*'=':^70}\n\n")
    data.write(f"{'='*70}\n")
    data.write(f"{'TERIMA KASIH TELAH BERBELANJA':^70}\n")
    data.write(f"{'='*70}\n")


def id(nama_kasir):
    nama = nama_kasir[0] + nama_kasir[len(nama_kasir)//2] + nama_kasir[-1]
    nama = nama.upper()
    waktu = dt.datetime.now()
    tahun = str(waktu.year)
    bulan = str(waktu.month)
    tanggal = str(waktu.day)
    jam = str(waktu.hour)
    menit = str(waktu.minute)
    kode = str(random.randint(100,999))

    nama_file = nama + tahun[-2:] + bulan + tanggal + jam + menit + kode
    return nama_file

def waktu():
    waktu = str(dt.datetime.now())
    waktu = waktu[2:16].replace("-","/")
    return waktu

folder = "invoices"

while True:
    # os.system("cls")
    Garis()
    print('SELAMAT DATANG'.center(70))
    Garis()
    print('Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar')
    Garis()
    opsi = int(input("Masukkan opsi pilihan:\t "))
    Garis()
    match opsi:
        case 1:
            if not os.path.exists("history"):
                createHistory()
                
            nama = input("Masukkan nama kasir:\t ")
            ID = id(nama)
            file_name = ID + ".txt"
            file_path = os.path.join(folder, file_name)

#jika folde tidak ada maka harus dibuat dlu
            if not os.path.exists(folder):
                os.mkdir(folder)
            data = open(file_path, "a")


            #data dibuka dan menulis header
            data = open(file_path, "a")
            WAKTU = waktu() #diubah menjadi variabel agar bisa masuk kedalam fungsi atasanStruk(nama, waktu) 
            atasanStruk(nama, WAKTU)

            total_belanja = 0

            while True:
                nama = input("Masukkan nama produk\t:")
                harga = int(input("Masukkan harga produk\t:"))
                jumlah = int(input("Masukkan jumlah produk\t:"))
                total_barang = harga * jumlah
                total_belanja += total_barang

                addStruk(nama, harga, jumlah, total_barang)

                
                
                #tambah jumlah belanja
                isTambah = input("Tambah produk? y/n\t")
                if isTambah == 'n':
                    bawahanStruk(total_belanja)
                    data.close()
                    break

                    #riwayat transaksi
            NOMINAL = str(total_belanja)
            addHistory(WAKTU,ID,NOMINAL)
            # with open("history","a") as his:
            #     his.write(f"{waktu()} {ID} Rp.{total}\n")
        case 2:
            cari = input("Masukkan ID file yang ingin dicari : ")
            cari_path = folder + "/" + cari + ".txt"
            if os.path.exists(cari_path):
                with open(cari_path, "r") as file:
                    print(file.read())
            else:
                print(f"File dengan ID {cari} tidak ditemukan")
        case 3:
            Garis()
            print("PROGRAM SELESAI".center(70))
            Garis()
            break
        case _:
            Garis()
            print("INPUT TIDAK VALID".center(70))
            Garis()