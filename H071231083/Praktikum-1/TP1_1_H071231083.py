print("menghitung luas permukaan dan keliling segitiga: ")
x = float(input("Masukkan panjang sisi x: "))
y = float(input("Masukkan panjang sisi y: "))
z = (x**2 + y**2)**0.5

a = (1/2) * y * x 

k = x + y + z

print(f"luas segitiga : {a:.2f}")
print(f"keliling segitiga : {k:.2f}")