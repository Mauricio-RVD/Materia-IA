#Ejercicio
"""
Leer el fichero adjunto "poblacion2.xlsx" y cargar los datos en un dataframe
Con esos datos, visualizar cuales la cuidad más poblada en América

Leer el fichero adjunto "poblacion2.1.cav" y cargarr los datos en un dataframe
Con esos datos, visualizar cual es la cuidad más poblada en Africa
Nota: necesario instalar openpyxl
"""
#Importar pandas
import pandas as pd

#Cargar los datos del excel
fichero_excel = pd.ExcelFile("\Elementos Programacion\Cursos\Python 3\poblacion2.xlsx")
tabla_excel = fichero_excel.parse('Hoja 1')
#Mostrar por pantalla la cuidad más poblada en América
print(tabla_excel['Ciudad más poblada'][3])
#Cargar el segundo archivo
tabla_csv = pd.read_csv("\Elementos Programacion\Cursos\Python 3\poblacion2.1.csv")
#Mostrar cual es la cuidad más poblada en Africa
print(tabla_csv['Ciudad más poblada'][1])