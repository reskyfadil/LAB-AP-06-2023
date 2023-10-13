#program konversi suhu dari celcius
print("konversi  suhu dari celcius ke kelvin, Reamur, Fahrenheit")
celcius = int(input("Masukkan nilai suhu dalam celcius : "))

#Rumus
k = int(celcius + 273.15)
r = int(4/5*celcius)
f = int((9/5*celcius)+32)

print(f"Hasil konversi dari suhu {celcius} derajat celcius ke kelvin adalah : {k}K")
print(f"Hasil konversi dari suhu {celcius} derajat celcius ke Reamur adalah : {r}R")
print(f"Hasil konversi dari suhu {celcius} dearjat celcius ke fahrenheit adalah : {f}F")