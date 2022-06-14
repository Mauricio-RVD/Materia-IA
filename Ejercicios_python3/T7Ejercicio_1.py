#Ejercicio
"""
Crear un diccionario con los siguientes pares de valores
    manzana,apple
    naranja,orange
    platano,banana
    limon,lemon
Muestra la traducción para la palabra "naranja"
Añade un elemento nuevo con "piña" y "pineapple"
Haz un bucle para mostrar todos los elementos del diccionario
"""
#Declarar el diccionario
diccionario = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}
#Mostrar la traducción
print(diccionario["naranja"])
#Agregar elementos al diccionario
diccionario["piña"] = "pineapple"
#Mostrar el diccionario
for clave,valor in diccionario.items():
    print("La palabra clave [{}] tiene el valor de {}".format(clave,valor))