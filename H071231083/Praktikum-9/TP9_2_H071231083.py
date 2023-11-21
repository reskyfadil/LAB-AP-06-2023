class Mahasiswa:
    def __init__(self, Nama, Nim, Jurusan, Ipk):
        self.Nama = Nama
        self.Nim = Nim
        self.Jurusan = Jurusan
        self.Ipk = Ipk

    def info(self):
        print("Nama:", self.Nama)
        print("Nim:", self.Nim)
        print("Jurusan:", self.Jurusan)
        print("Ipk:", self.Ipk)

    def hitung_predikat(self):
        if self.Ipk >= 3.5:
            predikat = "Cumlaude"
        elif self.Ipk >= 3.0:
            predikat = "Sangat memuaskan"
        elif self.Ipk >= 2.5:
            predikat = "Memuaskan"
        elif self.Ipk >= 2.0:
            predikat = "Cukup"
        else:
            predikat = "Kurang"
        return predikat
    
Mahasiswa1 = Mahasiswa("Ikhsan", "H071231083", "Sisfo", 3.8)
Mahasiswa1.info()

predikat = Mahasiswa1.hitung_predikat()
print("predikat:", predikat)