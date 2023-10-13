def palindrom(x: str):
    uji = True
    if not x.isdigit():
        for i in range(len(x)):
            if x[i] == x[-(i + 1)]:
                uji = uji
            else:
                uji = False
        if uji:
            return "Palindrom"
        else:
            return "Bukan palindrom"
    else :
        print("error")

input_kata = input("Masukkan kata = ").lower() 
hasil = palindrom(input_kata)
print(hasil)









