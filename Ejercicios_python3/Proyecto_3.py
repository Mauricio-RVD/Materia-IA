"""
Calculadora de propinas
#Precio de la fectura
#Porcentaje de propina
#Personas a repartir
"""
#Solcitar el importe total a pagar, el porcentaje de propina y la cantidad de personas
factura = float(input("Ingresa el importe de tu factura : "))
propina = int(input("Ingresa el el porcentaje de propina a dejar : "))
personas = int(input("Ingresa la cantidad de personas con las que se repartira la factura : "))

#Calcular el total a pagar
total_fact = factura * (1+(propina/100))
#Calcular la cantidad a pagar por persona
aporte_x_persona = total_fact/personas

#Imprimir resultado
print("El total de la factura es {} y la cantidad a pagar por persona es de {}".format(total_fact,aporte_x_persona))