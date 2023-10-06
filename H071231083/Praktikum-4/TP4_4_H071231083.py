def catAndMouse(catA, catB, MouseC):
    a = abs(catA - MouseC)
    b = abs(catB - MouseC)

    if a > b :
        print("cat B")
    elif a < b :
        print("cat A")
    else :
        print("Mouse C")

catAndMouse(catA = 5, catB = 20, MouseC = 15)  