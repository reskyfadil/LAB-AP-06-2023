import re
pola=r'^[A-Za-z02468]{40}[13579\s]{5}$'
stringnya=input()
print(bool(re.match(pola,stringnya)))