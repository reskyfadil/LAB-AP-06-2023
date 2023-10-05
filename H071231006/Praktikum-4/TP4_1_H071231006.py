def mutasi(kata) :
    for i in range(len(kata)):
        kata = kata[-1] + kata[:-1]
        print (kata, end=' | ')
try:
    mutasi2 = input("Masukkan Kata : ")
    if mutasi2.isnumeric():
        raise ValueError
    else:
        output = mutasi(mutasi2)
        
except:
    print("Inputan harus berupa string")