def tangkap (ab,bc,cc):
    a = abs(ab - cc)
    b = abs(bc - cc)
    if a > b :
        return('cat B')
    elif b > a:
        return ('cat A')
    else:
        return ('mouse C')
try:
    ab = int(input("Masukkan cat A: "))
    bc = int(input ("Masukkan cat B: "))
    cc = int(input ("Masukkan mouse C: "))
    print(tangkap (ab, bc, cc))
except ValueError:
    print ('Inputan hanya berupa integer')