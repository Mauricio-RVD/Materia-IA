#Ejercicio
"""
Vamos a filtrar datos en un DataFrame.

Crearemos una lista de 50 valores aleatorios enteros entre los valores 0 y 100
Convertiremos esta lista en un dataframe con 5 filas y 10 columnas
Filtraremos los datos del dataframe para visualizar solo los valores que sean mayores de 50
"""
#Importar librerias
import pandas as pd
import numpy as np 
#Generar la lista de números
numeros = np.random.randint(0,100,50)
# Redimensionar la lista de números
numeros.resize(5,10)
#Generar el dataframe
dataframe = pd.DataFrame(numeros) 
#Filtrar el dataframe y mostrarlo
print(dataframe[dataframe > 50])