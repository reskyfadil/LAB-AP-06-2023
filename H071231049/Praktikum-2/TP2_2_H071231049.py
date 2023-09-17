Input_Pertama = input("Masukkan Input Pertama : ")
Input_Kedua = input("Masukkan Input Kedua : ")
Input_Ketiga = input("Masukkan Input Ketiga : ")

match Input_Pertama:
    case "vertebrado":
        match Input_Kedua:
            case "ave":
                if Input_Ketiga == "carnivoro":
                    print("agula")
                elif Input_Ketiga == "onivoro":
                    print("pomba")
                else:
                    print("Invalid Input")
            case "mamifero":
                if Input_Ketiga == "onivoro":
                    print("homem")
                elif Input_Ketiga == "hernivoro":
                    print("vaca")
                else:
                    print("Invalid Input")
            case _:
                print("Invalid Input")
    case "invertebrado":
        match Input_Kedua:
            case "inseto":
                if Input_Ketiga == "hematofago":
                    print("pulga")
                elif Input_Ketiga == "herbivoro":
                    print("lagarta")
                else:
                    print("Invalid Input")
            case "anelideo":
                if Input_Ketiga == "hematofago":
                    print("sanguessuga")
                elif Input_Ketiga == "onivoro":
                    print("minhoca")        
                else:
                    print("Invalid Input")
            case _:
                print("Invalid Input")
    case _:
        print("Invalid Input")                    
                

                    
