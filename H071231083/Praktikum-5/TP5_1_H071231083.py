s1 = input("Masukkan huruf : ")
s2 = input("Masukkan huruf : ")
s2 = s2[::-1]

s3 = ""

max_len = max(len(s1), len(s2))

for i in range(max_len):
    if i < len(s1):
        s3 += s1[i]
    if i < len(s2):
        s3 += s2[i]

print(f"hasil gabungan : {s3}")