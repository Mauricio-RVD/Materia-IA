#Ejercicio
"""
Crear 2 arrays con 9 números aleatorios enterios entre los valores 0 y 100
Cambiar el formato de los arrays en una estructura de 3 filas por 3 columnas
Crear 2 dataframes con esos arrays
Concatenar esos 2 dataframes
"""
#Importar librerias
import pandas as pd
import numpy as np
#Crear arrays de números aleatorios
arreglo1 = np.random.randint(0,100,9)
arreglo2 = np.random.randint(0,100,9)
#Redimencionar arrays
arreglo1.resize(3,3)
arreglo2.resize(3,3)
#Crear dataframes
dataframe_1 = pd.DataFrame(arreglo1)
dataframe_2 = pd.DataFrame(arreglo2)
#Concatenar ambos dataframes
dataframe_resultante = pd.concat([dataframe_1,dataframe_2],ignore_index=True) # Indicar que se ignore el index del segundo elemento
#Mostrar resultado
print(dataframe_resultante)