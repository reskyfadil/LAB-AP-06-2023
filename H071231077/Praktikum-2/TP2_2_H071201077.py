a = input("Masukkan Input Pertama : ")
b = input("Masukkan Input Kedua : ")
c = input("Masukkan Input Ketiga : ")


#pake matchcase untuk membenarkan satu satu
match a, b, c:
    case "vertebrado","ave","carnivoro":
        print("Aguia")

    case "vertebrado","ave","onivoro":
        print("Pomba")

    case "vertebrado","mamifero","onivoro":
        print("Homem")

    case "vertebrado","mamifero","herbivoro":
        print("Vaca")

    case "invertebrado","inseto","hematofago":
        print("Pulga")

    case "invertebrado","inseto","herbivoro":
        print("Lagarta")

    case "invertebrado","anelideo","hematofago":
        print("Sanguessuga")

    case "invertebrado","anelideo","onivoro":
        print("Minhoca")

    case _:
        print("Input Salah")