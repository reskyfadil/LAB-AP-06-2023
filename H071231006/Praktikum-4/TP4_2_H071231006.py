def palindrom (n:str)-> str:
    if n.upper() == n[::-1].upper():
        return ("Palindrom")
    else:
        return ("Bukan Palindrom")

inputan = (input("Masukkan Kata : ")) 
print(palindrom(inputan))