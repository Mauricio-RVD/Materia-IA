#Ejercicio
"""
Crear un modulo "modulo1.py"
Añadir la clase "Coche" creada en un ejercicio anterior al modulo "modulo1"
Añadir la función lamda "media"creada en un ejercicio anterior al modulo "modulo1"

Crear un programa en Python "programa1.py"
Importar el modulo "modulo1" antes creado
Crear un objeto "coche1" al instanciar la clase "Coche"
Mediante print mostrar las caracteristicas del coche
Calcular la media de 3 notas y mostrar el resultado con print

Ejecutar el programa "T9Ejercicio_1.py" y ver el resultado
"""
#Importar modulo
import T9Ejercicio_Modulo1
#Crear objeto coche
coche1 = T9Ejercicio_Modulo1.Coche("Opel", "rojo", "gasolina", "1.6")
#Obtener media
media = T9Ejercicio_Modulo1._calcular_media(10,9,8)
#Mostrar ambos resultado
coche1.mostrar_caracteristicas()
print(media)