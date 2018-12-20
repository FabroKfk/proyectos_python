def primeros_dos(cadena):
    print("")
    print("Primeros dos caracteres: ")
    print(cadena[:2])
    print("--------------------")

def ultimos_tres(cadena):
    print("Ultimos tres: ")
    print(cadena[-3:])
    print("--------------------")

def cada_dos(cadena):
    print("De dos en dos: ")
    print(cadena[0::2])
    print("--------------------")


def inverso(cadena):
    print("Inverso: ")
    print(cadena[::-1])
    print("--------------------")


def reflejo(cadena):
    print("En reflejo: ")
    print(cadena[:],end="")
    print(cadena[::-1])

var = input("Ingrese una palabra: ")
primeros_dos(var)
ultimos_tres(var)
cada_dos(var)
inverso(var)
reflejo(var)

    
