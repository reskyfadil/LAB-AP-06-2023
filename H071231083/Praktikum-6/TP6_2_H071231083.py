array1 = set(list(map(int,(input("Input array ke-1 : ").split()))))
array2 = set(list(map(int,(input("Input array ke-2 : ").split()))))

x = array1.intersection(array2)
x = tuple(x)
print(f"Terdapat {len(x)} buah duplikat yaitu {x}")
