#Ejercicio
"""
Crear la función "operacion" que dados 3 números, divida el primer número entre la resta de los otros dos números

Utilizar la función creada con los números 5,4,2
Utilizar la función creada con los números 6,3,3

Utilizar el bloque try ... except para controlar cualquier posible error
"""
#Crear la función
def operacion (num1,num2,num3):
    resultado = 0 #Establecer resultado por defecto
    try:
        resultado = num1 / (num2 - num3)
    except ZeroDivisionError:
        print("Error de división entre cero")
    except:
        print("Ocurrio un error ...")
    finally:
        return resultado 

#Solicitar 3 números y operar con ellos
num1 = int(input("Ingresa un número : "))
num2 = int(input("Ingresa un segundo número : "))
num3 = int(input("Ingresa un tercer número : "))
#Llamar a la función
resultado = operacion(num1,num2,num3)
#Imprimir resultado
print(resultado)