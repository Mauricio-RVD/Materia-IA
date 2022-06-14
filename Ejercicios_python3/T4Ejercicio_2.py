#Ejercicio
"""
1.Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
2.Crear una variable "longitud" que contiene la longitud de la variable "cadena"
3.Crear una variable "strlongitud" que tenga el valor de "longitud" pero convertida a cadena de caracteres o string
4.Crear una variable "mayusculas" que contiene la variable "cadena" en mayusculas
5.Crear una variable "resultado" que concatene "mayusculas" con el texto " tiene longitud de " y "strlongitud"
"""
#Declarar variables
cadena = "Esto es un texto de ejemplo"
longitud = len(cadena)
strlongitud = str(longitud)
mayusculas = cadena.upper()
resultado = mayusculas + " tiene longitud de " + strlongitud
#Mostrar resultado
print(resultado)