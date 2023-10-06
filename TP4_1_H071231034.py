def permutasi(k):
    try:
        for _ in range(len(k)):
            k=k[-1]+k[:-1]
            print(k, end=" | ")
    except TypeError:
        print("Input tidak valid")

k=input()
permutasi(k)