"""
Calcular el número de botes de pintura que hacen falta para pintar una pared
Pediremos al usuario
    Alto de la pared
    Ancho de la pared
    Cuantos metros cuadrados cubre un bote de pintura
Crearemos una función que calcule el número de botes
    Formula = (Alto * Ancho) / m2 que cubre cada bote
"""
#Definir función
def calcular (alto,ancho,rendimientoP):
    #Calcular num de botes de pintura necesarios y devolver resultado
    return (alto * ancho)/rendimientoP
#Solicitar información
alto = int(input("Ingrese el alto de la pared a pintar : "))
ancho = int(input("Ingrese el ancho de la pared a pintar : "))
rendimientoP = int(input("Ingrese cuantos metros cuadrados cubre el bote de pintura : "))
#Realizar calculo
resultado = calcular(alto,ancho,rendimientoP)
#Mostrar resultado
print("La cantidad de botes de pintura necesarios para pintar la pared es de {}".format(resultado))