class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan 
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama : {self.nama}")
        print(f"Nim : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"IPK : {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5 and self.ipk <= 4.0:
            return "Cumlaude"
        elif self.ipk >= 3.0 and self.ipk < 3.5:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5 and self.ipk < 3.0 :
            return "Memuaskan"
        elif self.ipk >= 2.0 and self.ipk < 2.5:
            return "Cukup"
        elif self.ipk < 2.0 and self.ipk >= 0:
            return "Kurang"
        else:
            return "Invalid Input"
        
data = Mahasiswa("Sisy Ramadhani", "H071231006", "Sistem Informasi", 3.5)
info = data.tampilkan_info()
hitung_predikat = data.hitung_predikat()
print(f"Predikat : {hitung_predikat}")