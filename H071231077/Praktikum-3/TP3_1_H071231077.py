x = int(input("Masukkan angka = "))
m = 0
n = 1
print(f"{m} {n}", end=" ")
for i in range(x-2) :
    y = m + n
    m = n
    n = y 
    print (y, end= " ")
    















