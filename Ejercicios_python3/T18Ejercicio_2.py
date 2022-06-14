#Ejercicio
"""
Apartir de la lista "numeros" que contiene números del 1 al 10,
Obtener mediante "filter" una lista denominada "pares" con los númmeros pares de la lista "numeros"
"""
#Definir función de usará el filter
def pares (numero):
    return True if (numero % 2) == 0 else False #Hacer uso de un operador ternario 

#Hacer uso del filter
resultado = filter(pares,list(range(1,11)))

#Imprimir resultado
for num in resultado:
    print(num)