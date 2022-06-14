#Ejercicio
"""
1.Crear una variable "numeros" con la lista de los números del uno al 10 (ambos incluidos)
2.Mostrar el valor de la variable "numeros"
3.Recoger un dato del teclado y almacenarlo en la variable "dato"
4.Convertir "dato" en numérico y almacenarlo en la variable "numero"
5.Si el valor de "numero" está en la lista de números,mostrar el mensaje "Si"
6.Si el numero introducido no está en la lista de números,mostrar el mensaje "No"
"""
#Declarar variables y mostrarla
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
#Solicitar dato
numero = int(input("Ingresa un número :"))
#Comprar dato
if (numero in numeros):
    print("Si")
else:
    print("No")
