import random

def domino(dom1,dom2):
    print("")
    if dom1[1] == dom2[0]:
        print("Encajan")
    else:
        print("No encajan")

print("DOMINO - FICHAS")
print("----------")
d1c1 = random.randint(1,6)
d1c2 = random.randint(1,6)
d2c1 = random.randint(1,6)
d2c2 = random.randint(1,6)

dom1 = (d1c1,d1c2)
dom2 = (d2c1,d2c2)

print("[",dom1[0],":",dom1[1],"]","[",dom2[0],":",dom2[1],"]")

domino(dom1,dom2)
