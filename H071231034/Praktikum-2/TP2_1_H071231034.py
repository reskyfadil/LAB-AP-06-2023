g=float(input("Pilih Gender Anda\n1. Pria\n2. Wanita\n= "))

if g != 1 and g != 2: #tidak dieksekusi jika g-nya 1 atau 2
    print("Pilih input yang valid")
else:
    t = float(input("Masukkan tinggi badan (cm) : ")) / 100
    b = float(input("Masukkan berat badan (kg) : "))
    bmi = b / t**2

    if g == 1:
        if 27 <= bmi:
            kategori = "Obese"
        elif 24 <= bmi < 27:
            kategori = "Overweight"
        elif 18 <= bmi < 24:
            kategori = "Normal"
        else:
            kategori = "Underweight"
    else:
        if 28 <= bmi:
            kategori = "Obese"
        elif 24 <= bmi < 28:
            kategori = "Overweight"
        elif 17 <= bmi < 24:
            kategori = "Normal"
        else:
            kategori = "Underweight"

    print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")