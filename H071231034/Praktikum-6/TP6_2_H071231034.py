array1 = set(map(int, input("Input array ke-1: ").split()))
array2 = set(map(int, input("Input array ke-1: ").split()))

duplikat = array1&array2

if len(duplikat) > 1:
    print(f"Terdapat {len(duplikat)} buah duplikat yaitu {tuple(duplikat)}")
elif len(duplikat) == 1:
    print(f"Terdapat 1 buah duplikat yaitu ({(tuple(duplikat)[0])})")
else:
    print("Tidak ada duplikasi ditemukan.")