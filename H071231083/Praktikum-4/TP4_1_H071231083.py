def stringPermutation(kata):
    try:
        kata_panjang = len(kata)
        for i in range(kata_panjang):
            kata = kata[-1] + kata[:-1]
            print(kata, end= " | ")
        print()
    except TypeError:
        print("input harus berupa string")
 
stringPermutation("Mobil")
stringPermutation("Ayam")