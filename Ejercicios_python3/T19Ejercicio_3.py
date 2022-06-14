#Ejercicio
"""
Crear una lista con los valores numéricos del 0 al 30
Crear otra lista con los primeros 10 valors de la lista inicial
Crear otra lista con los últimos 10 valores de la lista inicial
Crear un bucle que recorre esta ultima lista de valores finales
"""
#Import numpy
import numpy as np
#Crear arrays
lista_1 = np.arange(31)
lista_2 = lista_1[:10] # 10 primeros valores
lista_3 = lista_1[-10:] #10 ultimos valores
#Imprimir los ultimos 10 valores
print(lista_3)

