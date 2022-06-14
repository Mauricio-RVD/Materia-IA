"""
Subasta para calcular la apuesta más alta

Flujo de trabajo:
-Mensaje de bienvenida al programa de subasta
-Preguntar por el nombre del primer apostante
-Preguntar por el precio de su apuesta
-Añadir el nombre (clave) y su apuesta (valor) a un diccionario de apuestas
-Borrar la pantalla
-Preguntar si hay mas personas que quieren hacer su apuesta (si,no) (bucle hasta respues == no)
    Si respuesta = si
        -Preguntar nombre de la otra persona
        -Preguntar por su apuesta
        -Añadir el nombre(clave) y apuesta (valor) al diccionario de apuestas crado al inicio
        -Borra la pantalla
    Si respuesta = no
        -Mostrar la apesta ganadora de la subasta(apuesta con el precio más alto)
        -Fin del programa
"""
#Dar bienvenida
print("Bienvenido al programa de subasta")
#Preguntar por el primer apostador
nombre = input("Ingrese su nombre : ")
#Preguntar por la cantidad a apostar
apuesta =  int(input("Ingrese la cantidad a apostar : "))
#Ingresar apostador al diccionario
apostadores = {nombre:apuesta}
#Preguntar por si hay mas apostadores
respuesta = input("Hay mas personas que quieren apostar si|no : ")
#Normalizar respuesta
respuesta= respuesta.lower().strip()
#Ingresar al bucle en caso de si
while respuesta != "no" :
    #Preguntar por el nombre del apostador
    nombre = input("Ingrese su nombre : ")
    #Preguntar por la cantidad a apostar
    apuesta =  int(input("Ingrese la cantidad a apostar : "))
    #Ingresar apostador al diccionario
    apostadores[nombre] = apuesta
    #Preguntar por si hay mas apostadores
    respuesta = input("Hay mas personas que quieren apostar si|no : ")
    #Normalizar respuesta
    respuesta= respuesta.lower().strip()
#Identificar quien es el ganador
ganador = max(apostadores, key=lambda key: apostadores[key])
#Imprimir el nombre del ganador
print(ganador)