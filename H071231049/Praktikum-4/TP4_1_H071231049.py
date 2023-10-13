def permutasi(kata, suku=0):
    try:
        if not kata.isnumeric():
            print(kata, end= " | ")
            kata = kata[-1] + kata[0:-1]
            suku += 1
            if suku < len(kata):
                permutasi(kata, suku)
        else:
            raise TypeError        
    except TypeError:
        print("Type Error")
                

inputannya = input("Masukkan kata : ")
permutasi(inputannya)        




