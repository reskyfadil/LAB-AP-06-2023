Gender = input("Pilih Gender Anda\n1. Pria\n2. Wanita\n= ")
if Gender != '1' and '2':
    print("Inputan yang anda masukkan salah")
    quit()
Tinggi = float(input("Masukkan tinggi badan (cm) : "))
Berat = float(input("Masukkan berat badan (kg) : "))
Tinggi_M = float(Tinggi / 100)
BMI = float(f"{Berat / (Tinggi_M**2):.2f}")

match Gender :
    case "1":
        if BMI < 18:
            print(f"Anda tergolong Underweight dengan BMI {BMI}")
        elif 18 <= BMI <= 23.9:
            print(f"Anda tergolong Normal dengan BMI {BMI} ")
        elif 24 <= BMI <= 26.9:
            print(f"Anda tergolong Overweight dengan BMI {BMI}")
        else:
            print(f"Anda tergolong Obesitas dengan BMI {BMI}")
    case "2":
        if BMI < 17:
            print(f"Anda tergolong Underweight dengan BMI {BMI}")
        elif 17 <= BMI <= 23.9:
            print(f"Anda tergolong Normal dengan BMI {BMI}")
        elif 24 <= BMI <= 27.9:
            print(f"Anda tergolong Overweight dengan BMI {BMI}")
        else:
            print(f"Anda tergolong Obesitas dengan BMI {BMI}")
           