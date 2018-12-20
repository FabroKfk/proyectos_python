def inicial(cadena):
    print("Iniciales:")
    digito = cadena.split(" ")
    for x in range(len(digito)):
        print(digito[x][0],end="")
    print("")
    
    print("----------------")
    print("Mayusculas:")
    mayus = cadena.title()
    print(mayus)

    print("----------------")
    print("Palabras con A:")
    frase = cadena.split(" ")
    for x in range(len(frase)):
        if frase[x][0] == "a" or frase[x][0] == "A":
            print(frase[x])
    
cadena = input("Ingrese una oracion: ")
inicial(cadena)
