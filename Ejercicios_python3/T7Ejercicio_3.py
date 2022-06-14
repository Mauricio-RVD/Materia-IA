#Ejercicio
"""
1.Crear una variable "inicio" con el valor 1
2.Crear una variable "fin" con el valor 6
3.Hacer un bucle while que muestre tantas filas como valores haya entre "inicio" y "fin"
4.En cada iteracción del bucle mostrar el texto "Esta es la fila " + número de fila en la que está
"""
#Declarar variables
inicio = 1
fin = 6
#Crear bucle while
while (inicio <= fin):
    #Imprimir fila
    print ("Esta es la fila " + str(inicio))
    #Aumentar en 1 a inicio
    inicio += 1