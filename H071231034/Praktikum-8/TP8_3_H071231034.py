import re

def validasi_username(username):
    return re.fullmatch(r'[a-zA-Z0-9]{5,20}', username) is not None

def validasi_email(email):
    return re.fullmatch(r'[a-z]+[0-9]{0,2}@[a-z]+\.[a-z]+(\.[a-z]{2})?', email) is not None

def validasi_password(password):
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    no_special = re.fullmatch(r'[A-Za-z0-9]{8,}', password)
    return all([has_upper, has_lower, no_special])

print(validasi_username('JohnDoe123'))
print(validasi_email('johndoe99@example.com'))
print(validasi_password('JohnDoe2022@')) # ada karakter spesial