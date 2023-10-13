#Input dari pengguna
jenis_kelamin = input("pilih gender anda : \n1.pria\n2.wanita\n= ")
tinggi_badan = float(input("Masukkan tinggi badan (cm) : "))
berat_badan = float(input("Masukkan berat badan (kg) : "))

#Konversi tinggi badan dari cm ke meter
tinggi_badan_m = tinggi_badan / 100

#Hitung BMI
BMI = berat_badan / (tinggi_badan_m ** 2)

#Menentukan kategori BMI
if jenis_kelamin == "1":
    if BMI < 18:
        print(f"anda tergolong Underweight dengan BMI {BMI:.2f}")
    elif 18 <= BMI < 24:
        print(f"anda tergolong Normal dengan BMI {BMI:.2f}")
    elif 24 <= BMI < 27:
        print(f"anda tergolong Overweight dengan BMI {BMI:.2f}")
    else:
        print(F"anda tergolong Obese dengan BMI {BMI:.2f}")
if jenis_kelamin == "2":
    if BMI < 17:
        print(f"anda tergolong Underweight dengan BMI {BMI:.2f}")
    elif 17 <= BMI < 24:
        print(f"anda tergolong Normal dengan BMI {BMI:.2f}")
    elif 24 <= BMI < 28:
        print(f"anda tergolong Overweight dengan BMI {BMI:.2f}")
    else:
        print(f"anda tergolong Obese dengan BMI {BMI:.2f}")