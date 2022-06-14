"""
Generador de contraseñas
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['¡','!','@','#','$','%','&','/','(',')','=','*','+','¿','?','-','_','{','}']

Preguntar por el número de letras, números y símbolos que quieres tener en la contraseña

#Generar una contraseña aleatoria mexcando lestras, números y símbolos de forma aleatoria
"""
import random

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','X','Y','Z']
numeros = ['0','1','2','3','4','5','6','7','8','9']
simbolos = ['¡','!','@','#','$','%','&','/','(',')','=','*','+','¿','?','-','_','{','}']

#Solicitar el número de elementos que quiere de cada tipo
nLetras = int(input("Ingresa el número de letras que quieres que contenga la contraseña : "))
nNumeros = int(input("Ingresa el número de números que quieres que contenga la contraseña : "))
nSimbolos =  int(input("Ingresa el número de símbolos que quieres que contenga la contraseña : "))

#Elegir de forma aleatoria cada uno de los elementos y guardarlo en una lista
elementosContra = []

#Letras
for cont in range(nLetras):
    #Seleccionar valor de forma aleatoria dentro de la lista letras y agregarlo la lista que contiene los caracteres de la contraseña
    elementosContra.append(random.choice(letras))

#Números
for cont in range(nNumeros):
    #Seleccionar valor de forma aleatoria dentro de la lista numeros y agregarlo la lista que contiene los caracteres de la contraseña
    elementosContra.append(random.choice(numeros))

#Símbolos
for cont in range(nSimbolos):
    #Seleccionar valor de forma aleatoria dentro de la lista simbolos y agregarlo la lista que contiene los caracteres de la contraseña
    elementosContra.append(random.choice(simbolos))

#Mezclar elementos de la lista
random.shuffle(elementosContra)

#Convertir lista a un string
contrasena = "".join(elementosContra)

#Imprimir resultado
print("Contraseña generada : {} ".format(contrasena))