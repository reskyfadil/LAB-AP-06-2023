# Metode sorted:
# s1 = sorted(input('\nMasukkan kata pertama: ').replace(' ','').lower())
# s2 = sorted(input('Masukkan kata kedua: ').replace(' ','').lower())
# print(f'\n{s1 == s2}')


# Metoda count:
s1 = input('\nMasukkan kata pertama: ').replace(' ','').lower()
s2 = input('Masukkan kata kedua: ').replace(' ','').lower()

x, y = 0, 0
for i in s1:
    x += s1.count(i)
    y += s2.count(i)
print(x == y)