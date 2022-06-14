#Ejercicio
"""
1.Crear una variable "tupla" que sea una tupla de los siguientes nombres: Antonio,Pedro y Maria
2.Mostrar el valor de la variable "tupla"
3.Recoger un dato por teclado y almacenarlo en la variable "dato"
4.Si el valor de "dato" está dentro de los valores de la variable "tupla", mostrar "Si"
5.Si el valor de "dato" no está dentro de los valores de la variable "tupla", mostrar "No"
"""
#Declarar la tupla
tupla = ("Antonio","Pedro","Maria")
#Mostrar tupla
print(tupla)
#Solicitar un dato
dato = input("Ingresado una palabra :")
#Verificar dato ingresado
if(dato in tupla):
    print("Si")
else:
    print("No")
