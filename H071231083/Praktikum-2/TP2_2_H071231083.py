a = input("Masukkan input pertama : ")
b = input("Masukkan input kedua : ")
c = input("Masukkan input ketiga : ")

match a, b, c:
    case "vertebrado", "ave", "carnivoro":
        print("aguia")
    case "vertebrado", "ave", "onivoro":
        print("pomba")
    case "vertebrado", "mamifero", "onivoro":
        print("homem")
    case "vertebrado", "mamifero", "herbivoro":
        print("vaca")
    case "invertebrado", "inserto", "hematofago":
        print("pulga")
    case "invertebrado", "inserto", "herbivoro":
        print("lagarta")
    case "invertebrado", "anelideo", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelideo", "onivoro":
        print("mihoca")
    case _:
        print("invalid input")