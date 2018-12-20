import random

def poker(c1,c2,c3,c4,c5):
    carta = 0
    cont = 0
    baraja = (c1,c2,c3,c4,c5)
    for k in range(len(baraja)):
        carta = baraja[k]
        for x in range(len(baraja)):
            if baraja[x] == carta:
                cont = cont + 1
    if cont == 17:
        print("")
        print("Es poker!")
    else:
        print("")
        print("No es poker...")

carta = random.randint(1,10)
c1 = (carta)
carta = random.randint(1,10)
c2 = (carta)
carta = random.randint(1,10)
c3 = (carta)
carta = random.randint(1,10)
c4 = (carta)
carta = random.randint(1,10)
c5 = (carta)

print("           CARTAS              ")
print("-----------------------------")
print("[",c1,"]","[",c2,"]","[",c3,"]","[",c4,"]","[",c5,"]")

poker(c1,c2,c3,c4,c5)


    
