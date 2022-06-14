#Ejercicio
"""
Crear la función "primos" que será una función generadora de números primos entre en 0 y el 100
Esta es la lista de números primos entre 0 y 100
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

Utilizar la función generadora para mostrar por pantalla números primos menores de 50
"""
#Declarar lista de números primos
numeros_primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
#Generar números primos
def primos (max):
    #Verificar que el número sea menor o igual a 100
    if (max > 100):
        #Asignar un valor de 100 en caso de que el número sea mayor a 100
        max = 100

    #Generar números primos mediante un bucle
    for num in range(max):
        #Comprobar si el número pertenece a la lista
        if (num in numeros_primos):
            #Devolver valor
            yield num

#Llamar a la función e imprimirlos
for num_primo in primos(80):
    print (num_primo)