def catAndMouse(catA, catB, mosC):
    jarak_catA = abs(catA - mosC)
    jarak_catB = abs(catB - mosC)

    if jarak_catA < jarak_catB:
        return "Cat A"
    elif jarak_catB < jarak_catA:
        return "Cat B"
    else:
        return "Mouse C"

catA=int(input("Kucing A: "))
catB=int(input("Kucing B: "))
mosC=int(input("Tikus: "))
print(catAndMouse(catA, catB, mosC))