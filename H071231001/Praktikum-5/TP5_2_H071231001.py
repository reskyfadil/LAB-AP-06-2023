a = input('Masukkan kata: ')
if len(a) <= 3:
    print(a)
else:
    print(a[0] + a[(len(a) // 2)] + a[-1])