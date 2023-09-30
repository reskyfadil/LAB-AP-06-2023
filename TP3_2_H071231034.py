harga=int(input())
nominal=int(input())
kembalian=nominal-harga

pecahan_uang=[100000,50000,20000,10000,5000,2000,1000]
jumlah_pecahan=[]

for pecahan in pecahan_uang:
    jumlah=kembalian//pecahan
    kembalian = kembalian % pecahan
    jumlah_pecahan.append(jumlah)

print("Kembalian:")
for i in range(len(pecahan_uang)):
    print(f"{jumlah_pecahan[i]} uang sejumlah Rp{pecahan_uang[i]}")