import re

def valid_username(username):
    pattern = r"^[A-Za-z0-9]{8,20}$"
    return re.search(pattern, username)

def valid_email(email):
    pattern = r"^[a-z]+[0-9]{2,}@[a-z]+\.(com|co\.id)"
    return re.search(pattern, email)

def valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.search(pattern, password)

username = input("Masukkan username : ")
if valid_username(username):
    email = input("Masukkan email : ")
    if valid_email(email):
        password = input("Masukkan password : ")
        if valid_password(password):
            print(f"Registrasi berhasil! Halo {username}")
        else:
            print("\nPassword yang dimasukkan beresiko di hack. Resgistrasi gagal!")
    else:
        print("\nEmail yang dimasukkan tidak valid. Registrasi gagal!")
else:
    print("\nUsername tidak valid dalam sistem. Registrasi gagal!")