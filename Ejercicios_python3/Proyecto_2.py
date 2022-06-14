"""
Crear un programa en python que lea los datos del fichero comprimido, 
guarde la información en la base de datos SQlite, 
y realice consultas sobre los datos almacenados
"""
#Importar librerias
from asyncio.windows_events import NULL
from sqlite3 import Error
import sqlite3
import pandas as pd
import zipfile

#Crear variable que guarda el nombre del fichero
nombre = "coches.zip"
#Descomprimir fichero
with zipfile.ZipFile(nombre,'r') as zip:
    zip.extractall()
#Pasar los datos a un dataframe
dataframe = pd.read_csv(nombre,sep=';')
#Crear conexión a la base de datos
try:
    #Establecer conexión
    conexion = sqlite3.connect("coches.db")
    #Crear tablas
    #Crear un cursor para ejecutar las sentencias
    cursor = conexion.cursor()
    #Verificar si la tabla a crear existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='coche'")
    #Recuperar dato
    existe = cursor.fetchall()
    #Verificar si el valor devuelto es nulo -> nota: en python toda lista vacia es falsa
    if not existe:
        #Ejecutar sentencia
        cursor.execute('CREATE TABLE coche(marca text,modelo text, combustible text,transmision text,estado text,año_matricula text,kilometraje integer, potencia real, costo real)')
        #Insertar datos
        for fila in dataframe.itertuples():
            #Insertar todos los datos en una tupla
            coche = (fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
            #Ingresar la tupla en la tabla
            cursor.execute('INSERT INTO coche(marca,modelo,combustible,transmision,estado,año_matricula,kilometraje,potencia,costo) VALUES (?,?,?,?,?,?,?,?,?)',coche) 
        #Guardar cambios
        conexion.commit()
    #Consultar datos de la base de datos
    cursor.execute('SELECT * FROM coche LIMIT 15')
    #Guardar los datos
    datosBD = cursor.fetchall()
    #Recorrer la lista
    for registro in datosBD:
        #Imprimir registro
        print(registro)
    #Cerrar conexión
    conexion.close()
except Error:
    #Imprimir error
    print(Error)
