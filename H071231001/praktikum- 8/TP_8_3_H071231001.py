import re
def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$" #untuk memvalidasi panjang karakter minimal 5 dan maksimal 20.
    return re.search(pattern, username)  

def is_valid_email(email):   #untuk validasi email.
    pattern = r"^[a-z]+\d{2,}@[a-z]+\.(com|co\.id)$" #untuk mencocokkan domain email.
    return re.search(pattern, email)     #jika tdk ada pencocokan maka research akan mengembalikan none

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$" #untuk validasi password sesuai permintaan soal.
    return re.search(pattern, password)   

username = input("Masukkan username: ")

if is_valid_username(username):
    email = input("Masukkan email: ")

    if is_valid_email(email):
     password = input("Masukkan password: ")

     if is_valid_password(password):
        print(f"\nRegistrasi berhasil! Selamat datang, {username}\n") 

     else:
        print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")

    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")