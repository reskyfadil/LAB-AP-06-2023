n = int(input("Masukkan nilai : "))

if 0 <= n:
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=' ')
        next_bil = a + b 
        a = b
        b = next_bil
        count += 1
