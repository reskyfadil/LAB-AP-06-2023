import re
def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    if re.match(pattern, username):
        return True
    else:
        return False

def is_valid_email(email):
    pattern = r"^[a-z0-9+\d{2,}@[a-z]+\.(com|co\.id)$" 
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.search(pattern, password)

username = input("Masukkan username: ")
if is_valid_username(username):
    email = input("Masukkan email: ")
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print("\nRegistrasi berhasil! Selamat Datang", username)
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")

