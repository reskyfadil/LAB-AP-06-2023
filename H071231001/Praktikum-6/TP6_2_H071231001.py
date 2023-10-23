array = list(map(int,input("input array ke-1 :").split()))
array2 = list(map(int, input("input array ke-2").split()))
duplikat = []
for i in array :
    if i in array2 and i not in duplikat :
        duplikat.append(i)
        
if len(duplikat)> 0 :
    print("terdapat",len(duplikat),"buah yaitu",tuple(duplikat))
else :
    print("tidak ada duplikat ditemukan")