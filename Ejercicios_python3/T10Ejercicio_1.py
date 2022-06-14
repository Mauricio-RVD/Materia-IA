#Ejercicio
"""
Crear el modulo "moduloficheros.py"
    Crear una clase "Fichero"
    Crear la función "leer_fichero" para leer de un fichero de texto
    Crear la función "grabar_fichero" para crear un fichero de texto
    Crear la función "incluir_fichero" para incluir datos al final de un fichero de texto

Crear un programa "programa1.py"
    Crear el objeto "fichero" de la clase "Fichero" del modulo "moduloficheros.py"
    Utilizar el método "grabar_fichero" del objeto "fichero para crear un nuevo fichero de texto
    Utilizar el método "incluir_fichero" para incorportar más datos al final del fichero
    Utilizar el método "leer_fichero" para ver todo el contenido del fichero

Ejecutar el programa "programa1.py" desde la terminar de comandos
"""
#Importar modulo
import T10Ejercicio_Modulo
#Crear objeto
fichero = T10Ejercicio_Modulo.Fichero("ficheroT10")
#Ejecutar métodos
fichero.grabar_fichero()
fichero.incluir_fichero("Primera linea de texto")
fichero.incluir_fichero("\nSegunda linea de texto")
info_Optenida = fichero.leer_fichero()
print(info_Optenida)