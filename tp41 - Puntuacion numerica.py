def separacion(cadena):
    digitos = ""
    posicion = -1
    punto = 0
    for x in range(len(cadena)):
        digitos = digitos + cadena[posicion]
        punto = punto + 1
        if punto == 3:
            digitos = digitos + "."
            punto = 0
        posicion = posicion - 1
    if digitos[-1] == ".":
        print(digitos[-2::-1])
    else:
        print(digitos[::-1])

num = input("Ingrese un numero: ")
separacion(num)
            
        
    
