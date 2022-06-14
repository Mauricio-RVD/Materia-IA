#Ejercicio
"""
1.Crear una variable "diccionario" con los pares de valores siguientes
    clave=uno   valor=one
    clave=dos   valor=two
    clave=tres   valor=three
2.Mostrar por pantalla el valor de la variable "diccionario"
3.Añadir un nuevo elemento al diccionario
    clave=cuatro    valor=four
4.Mostrar ahora el valor del diccionario
5.Recoger un valor introducido por teclado y almacenarlo en "dato"
6.Utilizar "dato" como clave del diccionario para recuperar su valor
"""
#Declarar el diccionario
diccionario = {"uno":"one","dos":"two","tres":"three"}
#Mostrar el diccionario
print(diccionario)
#Agregar elementos al diccionario
diccionario["cuatro"] = "four"
#Mostrar el diccionario
print(diccionario)
#Recibir un dato
dato = input("Ingrese una clave del diccionario :")
#Obtener valor del diccionario
if (dato in diccionario):
    print(diccionario[dato])
else:
    print("Clave no encontrada")