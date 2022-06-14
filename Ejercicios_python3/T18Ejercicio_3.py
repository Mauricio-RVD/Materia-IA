#Ejercicio
"""
Apartir de la lista "numeros" que contiene números del 1 al 10,
Obtener una nueva lista con todos los elementos incrementados en 10 unidades
"""

#Hacer uso del map
resultado = map(lambda numero: numero + 10,list(range(1,11))) # Hacer uso de una función lambda

#Imprimir resultado
for num in resultado:
    print(num)