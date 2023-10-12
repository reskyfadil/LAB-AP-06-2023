def find_largest_number(numbers):
    if not isinstance(numbers, list) :
        raise TypeError ("error")
    
    largest = numbers[0] 

    for num in numbers:
         # menambahkan kondisi untuk memeriksa tipe data
         if not isinstance(num, (int, float)):
             raise TypeError ("error")
         if num > largest:
            largest = num

    return largest

numbers = ["kambing"]
terbesar = find_largest_number(numbers)
print("Angka terbesar adalah:", terbesar)

