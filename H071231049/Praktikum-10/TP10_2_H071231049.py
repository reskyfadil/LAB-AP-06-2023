from abc import ABC, abstractmethod
#Implementasian Metode Enkapsulasi

class Mobil:
    def __init__(self, warna, merk):
        self.__warna = warna
        self.__merk = merk
    
    def getWarna(self):
        return self.__warna
    def getMerk(self):
        return self.__merk
    def setWarna(self, warna):
        self.__warna = warna
    def setMerk(self, merk):
        self.__merk = merk

mobil1 = Mobil("Silver", "Pagani")
mobil2 = Mobil("Hijau", "Lamborghini")

print(f"Merek mobil: {mobil1.getMerk()}\nWarna mobil: {mobil1.getWarna()} ")
print(f"Merek mobil: {mobil2.getMerk()}\nWarna mobil: {mobil2.getWarna()} ")
        
#Pengimplementasian Abstract Class, Inheritance, dan Polymorphism
class Bentuk(ABC):
    @abstractmethod
    def HitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def HitungLuas(self):
        return self.sisi ** 2
    
class Segitiga(Bentuk):
    def __init__(self, panjang, alas, tinggi):
        self.panjang = panjang
        self.alas = alas
        self.tinggi = tinggi

    def HitungLuas(self):
        return 1/2 * self.alas * self.tinggi
    
luas = Persegi(5)
segitiga = Segitiga(10, 10, 10)
print(f"Luas dari persegi: {luas.HitungLuas()}")
print(f"Luas dari segitiga: {segitiga.HitungLuas()}")


