#input
a = int(input("input a = "))
if a == 0:
    print("input a tidak boleh sama dengan 0!")
    exit()
b = int(input("input b = "))
c = int(input("input c = "))

x1 = (-b + (b**2 - 4*a*c)**0.5)/2*a
x2 = (-b - (b**2 - 4*a*c)**0.5)/2*a
print(x1)
print(x2)