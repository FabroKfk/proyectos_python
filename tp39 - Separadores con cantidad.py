def separador(cadena,caracter,cantidad):
    for x in range(cantidad):
        cad2 = ""
        for x in range(len(cadena)):
            cad2 = cad2 + cadena[x] + caracter
        print(cad2[:-1])

def reemplazo_espacio(cadena,caracter,cantidad):
    for x in range(cantidad):
        frase = ""
        for x in range(len(cadena)):
            if cadena[x] == " ":
                frase = frase + caracter
            else:
                frase = frase + cadena[x]
        print(frase)

def clave(cadena,caracter,cantidad):
    for x in range(cantidad):
        clave = ""
        for digito in cadena:
            clave = clave + caracter
        print("Su contraseña es:",clave)

def puntos(cadena,caracter,cantidad):
    for x in range(cantidad):
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
canti = int(input("Cuantas veces desea ejecutar esta accion?: "))
separador(cadena,sepa,canti)
print("")
print("ESPACIOS EN BLANCO")
print("----------")
cadena = input("Ingrese una palabra: ")
sepa = input("Ingrese reemplazo para los espacios: ")
canti = int(input("Cuantas veces desea ejecutar esta accion?: "))
reemplazo_espacio(cadena,sepa,canti)
print("")
print("PASSWORD")
print("----------")
cadena = input("Ingrese clave: ")
canti = int(input("Cuantas veces desea ejecutar esta accion?: "))
clave(cadena,"*",canti)
print("")
print("NUMEROS")
print("----------")
cadena = input("Ingrese un numero: ")
canti = int(input("Cuantas veces desea ejecutar esta accion?: "))
puntos(cadena,".",canti)
