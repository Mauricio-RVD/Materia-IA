#Ejercicio
"""
1.Imprime por pantalla el texto "Introduce el primer número"
2.Crear la variable "dato1" con el primer valor introducido en el paso anterior
3.Imprime por pantalla el texto "Introduce el segundo número"
4.Crear la variable "dato2" con el primer valor introducido en el paso anterior
5.Convertir la variable "dato1" en una variable numérica denominada "numero1"
6.Convertir la variable "dato2" en una variable numérica denominada "numero2"
7.Crear la variable "suma" con la suma de "numero1" y "numero2"
8.Convertir la variable "suma" en una variable de texto denominada "strSuma"
9.Crear la variable "resultado" con la concatenación de "La suma es " y "strSuma"
10.Imprimir el valor de "resultado"
"""
#Recibir datos y convertirlos
numero1 = int(input("Introduce el primer número : "))
numero2 = int(input("Introduce el segundo número : "))
#Reslizar suma , convertirla y concatenarla
resultado = "La suma es " + str(numero1 + numero2)
#Mostrar resultado
print(resultado)