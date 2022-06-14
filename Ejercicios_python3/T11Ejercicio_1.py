#Ejercicio
"""
Crear el diccionario "frutas"
frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

Grabar esta estructura de datos "frutas" en un fichero binario "fichero.pckl"
Ya que en un fichero de texto, solo se guardan caracteres, pero no se pueden guardarr estas estructuras
"""
#Importar pickle
import pickle
#Crear diccionario
frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}
#Guardar diccionario
fichero = open("ficheroT11","wb")
pickle.dump(frutas,fichero)
fichero.close()
#Verificar datos
fichero = open("ficheroT11","rb")
diccionario = pickle.load(fichero)
print(diccionario.values())
