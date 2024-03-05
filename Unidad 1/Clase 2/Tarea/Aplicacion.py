# Importaciones
from tkinter import *
from tkinter.messagebox import askyesno
from tkcalendar import *
import re
#Funciones
def validarLetras(valor):
    patron=re.compile("^[A-Za-zñÑáéíóú]*$")
    resultado=patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True
def validarLetrasCorreo(valor):
    patron=re.compile("^[A-Za-zñÑ0-9.@]*$")
    resultado=patron.match(valor.get()) is not None
    if not resultado:
        return False
    return True
def validarNumeros(valor):
    num=re.compile("^[0-9]*$")
    resultado= num.match(valor.get())is not None
    if not resultado:
        return False
    return True
def evento_presionar_tecla(evento):
    global texto_validar_nombre
    global nombre
    global texto_validar_apellido
    global apellido
    global texto_validar_correo
    global correo
    global texto_validar_edad
    global edad
    if validarLetras(nombre):
        texto_validar_nombre = ""
    else:
        texto_validar_nombre = "Sólo se permiten letras en el campo"
    labelValidacionNombre.config(text= texto_validar_nombre,fg="red")
    if validarLetras(apellido):
        texto_validar_apellido = ""
    else:
        texto_validar_apellido="Sólo se permiten letras en el campo"
    labelValidacionApellido.config(text=texto_validar_apellido,fg="red")
    if validarLetrasCorreo(correo):
        texto_validar_correo = ""
    else:
        texto_validar_correo="Sólo se permiten letras/numeros/./@"
    labelValidacionCorreo.config(text=texto_validar_correo,fg="red")
    if validarNumeros(edad):
        texto_validar_edad = ""
    else:
        texto_validar_edad = "Sólo se permiten números"
    labelValidacionEdad.config(text=texto_validar_edad,fg="red")

def validar_boton():
    nombre_sin_espacios = nombre.get().strip()
    apellido_sin_espacios = apellido.get().strip()
    correo_sin_espacios = correo.get().strip()
    edad_sin_espacios = edad.get().strip()

    if not (nombre_sin_espacios and apellido_sin_espacios and correo_sin_espacios and edad_sin_espacios):
        texto_validacion = "Verifique que no hayan campos en blanco"
    elif (validarLetras(nombre) and validarLetras(apellido) and validarLetrasCorreo(correo) and validarNumeros(edad)):
        texto_validacion= "Usuario Validado con Éxito!!!"
    else:
        texto_validacion = "Hay algún campo incorrecto"
    labelValidacion.config(text=texto_validacion,fg="red")
    
def salir():
    if askyesno("Salir de la aplicación",'¿Desea salir de la aplicación?'):
        ventana.destroy()
# Ventana
ventana=Tk()
ventana.title("App")
ventana.geometry("500x500")
ventana.config(bg="aquamarine3")

# Labels
nombre=StringVar(ventana)
apellido=StringVar(ventana)
correo=StringVar(ventana)
edad= StringVar(ventana)
labelnombre=Label(ventana,text="Nombre",bg="aquamarine3")
labelnombre.place(relx=0.05,rely=0.1,relwidth=0.1,relheight=0.05)
labelapellido=Label(ventana,text="Apellido",bg="aquamarine3")
labelapellido.place(relx=0.05,rely=0.25,relwidth=0.1,relheight=0.05)
labelcorreo=Label(ventana,text="Correo",bg="aquamarine3")
labelcorreo.place(relx=0.05,rely=0.4,relwidth=0.1,relheight=0.05)
labeledad=Label(ventana,text="Edad",bg="aquamarine3")
labeledad.place(relx=0.05,rely=0.55,relwidth=0.1,relheight=0.05)
labelfecha=Label(ventana,text="Fecha de\nNacimiento",bg="aquamarine3")
labelfecha.place(relx=0.03,rely=0.7,relwidth=0.15,relheight=0.05)
label6=Label(ventana,text="Registre su Información",bg="aquamarine3")
label6.place(relx=0.35,rely=0.02,relwidth=0.3,relheight=0.05)
labelValidacionNombre=Label(ventana,text="",bg="aquamarine3")
labelValidacionNombre.place(relx=0.25,rely=0.15,relwidth=0.55,relheight=0.1)
labelValidacionApellido=Label(ventana,text="",bg="aquamarine3")
labelValidacionApellido.place(relx=0.25,rely=0.3,relwidth=0.55,relheight=0.1)
labelValidacionCorreo=Label(ventana,text="",bg="aquamarine3")
labelValidacionCorreo.place(relx=0.25,rely=0.45,relwidth=0.55,relheight=0.1)
labelValidacionEdad=Label(ventana,text="",bg="aquamarine3")
labelValidacionEdad.place(relx=0.25,rely=0.6,relwidth=0.55,relheight=0.1)
labelValidacion=Label(ventana,text="",fg="aquamarine3",bg="aquamarine3")
labelValidacion.place(relx=0.25,rely=0.75,relwidth=0.55,relheight=0.07)

# Entrys
entry_nombre=Entry(ventana,bg="beige",textvariable=nombre)
entry_nombre.bind("<KeyRelease>", evento_presionar_tecla)
entry_nombre.place(relx=0.25,rely=0.1,relwidth=0.55,relheight=0.05)
entry_apellido=Entry(ventana,bg="beige",textvariable=apellido)
entry_apellido.bind("<KeyRelease>",evento_presionar_tecla)
entry_apellido.place(relx=0.25,rely=0.25,relwidth=0.55,relheight=0.05)
entry_correo=Entry(ventana,bg="beige",textvariable=correo)
entry_correo.bind("<KeyRelease>",evento_presionar_tecla)
entry_correo.place(relx=0.25,rely=0.4,relwidth=0.55,relheight=0.05)
entry_edad=Entry(ventana,bg="beige",textvariable=edad)
entry_edad.bind("<KeyRelease>",evento_presionar_tecla)
entry_edad.place(relx=0.25,rely=0.55,relwidth=0.55,relheight=0.05)
entry_calendario=DateEntry(ventana,bg="beige",year=2000)
entry_calendario.place(relx=0.25,rely=0.7,relwidth=0.55,relheight=0.05)

# Buttons
boton1=Button(ventana,text="Validar",bg="aquamarine1",command=lambda:validar_boton())
boton1.place(relx=0.25,rely=0.82,relwidth=0.2,relheight=0.1)
boton2=Button(ventana,text="Salir",bg="aquamarine1",command=lambda:salir())
boton2.place(relx=0.55,rely=0.82,relwidth=0.2,relheight=0.1)

ventana.mainloop()