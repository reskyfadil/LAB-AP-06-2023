class Mahasiswa:
    def __init__(self, nama, nim, jurusan, Ipk):
        self.nama = nama  
        self.nim = nim 
        self.jurusan = jurusan
        self.Ipk = Ipk

    def info(self):
        print('Nama     :',self.nama)
        print('nim      :',self.nim)
        print('jurusan  :',self.jurusan)
        print('Ipk      :',self.Ipk)
    
    def hitung_predikat(self):
        if self.Ipk >= 3.5:
            print("Cumlaude")
        elif self.Ipk >= 3.0:
            print("Sangat Memuaskan")
        elif self.Ipk >= 2.5:
            print("Memuaskan")
        elif self.Ipk >= 2.0:
            print("Cukup")
        else:
            print("Kurang")



mhs1 = Mahasiswa("jaka", "001", "Sisfor", 4.00)
mhs2 = Mahasiswa("nay", "017", "sisfor", 4.00)
mhs3 = Mahasiswa("dita", "014", "geofisika", 4.00)
mhs1.info()
mhs2.info()
mhs3.info()
mhs1.hitung_predikat()
mhs2.hitung_predikat()
mhs3.hitung_predikat()


# def hitung_predikat(self):
#     if self.Ipk >= 3.5:
#         print("Cumlaude")
#     elif self.Ipk >= 3.0:
#         print("Sangat Memuaskan")
#     elif self.Ipk >= 2.5:
#         print("Memuaskan")
#     elif self.Ipk >= 2.0:
#         print("Cukup")
#     else:
#         print("Kurang")

