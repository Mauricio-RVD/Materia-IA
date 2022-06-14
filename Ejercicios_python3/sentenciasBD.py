"""
Funciones con la base de datos libros
"""
#Importar libreria de sqlite
import sqlite3

def prepararConexion():
    """
    Función que crear la base de datos y la tabla en donde se realizaran las demas operaciones
    """
    #Conectarse con la base de datos
    conexion = sqlite3.connect("libros.db")
    #Crear cursor que servira para ejecutar las sentencias
    cursor = conexion.cursor()
    #Ejecutar sentencia
    cursor.execute("CREATE TABLE IF NOT EXISTS libro(id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, año INTEGER, isbn TEXT)")
    #Guardar cambios
    conexion.commit()
    #Cerrar conexión
    conexion.close()

def visualizar():
    """
    Función que retorna una lista de todos los registros dentro de la tabla libro
    """
    #Conectarse con la base de datos
    conexion = sqlite3.connect("libros.db")
    #Crear cursor que servira para ejecutar las sentencias
    cursor = conexion.cursor()
    #Ejecutar sentencia
    cursor.execute("SELECT * FROM libro")
    #Guardar lista obtenida
    resultado = cursor.fetchall()
    #Cerrar conexión
    conexion.close()
    #Devolver lista
    return resultado

def buscar(titulo="",autor="",anio=0,isbn=0):
    """
    Función que retorna una lista de todos los registros encontrados con las caracteristicas dadas
    """
    #Conectarse con la base de datos
    conexion = sqlite3.connect("libros.db")
    #Crear cursor que servira para ejecutar las sentencias
    cursor = conexion.cursor()
    #Ejecutar sentencia
    cursor.execute("SELECT * FROM libro WHERE titulo=? OR autor=? OR año=? OR isbn=?",(titulo,autor,anio,isbn))
    #Guardar lista obtenida
    resultado = cursor.fetchall()
    #Cerrar conexión
    conexion.close()
    #Devolver lista
    return resultado

def agregar(titulo,autor,anio,isbn):
    """
    Función que inserta un registro dentro de la tabla libro
    """
    #Conectarse con la base de datos
    conexion = sqlite3.connect("libros.db")
    #Crear cursor que servira para ejecutar las sentencias
    cursor = conexion.cursor()
    #Ejecutar sentencia
    cursor.execute("INSERT INTO libro VALUES (NULL,?,?,?,?)",(titulo,autor,anio,isbn))
    #Guardar cambios
    conexion.commit()
    #Cerrar conexión
    conexion.close()

def actualizar(titulo,autor,anio,isbn,idR):
    """
    Función que actualiza un registro
    """
    #Conectarse con la base de datos
    conexion = sqlite3.connect("libros.db")
    #Crear cursor que servira para ejecutar las sentencias
    cursor = conexion.cursor()
    #Ejecutar sentencia
    cursor.execute("UPDATE libro SET titulo=?, autor=?, año=?, isbn=? WHERE id=? ",(titulo,autor,anio,isbn,idR))
    #Guardar cambios
    conexion.commit()
    #Cerrar conexión
    conexion.close()

def borrar(idR):
    """
    Función que borra un registro
    """
    #Conectarse con la base de datos
    conexion = sqlite3.connect("libros.db")
    #Crear cursor que servira para ejecutar las sentencias
    cursor = conexion.cursor()
    #Ejecutar sentencia
    cursor.execute("DELETE FROM libro WHERE id=? ",(idR,))
    #Guardar cambios
    conexion.commit()
    #Cerrar conexión
    conexion.close()