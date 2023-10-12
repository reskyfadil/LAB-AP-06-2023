def CekPalindrom(kata: str) -> str: 
    bacaan = kata

    if bacaan == bacaan[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
inputannya = input("Masukkan Kata : ")
hasil = CekPalindrom(inputannya)
print(f"{inputannya} adalah {hasil}" )