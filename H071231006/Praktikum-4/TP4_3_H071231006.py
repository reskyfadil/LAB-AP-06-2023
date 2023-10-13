def maximum(*n):
    n = list(map(int, input('Masukkan nilai :').split(',')))
    maximum = n[0]
    for i in n:
        if i > maximum:
            maximum = i
    return (maximum)
print (maximum())