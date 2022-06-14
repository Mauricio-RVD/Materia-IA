#Ejercicio
"""
Crear una base de datos "basededatos.db"
Crear una tabla "productos" con 3 campos
    id : Identificador del producto de tipo numérico
    nombre : Nombre del producto de tipo texto
    precio : Precio del producto de tipo numérico

Insertar 3 productos en la tabla "productos"
    1,"Impresora",300
    2,"Raton",20
    3,"Ordenador",600

Consultar los productos de la tabla "productos"
Cerrar la base de datos "basededatos.db"
"""
#Importar sqllite
import sqlite3
#Crear tabla y establecer la conexión con la base de datos
conexion = sqlite3.connect("basededatos.db")
#Crear un cursor para ejecutar las sentencias
cursor = conexion.cursor()

#Crear la tabla
cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER ,nombre TEXT ,precio INTEGER)")

#Ingresar registros
lista_productos = [(1,"Impresora",300),(2,"Raton",20),(3,"Ordenador",600)]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",lista_productos)

#Guardar cambios
conexion.commit()

#Consultar registros
cursor.execute("SELECT * FROM PRODUCTOS")
#Guardar lista
lista_Devuelta = cursor.fetchall()
#Mostrar elementos de la lista
for producto in lista_Devuelta:
    print(producto)

#Cerrar conexión
conexion.close()