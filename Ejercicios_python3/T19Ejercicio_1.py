#Ejercicio
"""
Crear la función "pares" que devuelva un array de números pares entre dos valores pasados como parametros a la
función (inicio y fin)
Utilizar la función "pares con los números 1 y 30
Utilizar la función "pares con los números 2 y 40
"""
#Importar numpy
import numpy as np
#Crear función
def pares (inicio,fin):
    #Ver si el inicio es impar
    if (inicio % 2 != 0):
        #Aumentar en 1 el inicio para convertirlo en par
        inicio += 1
    
    #Generar el array de números pares
    return np.arange(inicio,fin + 1,2)

#Probar la función
for num in pares(1,30):
    print (num)

for num in pares(2,40):
    print (num)