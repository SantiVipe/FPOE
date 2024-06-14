import os
import tkinter as tk
from tkinter.messagebox import showerror,askyesno
from controller.ControllerCliente import ClienteController
from models.Cliente import Cliente

class BorrarCliente():

    def borrar(self):
        cedula= self.entryCedula.get()
        if cedula:
            cliente = self.controlador.eliminar_cliente_por_cedula(cedula)
        else:
            showerror("Error","La cédula no coincide con ningún cliente registrado")


    def salir(self):
       if askyesno("Confirmación","¿Desea salir de la aplicación?"):
            self.ventana.destroy() 

    def __init__(self, ventanaPrincipal):
        self.ventana= tk.Toplevel(ventanaPrincipal)
        self.ventana.geometry("500x500")
        self.ventana.focus_set()
        self.ventana.title("Borrar Cliente")
        self.ventana.config(bg="#FFCCCC")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","remover_cliente.ico")
        self.ventana.iconbitmap(self.ruta_icono)

        self.controlador = ClienteController(self.ventana)
        self.cliente = Cliente(self.ventana)

        self.labelTitulo = tk.Label(self.ventana,text="Borrar Cliente",font=("Arial",12), bg="#FFCCCC")
        self.labelTitulo.place(relx=0.5,rely=0.05,anchor="center")


        self.labelCedula = tk.Label(self.ventana,text="Cedula:",font=("Arial",12), bg="#CC3333")
        self.labelCedula.place(relx=0.1,rely=0.45,relheight=0.1,relwidth=0.2)
        self.entryCedula = tk.Entry(self.ventana,textvariable=self.cliente.cedula,font=("Arial",12), bg="#FFCCCC")
        self.entryCedula.place(relx= 0.4,rely=0.45,relheight=0.1,relwidth=0.3)

        self.boton_borrar = tk.Button(self.ventana,text="Borrar",font=("Arial",12),command=lambda:self.borrar(),bg="#CC3333")
        self.boton_borrar.place(relx=0.35,rely=0.8,relheight=0.1,relwidth=0.1)

        self.boton_salir = tk.Button(self.ventana,text="Salir",font=("Arial",12),command=lambda:self.salir(),bg="#CC3333")
        self.boton_salir.place(relx=0.55,rely=0.8,relheight=0.1,relwidth=0.1)

    