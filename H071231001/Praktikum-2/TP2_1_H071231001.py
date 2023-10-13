print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
gender = int(input("= "))

tinggi_badan = float(input("Masukkan tinggi badan (cm) : ")) / 100
berat_badan = float(input("Masukkan berat badan (kg) : "))

bmi = berat_badan / (tinggi_badan * tinggi_badan)

if gender == 1:
    if bmi < 18:
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif 18 <= bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif 24 <= bmi < 27:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    else:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
elif gender == 2:
    if bmi < 17:
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif 17 <= bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif 24 <= bmi < 28:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    else:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}")
else:
    print("Input tidak valid")
