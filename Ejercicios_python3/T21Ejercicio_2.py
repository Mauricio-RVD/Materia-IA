#Ejercicio
"""
Obtener la tabla de paises de la pagina 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'
Limpiar los datos lo necesaro para que los nombres de las columnas sean correctos.
Nota: necesario instalar lxml y pasar archivos de una carpeta de miniconda
"""
#Importar pandas
import pandas as pd
url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'
tablas_wiki = pd.read_html(url)
#Guardar solo la tabla de paises
tabla_paises = tablas_wiki[0]
#Mostrar dataframe
print(tabla_paises)