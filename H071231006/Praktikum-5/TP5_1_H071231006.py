def string_campuran(s1, s2):
    mixed = ""
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_len = max(len_s1, len_s2)
    s2 = s2[::-1]

    for i in range (max_len):
        if i < (len_s1):
            mixed += s1[i]
        if i < (len_s2):
            mixed += s2[i]
    return mixed

s1 = input("Masukkan s1 = ")
s2 = input("Masukkan s2 = ")

hasil_mixed = string_campuran(s1, s2)
print("Hasil mixed = ", hasil_mixed)