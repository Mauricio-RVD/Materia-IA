#Ejercicio
"""
1.Crea una variable "minimo" con el valor 20
2.Crea una variable "maximo" con el valor 500
3.Recoge un valor del teclado y almacénalo en la variable "dato"
4.Convierte la variable "dato" en un número y almacénalo en la variable "numero"
5.Si el "numero" es menor que el valor de "minimo", mostrar el texto "Valor bajo"
6.Si el "numero" es mayor que el valor de "maximo", mostrar el texto "Valor alto"
7.Si el "numero" está entre el valor de "minimo" y "maximo", mostrar "Valor medio"
"""
#Inicializar las variables
minimo = 20
maximo = 500
#Solicitar dato
numero = int(input("Ingresa algun número : "))
#Comparar y mostrar resultado
if (numero < minimo):
    print("Valor bajo")
elif(numero > maximo):
    print("Valor alto")
else:
    print("Valor medio")
