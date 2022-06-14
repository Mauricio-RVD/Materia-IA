#Ejercicio
"""
Crear una variable "nota1" que tenga el valor 6
Crear otra variable "nota2" que tenga el valor 4
Crear otra variable "nota3" que tanfa el valor 7
Crear otra variable "nota_media" que tenga el valor medio de las 3 notas anteriores
Crear otra variable "nota_final" que tenga el valor "aprobado" (mayor o igual a 5)
"""
#Inicializar variables
nota1 = 6
nota2 = 4
nota3 = 7
#Obtener la media de las notas
nota_media = (nota1 + nota2 + nota3) / 3
#Comprobar la nota
nota_final = "no aprobado"
if (nota_media >= 5) :
    nota_final = "aprobado"
#Mostrar resultados
print(nota_final)