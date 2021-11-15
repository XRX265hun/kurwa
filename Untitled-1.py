#kisértetház
from random import randint
print ("Kísértetház")
bátor_vagyok = True
pontszám = 0
while bátor_vagyok: 
    szellem_ajtó = randint (1, 3)
    print ("3 ajtó van")
    print ("Az egyik mögött szellem van")
    print ("melyiket nyitod ki?")
    ajtó = input("1,2 vagy 3?")
    ajtó_szám= int(ajtó)
    if ajtó_szám == szellem_ajtó:
        print("SZELLEM")
        bátor_vagyok = False
    else:
        print ("nincs szellem")
        print ("lépj a következő szintre")
        pontszám = + 1
print("MENEKÜLJ")
print("vége a játéknak az elért pontszám:", pontszám)
