#Ejercicio
"""
Dado el fichero excel que os adjunto en varios formatos
Copiar los datos al portapapeles
Crear un dataframe "datos" con esos datos copiado.
Mostrar por pantalla, todos los datos del dataframe
Mostrar todos los nombre de columnas del dataframe
Mostrar la primera fila del dataframe
Mostrar la primera columna del dataframe
Mostrar todas las filas pero sólo las columnas "Continente" y "Poblacion"
Mostrar las primeras 3 filas del dataframe
Mostrar las 2 ultimas filas del dataframe
"""
#Importar el módulo pandas
import pandas as pd
#Guardar el tabla del portapapeles en un dataframe
datos = pd.read_clipboard()
#Mostrar todo el dataframe
print(datos)

print("-"*30 + "\n")#Crear espacio de división
print(datos.columns)#Mostrar todos los nombre de columnas del dataframe

print("-"*30 + "\n")#Crear espacio de división
print(datos.loc[0])#Mostrar la primera fila del dataframe

print("-"*30 + "\n")#Crear espacio de división
print(datos['Continente'])#Mostrar la primera columna del dataframe

print("-"*30 + "\n")#Crear espacio de división
print(datos[['Continente','Población']])#Mostrar todas las filas pero sólo las columnas "Continente" y "Poblacion"

print("-"*30 + "\n")#Crear espacio de división
print(datos.head(3))#Mostrar las primeras 3 filas del dataframe

print("-"*30 + "\n")#Crear espacio de división
print(datos.tail(2))#Mostrar las 2 ultimas filas del dataframe