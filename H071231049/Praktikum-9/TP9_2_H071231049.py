class Mahasiswa():
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"IPK     : {self.ipk}")

    def hitung_predikat(self):
        if 3.5 <= self.ipk <= 4.0:
            predikat = "Cumlaude"
        elif 3.0 <= self.ipk < 3.5:
            predikat = "Sangat memuaskan"
        elif 2.5 <= self.ipk < 3.0:
            predikat = "Memuaskan"
        elif 2.0 <= self.ipk < 2.5:
            predikat = "Cukup"
        elif self.ipk < 2.0 :
            predikat = "Kurang"
        else:
            print("Ipk tidak valid, Masukkan Ipk yang valid")
            return

        print(f"Predikat: {str(predikat)}")


hamdi = Mahasiswa("Syaebatul Hamdi", "H071231049", "Sistem Informasi", 4.0)

print("Data Mahasiswa:")
hamdi.tampilkan_info()
hamdi.hitung_predikat()