n = int(input(""))
if n < 0:
    print("Bukan fibonacci")
else:
    S1 = 0 #suku pertama bilangan fibonacci
    S2 = 1 #suku kedua
    for i in range(n):
        print(S1, end=" ")
        S3 = S1 + S2
        S1 = S2
        S2 = S3