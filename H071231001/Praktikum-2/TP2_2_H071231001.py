print('\nPenentuan Organisme\n===================\n')

a = input('Masukkan input pertama: ').lower()
b = input('Masukkan input kedua: ').lower()
c = input('Masukkan input ketiga: ').lower()

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('\nagula\n')
        elif c == 'onivoro':
            print('\npomba\n')
        else:
            print('\nInvalid input\n')
    elif b == 'mamifero':
        if c == 'onivoro':
            print('\nhomem\n')
        elif c == 'herbivoro':
            print('\nvaca\n')
        else:
            print('\nInvalid input\n')
    else:
        print('\nInvalid input\n')
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('\npulga\n')
        elif c == 'herbivoro':
            print('\nlagarta\n')
        else:
            print('\nInvalid input\n')
    elif b == 'anelideo':
        if c == 'hematofago':
            print('\nsanguessuga\n')
        elif c == 'onivoro':
            print('\nminhoca\n')
        else:
            print('\nInvalid input\n')
    else:
        print('\nInvalid input\n')
else:
    print('\nInvalid input\n')