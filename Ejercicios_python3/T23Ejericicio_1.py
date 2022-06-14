#Ejercicio
"""
Crear una lista de 1000 valores aleatorios que sigan una distribución normal
Crear un histograma mediante matplotlib con la lista de valores
Crear un diagrama de caja (donde se acumula el 50% de los valores) mediante seaborn
"""
#Importar liberias
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#Generar lista de valores aleatorios
lista = np.random.randn(1000)
#Generar histograma y  mostrar
plt.hist(lista)
plt.show()
#Generar diagrama de caja
sns.boxplot(lista)
plt.show()