#Ejercicio
"""
Crear la función "buscar" que mediante una expresion regular indique si una palabra está en una frase

Probar la función "buscar" con estas frases
    texto = "Esto es una frase de pruebas para hacer busquedas"
    palabra_a_buscar = 'frase'
En caso de encontrar la palabra en la frase, indicar en que posición empieza y en cual finaliza
"""
#Importar re
import re
#Crear función
def buscar (texto,frase):
    #Buscar elemento
    resultado = re.search(frase,texto)
    #Mostrar resultado
    if (resultado):
        print("La frase '{}' se encuentra de la posición [{}-{}] en el texto '{}'".format(frase,resultado.start(),resultado.end(),texto))

#Hacer uso de la función
texto = "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = 'frase'
buscar(texto,palabra_a_buscar)