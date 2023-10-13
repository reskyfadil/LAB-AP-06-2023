def CekAnagram(kata1, kata2):
    notFound = 0
    for i in kata1:
        eksistensi1 = kata2.count(i)
        eksistensi2 = kata1.count(i)
        if eksistensi1 != eksistensi2:
            notFound += 1
    if notFound == 0 and len(kata1) == len(kata2):
        return True
    else:
        return False
    
    

kata1 = input("Masukkan kata pertama : ")
kata2 = input("Masukkan kata kedua : ")

var1 = kata1.replace(" ","")
var2 = kata2.replace(" ","")

print(f"2 kata adalah anagram = {CekAnagram(var1, var2)}")