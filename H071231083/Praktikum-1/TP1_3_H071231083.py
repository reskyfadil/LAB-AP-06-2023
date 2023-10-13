#Persamaan kudarat
a = int(input("input a = "))
if a == 0:
    print("input a tidak boleh 0 !")
    exit() 
b = int(input("input b = "))
c = int(input("input c = "))

b1 = b ** 2
a1 = 2 * a
ac = 4 * a * c

x1 = (- b + ((b1 - ac)**0.5))/ a1
x2 = (- b - ((b1 - ac)**0.5))/a1

print(f'x1 = {x1:.2f}')
print(f'x2 = {x2:.2f}')