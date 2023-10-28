kata1=input('kata pertama = ')
kata2=input('kata kedua = ')
kata1=kata1.replace(" ","")
kata2=kata2.replace(" ","")

for huruf in kata1:
    hasil1=kata1.count(huruf)
    hasil2=kata2.count(huruf)
    if hasil1 == hasil2:
        continue
    else:
        print(False)
        break
if hasil1 == hasil2:
    print(True)