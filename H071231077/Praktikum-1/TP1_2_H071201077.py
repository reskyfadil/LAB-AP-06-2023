#input
print("Konversi Suhu Dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
c = int(input("Masukkan Nilai Suhu Dalam Celcius : "))

# Rumus
k = int(c + 273.15)
r = int(4/5*c)
f = int((9/5*c)+32)

#output
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {k}K")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Reamur adalah : {r}R")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Fahrenheit adalah : {f}F")