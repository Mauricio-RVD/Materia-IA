#Ejercicio
"""
Creamos una variable "nota" que tenga el valor 4.5
Creamos una vairable "trabajo_realizado" que tenga el valor "si"
Calcular el valor de la variable "nota_final", teniendo en cuenta que, si la nota_final es mayor o igual a 4, y el
valor de la variable "trabajo_realizado" es igual a "si", entonces "nota_final" sera igual a "aprobado", en caso contrario sera igual a "suspenso"
"""
#Declarar variables
nota = 4.5
trabajo_realizado = "si"
#Verificar nota
nota_final = "suspenso"
if (nota >= 4) and (trabajo_realizado == "si"):
    nota_final = "aprobado"
#Mostrar nota final
print(nota_final)