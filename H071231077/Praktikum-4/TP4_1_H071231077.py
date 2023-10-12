def permutasi_kata(kata):
    if not kata.isdigit(): 
        for i in range(len(kata)):     #Looping untuk hasil permutasi kata sesuai dengan panjang kata yang dimasukkan
            kata = kata[-1] + kata[:-1]   #untuk mengganti kata
            print(kata, end="|")
    else:
        print("Masukkan String")

input_kata = input("Masukkan kata = ")
permutasi_kata(input_kata)



















    



