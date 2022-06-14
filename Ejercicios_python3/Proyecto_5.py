"""
Juego de piedra, papel, tijera

El usuario elige también su opción
Ordenador elige un opción aleatoria

Resultado
La tijera gana al papel
El papel gana a la piedra
La piedra gana a la tijera
"""
#Importar libreria
import random
#Solicitar elección del usuario
eleccionP =  input("Elige [Piedra | Papel | Tijera] : ")
#Normalizar respuesta
eleccionP= eleccionP.lower().strip()
#Generar opcion del ordenador
eleccionC = random.randint(0,2)
#Comprobar quien gano
# 0 = Piedra, 1 = Papel, 2 = Tijera
if eleccionP == "tijera" and eleccionC ==1 :
    print("La computadora eligio papel, tu ganas !!!")
elif eleccionP == "papel" and eleccionC == 0:
    print("La computadora eligio piedra, tu ganas !!!")
elif eleccionP == "piedra" and eleccionC == 2:
    print("La computadora eligio tijera, tu ganas!!!")
else:
    print("Perdiste")
