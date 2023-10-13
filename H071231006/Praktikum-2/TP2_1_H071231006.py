print('Pilih Gender Anda:')
print('1. Pria')
print('2. Wanita')

gender=int(input('= '))
 
tinggi=float(input('Masukan tinggi badan (cm): ')) / 100
berat= float(input('Masukan berat badan (kg): '))


BMI= berat/(tinggi**2)

if gender == 1:
    if BMI <18:
     print(f'Anda tergolong Underweight dengan BMI {BMI:.2f}')
    elif 18 <= BMI <= 23.9:
     print(f'Anda tergolong Normal dengan BMI {BMI:.2f}')
    elif 24 <= BMI <= 26.9:
     print(f'Anda tergolong Overweight dengan BMI {BMI:.2f}')
    else:
     print(f'Anda tergolong Obesitas dengan BMI {BMI:.2f}')
elif gender == 2:
    if BMI <17:
     print(f'Anda tergolong Underweight dengan BMI {BMI:.2f}')
    elif 17 <= BMI <= 23.9:
     print(f'Anda tergolong Normal dengan BMI {BMI:.2f}')
    elif 24 <= BMI <= 27.9:
     print(f'Anda tergolong Overweight dengan BMI {BMI:.2f}')
    else:
     print(f'Anda tergolong Obesitas dengan BMI {BMI:.2f}')
else:
    print('jenis kelamin tidak ditemukan')