array1 = list(map(int, input("Input array ke-1 : ").split()))
array2 = list(map(int, input("Input array ke-2 : ").split()))
duplikat = []
for i in array1:
    if i in array2 and i not in duplikat:
        duplikat.append(i)

if len(duplikat) > 0:
    print("Terdapat",len(duplikat),"Buah yaitu",tuple(duplikat))
else:
    print("Tidak ada duplikat ditemukan")