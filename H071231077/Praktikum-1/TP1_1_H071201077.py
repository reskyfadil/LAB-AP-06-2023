#input
print("Menghitung Permukaan Luas dan Keliling Segitiga")
x = int(input("Masukkan Panjang Sisi X (Tingginya) : "))
y = int(input("Masukkan Panjang Sisi Y (Alasnya) : "))
z = (x**2 + y**2)**0.5#sisi miring


#rumus yang di pake untuk menghitung 
Luas = 1/2 * y * x
Keliling = x + y + z

#output
print(f"Luas dari segitiga : {Luas:.2f}")
print(f"Keliling dari segitiga : {Keliling:.2f}")