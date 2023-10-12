def string_baru(input):
    x = len(input)
    if x < 3:
        return "Input terlalu pendek"

    middle_index = x // 2
    if x % 2 != 0:
        string = input[0] + input[middle_index] + input[-1]
        return string
    else:
        string = input[0] + input[middle_index - 1] + input[middle_index] + input[-1]
        return string

input= input("Masukkan kata: ")
string = string_baru(input)
print(string)