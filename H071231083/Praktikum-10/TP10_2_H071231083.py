from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

class Manusia(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def suara(self):
        pass

    def get_nama(self):
        return self.nama
    
class Faiz(Manusia):
    def suara(self):
        return "pinjam dulu seratus"
    
class Ikhsan(Manusia):
    def suara(self):
        return "hahahahahah"
    
f = Faiz("Faiz")
i = Ikhsan("Ikhsan")

print(f'{f.suara()}')
print(f'{i.suara()}')