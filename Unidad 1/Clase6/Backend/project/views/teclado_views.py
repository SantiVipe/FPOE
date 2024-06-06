import tkinter as tk
from tkinter.messagebox import askyesno
from django.http import HttpResponse

def mostrar_ventana_tkinter(request):
    def salir():
        if askyesno("Salir de la aplicación",'¿Desea salir de la aplicación?'):
            ventana.destroy()
# Ventana
    ventana=tk.Tk()
    ventana.geometry("500x500")
    ventana.title("App")
    ventana.config(bg="aquamarine1")
    # labels
    label_titulo=tk.Label(ventana,text="Personalice su Teclado",bg="aquamarine1")
    label_titulo.place(relx=0.35,rely=0.05,relheight=0.1,relwidth=0.3)
    label_teclado=tk.Label(ventana,text="Teclado:",bg="aquamarine1")
    label_teclado.place(relx=0.1,rely=0.2,relheight=0.1,relwidth=0.1)
    label_switch=tk.Label(ventana,text="Switch:",bg="aquamarine1")
    label_switch.place(relx=0.1,rely=0.33,relheight=0.1,relwidth=0.1)
    label_keycaps=tk.Label(ventana,text="Keycaps:",bg="aquamarine1")
    label_keycaps.place(relx=0.1,rely=0.45,relheight=0.1,relwidth=0.1)
    label_formato=tk.Label(ventana,text="Formato:",bg="aquamarine1")
    label_formato.place(relx=0.1,rely=0.57,relheight=0.1,relwidth=0.1)
    label_conectividad=tk.Label(ventana,text="Conectividad:",bg="aquamarine1")
    label_conectividad.place(relx=0.07,rely=0.7,relheight=0.1,relwidth=0.17)
    # Entrys
    entry_teclado=tk.Entry(ventana,bg="aquamarine3")
    entry_teclado.place(relx=0.3,rely=0.2,relheight=0.1,relwidth=0.45)
    entry_switch=tk.Entry(ventana,bg="aquamarine3")
    entry_switch.place(relx=0.3,rely=0.33,relheight=0.1,relwidth=0.45)
    entry_keycaps=tk.Entry(ventana,bg="aquamarine3")
    entry_keycaps.place(relx=0.3,rely=0.45,relheight=0.1,relwidth=0.45)
    entry_formato=tk.Entry(ventana,bg="aquamarine3")
    entry_formato.place(relx=0.3,rely=0.57,relheight=0.1,relwidth=0.45)
    entry_conectividad=tk.Entry(ventana,bg="aquamarine3")
    entry_conectividad.place(relx=0.3,rely=0.7,relheight=0.1,relwidth=0.45)
    # Buttoms
    boton_guardar=tk.Button(ventana,text="Guardar",bg="aquamarine3",)
    boton_guardar.place(relx=0.3,rely=0.83,relheight=0.12,relwidth=0.17)
    boton_salir=tk.Button(ventana,text="Salir",bg="aquamarine3",command=lambda:salir())
    boton_salir.place(relx=0.58,rely=0.83,relheight=0.12,relwidth=0.17)

    ventana.mainloop()
    
    return HttpResponse("Ventana de Tkinter mostrada correctamente")
