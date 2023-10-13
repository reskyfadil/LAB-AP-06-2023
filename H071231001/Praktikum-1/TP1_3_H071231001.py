a = int(input("input a = "))
b = int(input("input b = "))
c = int(input("input c = "))
if a == 0:
    print('a tidak boleh sama dengan nol')
else:
    x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
print(f'x1={x1:.2f}')
print(f'x2={x2:.2f}') 