def anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
       
    for char in kata1:
        if kata1.count(char) != kata2.count(char):
            return False
    return True

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua  : ")

hasil = anagram(kata1, kata2)
print(hasil)