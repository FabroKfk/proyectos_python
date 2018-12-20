def separador(cadena,caracter):
    cad2 = ""
    for x in range(len(cadena)):
        cad2 = cad2 + cadena[x] + caracter
    print(cad2[:-1])

def reemplazo_espacio(cadena,caracter):
    frase = ""
    for x in range(len(cadena)):
        if cadena[x] == " ":
            frase = frase + caracter
        else:
            frase = frase + cadena[x]
    print(frase)

def clave(cadena,caracter):
    clave = ""
    for digito in cadena:
        clave = clave + caracter
    print("Su contraseña es:",clave)

def puntos(cadena,caracter):
    digitos = ""
    p = 0
    for x in range(len(cadena)):
        p = p + 1
        digitos = digitos + cadena[x]
        if p > 2:
            digitos = digitos + caracter
            p = 0
    if digitos[-1] == ".":
        print(digitos[0:-1])
    else:
        print(digitos)
        
print("SEPARADORES")
print("----------")
cadena = input("Ingrese una palabra: ")
sepa = input("Ingrese separador: ")
separador(cadena,sepa)
print("")
print("ESPACIOS EN BLANCO")
print("----------")
cadena = input("Ingrese una palabra: ")
sepa = input("Ingrese reemplazo para los espacios: ")
reemplazo_espacio(cadena,sepa)
print("")
print("PASSWORD")
print("----------")
cadena = input("Ingrese clave: ")
clave(cadena,"*")
print("")
print("NUMEROS")
print("----------")
cadena = input("Ingrese un numero: ")
puntos(cadena,".")

    
