jenis_kelamin = int(input("Gender \n1. Cowok \n2. Cewek \n= "))
tinggi = int(input("Masukkan tinggi badan (cm) = "))
berat = float(input("Masukkan berat badan (kg)= "))
tinggidalammeter = tinggi/100 #di bagi 100 untuk menguba centi ke meter
bmi = berat/((tinggidalammeter)**2)
if jenis_kelamin == 1:
    if bmi < 18:
        print(f"Underweight = {bmi:.2f}")
    elif bmi >= 18 and bmi < 24:
        print(f"Normal = {bmi:.2f}")
    elif bmi >= 24 and bmi < 27:
        print(f"Overweight = {bmi:.2f}")
    elif bmi >= 27:
        print(f"Obese = {bmi:.2f}");
elif jenis_kelamin == 2:
    if bmi < 17:
        print(f"Underweight = {bmi:.2f}")
    elif bmi >= 17 and bmi < 24:
        print(f"Normal = {bmi:.2f}")
    elif bmi >= 24 and bmi < 28:
        print(f"Overweight = {bmi:.2f}")
    elif bmi >= 28:
        print(f"Obese = {bmi:.2f}");
else:
    print("tidak valid")