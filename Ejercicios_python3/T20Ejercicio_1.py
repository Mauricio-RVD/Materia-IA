#Ejercicio
"""
Tenemos 3 clases "clase1","clase2","clase3"
Vamos a generar un número aleatorio de alumnos por clase
Para obtener un número aleatorio utilizaremos
    np.random.randint(minimo,maximo,numero)

Crear una serie de clases y alumnos
Utilizar el indice de la serie creada para saber el número de alumnos de la clase2
"""
#Importar módulos
import pandas as pd
import numpy as np
#Generar los alumnos por cada clase
num_alumnos = np.random.randint(10,40,3) # -> num min de alumnos | num max de alumnos | num de salones
#Crear serie
alumnos_x_clase = pd.Series (num_alumnos,index = ["Clase1","Clase2","Clase3"])
#Mostrar serie
print(alumnos_x_clase)
#Imprimir solo el número de alumnos de la clase2
print("El número de alumnos de la clase 2 es : {}".format(alumnos_x_clase["Clase2"]))