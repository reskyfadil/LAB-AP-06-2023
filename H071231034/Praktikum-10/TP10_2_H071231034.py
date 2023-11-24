from abc import ABC, abstractmethod

class SausSambal(ABC):
    def __init__(self, merek, rasa):
        self._merek = merek  
        self._rasa = rasa

    @abstractmethod
    def cara_membuat(self):
        pass

    def display_info(self):
        print(f"Saus Sambal {self._merek} rasa {self._rasa}")

class Jawara(SausSambal):
    def __init__(self, rasa):
        super().__init__("Jawara", rasa)

    def cara_membuat(self):
        return "Dibuat dengan bahan pilihan dan resep tradisional"

class ABC(SausSambal):
    def __init__(self, rasa):
        super().__init__("ABC", rasa)

    def cara_membuat(self):
        return "Dibuat dengan teknologi modern dan standar kualitas tinggi"

class Indofood(SausSambal):
    def __init__(self, rasa):
        super().__init__("Indofood", rasa)

    def cara_membuat(self):
        return "Dibuat dari bahan lokal terbaik dengan cita rasa nusantara"

class Heinz(SausSambal):
    def __init__(self, rasa):
        super().__init__("Heinz", rasa)

    def cara_membuat(self):
        return "Dibuat dengan resep internasional dan standar global"

def cetak_cara_membuat(sambal):
    print(sambal.cara_membuat())

jawara_asli = Jawara("Sambal Asli")
abc_bangkok = ABC("Bangkok")
indofood_pedas = Indofood("Extra Pedas")
heinz_tomat = Heinz("Sambal Tomat")

jawara_asli.display_info()
abc_bangkok.display_info()
indofood_pedas.display_info()
heinz_tomat.display_info()

cetak_cara_membuat(jawara_asli)
cetak_cara_membuat(abc_bangkok)
cetak_cara_membuat(indofood_pedas)
cetak_cara_membuat(heinz_tomat)