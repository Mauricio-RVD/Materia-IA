"""
Elaborar una pregunta que realiza una serie de preguntas y con base a las respuestas perderemos o ganaremos
"""
#Importar librerias
import sys
#Realizar pregunta
print("Inicia el juego ...")
respuesta  = input("¿Izquierda o Derecha? : ")
#Normalizar respuesta
respuesta= respuesta.lower().strip()
#Comprobar respuesta
if respuesta == "izquierda":
    sys.exit("Fin ...")

#Realizar pregunta
respuesta  = input("Nadar o Esperar? : ")
#Normalizar respuesta
respuesta= respuesta.lower().strip()
#Comprobar respuesta
if respuesta == "nadar":
    sys.exit("Fin ...")

#Realizar pregunta
respuesta  = input("¿Rojo, Azul o Verde? : ")
#Normalizar respuesta
respuesta= respuesta.lower().strip()
#Comprobar respuesta
if respuesta == "rojo" or respuesta == "azul":
    sys.exit("Fin ...")

#Mostrar que ha ganado
print("Has ganado !!!")