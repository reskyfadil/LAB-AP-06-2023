
print('menghitung luas permukaan dan keliling segitiga XYZ')
X = float(input('panjang sisi X: '))
Y= float(input('panjang sisi Y: '))
Z = (X**2 + Y**2)**0.5

luas = float (0.5*X*Y)
keliling =float (X+Y+Z)
print(f'luas = {luas:.2f}')
print(f'keliling = {keliling:.2f}')