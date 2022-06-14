"""
Crear una interfaz visual para gestionar los registros de una base de datos
Base de datos -> tabla : libros
                    Título TEXT
                    Año INTEGER
                    Autor TEXT
                    ISBN TEXT
"""
#Importar librerias
from tkinter import *
import sentenciasBD

# Configuración de la raíz
raiz = Tk()
# Establecer título de la ventana 
raiz.title("Hola mundo")
# Desactivar redimensión de ventana    
raiz.resizable(False,False)

#Crear frame que contendra todo
ventana = Frame(raiz)
ventana.pack()

#/---------- Funciones ----------/

#Preparar la base de datos con la que se operara
sentenciasBD.prepararConexion()

def limpiarCampos ():
    #Vaciar la información de las entradas de texto
    tbx_titulo.delete(0,END)
    tbx_autor.delete(0,END)
    tbx_anio.delete(0,END)
    tbx_isbn.delete(0,END)

def funVisualizar ():
    #Borrar la información actual de la lista
    lista.delete(0,END)
    #Obtener la lista de libros de la base de datos
    listaResultante = sentenciasBD.visualizar()
    #Agregar registros a la lista
    for registro in listaResultante:
        lista.insert(END,registro)

def funBuscar():
    #Borrar la información actual de la lista
    lista.delete(0,END)
    #Obtener los registros encontrados en la base de datos
    listaResultante = sentenciasBD.buscar(titulo.get(),autor.get(),anio.get(),isbn.get())
    #Agregar registros a la lista
    for registro in listaResultante:
        lista.insert(END,registro)

def funAgregar():
    #Llamar a la sentencia que agrega un registro
    sentenciasBD.agregar(titulo.get(),autor.get(),anio.get(),isbn.get())
    #Limpiar los campos
    limpiarCampos()
    #Llamar a la función que muestra los registros en la interfaz
    funVisualizar()

def funActualizar():
    #Llamar a la sentencia que agrega un registro
    sentenciasBD.actualizar(titulo.get(),autor.get(),anio.get(),isbn.get(),regSeleccionado[0])
    #Limpiar los campos
    limpiarCampos()
    #Llamar a la función que muestra los registros en la interfaz
    funVisualizar()

def funBorrar():
    #Llamar a la sentencia que agrega un registro
    sentenciasBD.borrar(regSeleccionado[0])
    #Limpiar los campos
    limpiarCampos()
    #Llamar a la función que muestra los registros en la interfaz
    funVisualizar()

def funRegSeleccionado(event):
    try:
        #Declrar variable que contendra el registro seleccionado
        global regSeleccionado
        #Obtener el id del elemento seleccionado
        identificador = lista.curselection()[0]
        #Obtener el registro completo
        regSeleccionado = lista.get(identificador)
        #Limpiar todos los campos
        limpiarCampos()
        #Rellenarlos con el registro seleccionado
        tbx_titulo.insert(END,regSeleccionado[1])
        tbx_autor.insert(END,regSeleccionado[2])
        tbx_anio.insert(END,regSeleccionado[3])
        tbx_isbn.insert(END,regSeleccionado[4])
    except IndexError:
        pass

#/---------- Elementos visuales ----------/

#Etiquetas
lb_titulo = Label(ventana,text = "Título")
lb_titulo.grid(row=0,column=0)

lb_autor = Label(ventana,text = "Autor")
lb_autor.grid(row=0,column=2)

lb_anio = Label(ventana,text = "Año")
lb_anio.grid(row=1,column=0)

lb_isbn = Label(ventana,text = "ISBN")
lb_isbn.grid(row=1,column=2)

#Entradas de texto
titulo = StringVar() #Variable que contendra el valor ingresado
tbx_titulo = Entry(ventana,textvariable=titulo)
tbx_titulo.grid(row=0,column=1,pady=5,padx=5)

autor = StringVar() #Variable que contendra el valor ingresado
tbx_autor = Entry(ventana,textvariable=autor)
tbx_autor.grid(row=0,column=3,pady=5,padx=5)

anio = StringVar() #Variable que contendra el valor ingresado
tbx_anio = Entry(ventana,textvariable=anio)
tbx_anio.grid(row=1,column=1,pady=5,padx=5)

isbn = StringVar() #Variable que contendra el valor ingresado
tbx_isbn = Entry(ventana,textvariable=isbn)
tbx_isbn.grid(row=1,column=3,pady=5,padx=5)

#Botones
btn_visualizar = Button(ventana,text="Visualizar",width=16,height=1,command = funVisualizar)
btn_visualizar.grid(row=2,column=3,pady=5,padx=5)

btn_buscar = Button(ventana,text="Buscar",width=16,height=1,command = funBuscar)
btn_buscar.grid(row=3,column=3,pady=5,padx=5)

btn_aniadir = Button(ventana,text="Añadir",width=16,height=1,command = funAgregar)
btn_aniadir.grid(row=4,column=3,pady=5,padx=5)

btn_actualizar = Button(ventana,text="Actualizar",width=16,height=1,command = funActualizar)
btn_actualizar.grid(row=5,column=3,pady=5,padx=5)

btn_borrar = Button(ventana,text="Borrar",width=16,height=1,command = funBorrar)
btn_borrar.grid(row=6,column=3,pady=5,padx=5)

#Lista y scrollbar
lista = Listbox(ventana,height=10,width=25)
lista.grid(row=2,column=0,rowspan=5,columnspan=2)

scrollbar = Scrollbar (ventana)
scrollbar.grid(row=2,column=2,rowspan=5)

#Configurar ambos elementos para enlazarlos
lista.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista.yview)

#Agregar evento a la lista al momento de seleccionar un registro de la lista
lista.bind('<<ListboxSelect>>',funRegSeleccionado)

# Lanzar la aplicación en bucle
ventana.mainloop()