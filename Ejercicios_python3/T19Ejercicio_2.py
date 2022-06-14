#Ejercicio
"""
1.- Crear una lista con números del 10 al 19
2.- Crear otra lista con números del 50 al 59
3.- Crear una matriz 2x10 con las listas anteriores
4.- Crear otra matriz que cuyos valores sean iguales a la matriz anterior multiplicados por 2
"""
#Import numpy
import numpy as np
#Crear listas
lista_num_1 = list(range(10,20))
lista_num_2 = list(range(50,60))
#Crear matriz
matriz = np.array((lista_num_1,lista_num_2))
#Multiplicar matriz
matriz_multi = matriz * 2
#Imprimir ambas matrices
print(matriz)
print(matriz_multi)
