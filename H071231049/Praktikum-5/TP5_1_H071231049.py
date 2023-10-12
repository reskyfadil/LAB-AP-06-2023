def pergabungan(kata1, kata2):
    var = ''
    panjang_kata = max(len(kata1), len(kata2))
    
    for i in range(panjang_kata):
        if i < len(kata1):
            var += kata1[i]
        if i < len(kata2):
            var += kata2[-(i + 1)]
    return var

kata1 = input("Masukkan input : ")
kata2 = input("Masukkan input : ")
output = pergabungan(kata1, kata2)
print(output)