#Crear clase coche
class Coche:
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada
    
    def mostrar_caracteristicas(self):
        print("El coche es de la marca {}, de color {}, usa {} y tiene una cilindrada de {}".format(self.marca,self.color,self.combustible,self.cilindrada))

#Crear función lambda
_calcular_media = lambda nota1,nota2,nota3 : (nota1 + nota2 + nota3)/3