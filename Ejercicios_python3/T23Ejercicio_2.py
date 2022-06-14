#Ejercicio
"""
Crear un array con 100 números enterios aleatorios con valores comprendidos entre 0 y 500
Utilizar un diagrama de caja para representar los valores aleatorios generados
"""
#Importar liberias
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
#Generar lista de valores aleatorios
lista = np.random.randint(0,500,100)
#Generar diagrama de caja y  mostrar
sns.boxplot(lista)
plt.show()