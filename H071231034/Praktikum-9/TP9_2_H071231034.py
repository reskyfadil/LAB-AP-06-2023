class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    def info_mahasiswa(self):
        return (f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}\nIPK: {self.ipk}")
    def hitung_ipk(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif 3.0 <= self.ipk < 3.5:
            return "Sangat Memuaskan"
        elif 2.5 <= self.ipk < 3.0:
            return "Memuaskan"
        elif 2.0 <= self.ipk < 2.5:
            return "Cukup"
        else:
            return "Kurang"

nm=input("Masukkan nama: ")
nim=input("Masukkan NIM: ")
jurusan=input("Masukkan Jurusan: ")
ipk=float(input("Masukkan IPK: "))

mahasiswa1 = Mahasiswa(nm,nim,jurusan,ipk)

print()
print("IPK Mahasiswa:",mahasiswa1.hitung_ipk())
print("Info Mahasiswa:")
print(mahasiswa1.info_mahasiswa())