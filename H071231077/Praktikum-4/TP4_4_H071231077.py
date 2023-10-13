
def mouseAndCat(catA, catB, mosC):

    if abs(catA - mosC) < abs(catB - mosC):
        return "Cat A"
    elif abs(catA - mosC) > abs(catB - mosC):
        return "Cat B"
    else:
        return "Mouse C"


a = int(input('Masukkan posisi Cat A : '))
b = int(input('Masukkan posisi Cat B : '))
c = int(input('Masukkan posisi Mouse C : '))

hasil = mouseAndCat(a, b, c)
print(hasil)
