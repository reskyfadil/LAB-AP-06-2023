tulang_belakang=input("Masukkan Input Pertama : ")
subgrup=input("Masukkan Input Kedua : ")
sub_subgrup=input("Masukkan Input Ketiga : ")

match (tulang_belakang, subgrup, sub_subgrup):
    case ("vertebrado", "ave", "carnivoro"):
        print("aguia")
    case ("vertebrado", "ave", "onivoro"):
        print("pomba")
    case ("vertebrado", "mamifero", "onivoro"):
        print("homem")
    case ("vertebrado", "mamifero", "herbivoro"):
        print("vaca")
    case ("invertebrado", "inseto", "hematofago"):
        print("pulga")
    case ("invertebrado", "inseto", "herbivoro"):
        print("lagarta")
    case ("invertebrado", "anelideo", "hematofago"):
        print("sanguessuga")
    case ("invertebrado", "anelideo", "onivoro"):
        print("minhoca")
    case _:
        print("Invalid input")