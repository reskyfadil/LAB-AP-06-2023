def mencarihuruftertentu(input_string):
    x=len(input_string)
    if x <= 3:
        return input_string
    else:
        tengah = x//2
        posisi = input_string[0] + input_string[tengah] + input_string[-1]
        return posisi
    
input_string = input("")
print(mencarihuruftertentu(input_string))