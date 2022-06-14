"""
Programar una calculadora junto con el modulo Tkinter
"""
#Importar librerias
import tkinter

#Configurar la ventana
ventana = tkinter.Tk()
ventana.title("Calculadora")
ventana.resizable(False,False)

#Crear frame y configurarlo
frame = tkinter.Frame(ventana)
frame.config(bg="gray7",width=500,height=500)
frame.pack()
#/-------------- Funciones --------------/
#Variables
operacion = ""
resultado = ""
def borrar():
    global operacion
    global resultado
    operacion = ""
    display.delete(0,tkinter.END)

def pulsar(valor):
    global operacion
    global resultado
    operacion += str(valor)
    display.delete(0,tkinter.END)
    display.insert(0,operacion)

def calcular():
    global operacion
    global resultado
    try:
        resultado = str(eval(operacion))
    except:
        resultado = "Error !!!"
        borrar()
    finally:
        display.delete(0,tkinter.END)
        display.insert(0,resultado)
#/-------------- Botones --------------/

#Estandar de botones
ancho = 8
alto = 3
#Display
display = tkinter.Entry(frame,font=("Comic Sans MS", 20, "bold"),bg="gray12",borderwidth=0,foreground="white",justify=tkinter.RIGHT)
display.grid(row=0,column=0,columnspan=4,pady=5,padx=5)

#C
botonC=tkinter.Button(frame,text="C",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:borrar())
botonC.grid(row=1,column=2,pady=5,padx=5)

# =
botonC=tkinter.Button(frame,text="=",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:calcular())
botonC.grid(row=5,column=3,pady=5,padx=5)

#Operaciones
#+
botonC=tkinter.Button(frame,text="+",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar("+"))
botonC.grid(row=1,column=3,pady=5,padx=5)
#-
botonC=tkinter.Button(frame,text="-",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar("-"))
botonC.grid(row=2,column=3,pady=5,padx=5)
#/
botonC=tkinter.Button(frame,text="/",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar("/"))
botonC.grid(row=3,column=3,pady=5,padx=5)
#*
botonC=tkinter.Button(frame,text="x",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar("*"))
botonC.grid(row=4,column=3,pady=5,padx=5)

#Números
#Num1
boton1 = tkinter.Button(frame,text="1",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(1))
boton1.grid(row=2,column=0,pady=5,padx=5)
#Num2
boton1 = tkinter.Button(frame,text="2",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(2))
boton1.grid(row=2,column=1,pady=5,padx=5)
#Num3
boton1 = tkinter.Button(frame,text="3",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(3))
boton1.grid(row=2,column=2,pady=5,padx=5)
#Num4
boton1 = tkinter.Button(frame,text="4",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(4))
boton1.grid(row=3,column=0,pady=5,padx=5)
#Num5
boton1 = tkinter.Button(frame,text="5",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(5))
boton1.grid(row=3,column=1,pady=5,padx=5)
#Num6
boton1 = tkinter.Button(frame,text="6",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(6))
boton1.grid(row=3,column=2,pady=5,padx=5)
#Num7
boton1 = tkinter.Button(frame,text="7",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(7))
boton1.grid(row=4,column=0,pady=5,padx=5)
#Num8
boton1 = tkinter.Button(frame,text="8",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(8))
boton1.grid(row=4,column=1,pady=5,padx=5)
#Num9
boton1 = tkinter.Button(frame,text="9",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(9))
boton1.grid(row=4,column=2,pady=5,padx=5)
#Num0
boton1 = tkinter.Button(frame,text="0",width=20,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar(0))
boton1.grid(row=5,column=0,columnspan=2,pady=5,padx=5)
#Punto
boton1 = tkinter.Button(frame,text=".",width=ancho,height=alto,bg="gray12",foreground="white",borderwidth=0,command=lambda:pulsar("."))
boton1.grid(row=5,column=2,pady=5,padx=5)
ventana.mainloop()