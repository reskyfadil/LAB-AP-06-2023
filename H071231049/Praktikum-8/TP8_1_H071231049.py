import re

input_string = input('Masukkan string : ')
pattern = r'[A-Za-z24680]{40}[13579\s]{5}'
result = re.match(pattern, input_string)
print(result)
# if result:
#     print(True)
# else:
#     print(False)