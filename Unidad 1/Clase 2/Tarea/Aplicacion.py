# Importaciones
from tkinter import *
from tkinter.messagebox import askyesno
import re
#Funciones
def validar():
    nombre=entry1.get()
    apellido=entry2.get()
    correo=entry3.get()
    edad=entry4.get()
    fecha=entry5.get()
    fecha_regex = r'^\d{2}/\d{2}/\d{4}$'  
    if len(nombre)!=0 or len(apellido)!=0 or len(correo)!=0 or len(edad)!=0 or len(fecha)!=0:
        if nombre.isalpha() and apellido.isalpha():
            if edad.isdigit():
                if  re.match(fecha_regex, fecha):
                    print("Usuario validado con éxito!!!")
                else:
                    print("Error: El campo Fecha de Nacimiento debe tener el formato dd/mm/yyyy.")
            else:
                print("Error: Por favor verifique el campo Edad e intente nuevamente.")
        else:
            print("Error: Los campos Nombre y/o Apellido sólo aceptan letras, por favor verifique.")
    else:
        print("Error: Por favor verifique que no hayan espacios en blanco.")
    
def salir():
    if askyesno("Salir de la aplicación",'¿Desea salir de la aplicación?'):
        ventana.destroy()
# Ventana
ventana=Tk()
ventana.title("App")
ventana.geometry("500x500")
ventana.config(bg="aquamarine3")

# Labels
label1=Label(ventana,text="Nombre",bg="aquamarine3")
label1.place(relx=0.05,rely=0.05,relwidth=0.1,relheight=0.05)
label2=Label(ventana,text="Apellido",bg="aquamarine3")
label2.place(relx=0.05,rely=0.2,relwidth=0.1,relheight=0.05)
label3=Label(ventana,text="Correo",bg="aquamarine3")
label3.place(relx=0.05,rely=0.35,relwidth=0.1,relheight=0.05)
label4=Label(ventana,text="Edad",bg="aquamarine3")
label4.place(relx=0.05,rely=0.5,relwidth=0.1,relheight=0.05)
label5=Label(ventana,text="Fecha de\nNacimiento",bg="aquamarine3")
label5.place(relx=0.03,rely=0.65,relwidth=0.15,relheight=0.05)

# Entrys
entry1=Entry(ventana,bg="beige")
entry1.place(relx=0.25,rely=0.05,relwidth=0.55,relheight=0.05)
entry2=Entry(ventana,bg="beige")
entry2.place(relx=0.25,rely=0.2,relwidth=0.55,relheight=0.05)
entry3=Entry(ventana,bg="beige")
entry3.place(relx=0.25,rely=0.35,relwidth=0.55,relheight=0.05)
entry4=Entry(ventana,bg="beige")
entry4.place(relx=0.25,rely=0.5,relwidth=0.55,relheight=0.05)
entry5=Entry(ventana,bg="beige")
entry5.place(relx=0.25,rely=0.65,relwidth=0.55,relheight=0.05)

# Buttons
boton1=Button(ventana,text="Validar",bg="aquamarine1",command=lambda:validar())
boton1.place(relx=0.25,rely=0.8,relwidth=0.2,relheight=0.1)
boton2=Button(ventana,text="Salir",bg="aquamarine1",command=lambda:salir())
boton2.place(relx=0.55,rely=0.8,relwidth=0.2,relheight=0.1)

ventana.mainloop()