#Ejercicio
"""
Crear una clase "Coche" que tenga estos atributos :
marca, color, combustible y cilindrada

Crear la función "_init_" que asigna los parametros de la clase a los atributos de la clase

Crear otra función "mostrar_caracteristicas" que mediante print muestre por pantalla
las características (o atríbutos) que tiene el coche

Crear un objeto "coche1" de la clase "Coche" con los tributos "Opel", "rojo", "gasolina", "1.6"

Ejecutar las función "mostrar_caracteristicas" del objeto "coche1"
"""
#Crear clase coche
class Coche:
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self):
        print("El coche es de la marca {}, de color {}, usa {} y tiene una cilindrada de {}".format(self.marca,self.color,self.combustible,self.cilindrada))

#Crear objeto
coche1 = Coche("Opel", "rojo", "gasolina", "1.6")
#Ejecutar método
coche1.mostrar_caracteristicas()