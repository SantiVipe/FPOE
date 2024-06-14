import os
import tkinter as tk
from tkinter.messagebox import showerror,askyesno
from controller.ControllerCliente import ClienteController
from models.Cliente import Cliente

class CrearCliente():
    
    def guardar_cliente(self):
        cliente_data = {
            "nombre": self.entryNombre.get(),
            "apellido": self.entryApellido.get(),
            "cedula": self.entryCedula.get(),
            "telefono": self.entryTelefono.get(),
            "correo": self.entryEmail.get()
        }
        if all(cliente_data.values()):
            if self.controlador.comprobar_cedula(cliente_data['cedula']):
                showerror("Error", "Ya existe un cliente con esta cédula.")
            else:
                if self.controlador.guardar_cliente(cliente_data):
                    self.ventana.destroy()
        else:
            showerror("Error", "Por favor, completa todos los campos.")
    def salir(self):
        if askyesno("Confirmación","¿Desea salir de la aplicación?"):
            self.ventana.destroy()
    
    def __init__(self,ventanaPrincipal):
        
        self.ventana=tk.Toplevel(ventanaPrincipal)
        self.ventana.geometry("300x300")
        self.ventana.focus_set()
        self.ventana.title("Crear Cliente")
        self.ventana.config(bg="#98FB98")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","crear_cliente.ico")
        self.ventana.iconbitmap(self.ruta_icono)
        
        self.controlador = ClienteController(self.ventana)
        
        self.cliente = Cliente(self.ventana)
        
        self.labelTitulo = tk.Label(self.ventana,text="Registrar Cliente",font=("Arial",12), bg="#98FB98")
        self.labelTitulo.place(relx=0.5,rely=0.05,anchor="center")
        
        self.labelNombre = tk.Label(self.ventana,text="Nombre:",font=("Arial",12), bg="#9ACD32")
        self.labelNombre.place(relx=0.1,rely=0.2,relheight=0.1,relwidth=0.2)
        self.entryNombre = tk.Entry(self.ventana,textvariable=self.cliente.nombre,font=("Arial",12), bg="#E5F3E2")
        self.entryNombre.bind("<Return>", lambda event: self.entryApellido.focus_set())
        self.entryNombre.place(relx= 0.4,rely=0.2,relheight=0.1,relwidth=0.3)

        self.labelApellido = tk.Label(self.ventana,text="Apellido:",font=("Arial",12), bg="#9ACD32")
        self.labelApellido.place(relx=0.1,rely=0.35,relheight=0.1,relwidth=0.2)
        self.entryApellido = tk.Entry(self.ventana,textvariable=self.cliente.apellido,font=("Arial",12), bg="#E5F3E2")
        self.entryApellido.bind("<Return>", lambda event: self.entryCedula.focus_set())
        self.entryApellido.place(relx= 0.4,rely=0.35,relheight=0.1,relwidth=0.3)

        self.labelCedula = tk.Label(self.ventana,text="Cedula:",font=("Arial",12), bg="#9ACD32")
        self.labelCedula.place(relx=0.1,rely=0.5,relheight=0.1,relwidth=0.2)
        self.entryCedula = tk.Entry(self.ventana,textvariable=self.cliente.cedula,font=("Arial",12), bg="#E5F3E2")
        self.entryCedula.bind("<Return>", lambda event: self.entryTelefono.focus_set())
        self.entryCedula.place(relx= 0.4,rely=0.5,relheight=0.1,relwidth=0.3)

        self.labelTelefono = tk.Label(self.ventana,text="Teléfono:",font=("Arial",12), bg="#9ACD32")
        self.labelTelefono.place(relx=0.1,rely=0.65,relheight=0.1,relwidth=0.2)
        self.entryTelefono = tk.Entry(self.ventana,textvariable=self.cliente.telefono,font=("Arial",12), bg="#E5F3E2")
        self.entryTelefono.bind("<Return>", lambda event: self.entryEmail.focus_set())
        self.entryTelefono.place(relx= 0.4,rely=0.65,relheight=0.1,relwidth=0.3)

        self.labelEmail = tk.Label(self.ventana,text="Email:",font=("Arial",12), bg="#9ACD32")
        self.labelEmail.place(relx=0.1,rely=0.8,relheight=0.1,relwidth=0.2)
        self.entryEmail = tk.Entry(self.ventana,textvariable=self.cliente.email,font=("Arial",12), bg="#E5F3E2")
        self.entryEmail.place(relx= 0.4,rely=0.8,relheight=0.1,relwidth=0.3)
        
        self.boton_guardar = tk.Button(self.ventana, text="Guardar",font=("Arial",12), command=lambda: self.guardar_cliente(), bg="#9ACD32")
        self.boton_guardar.place(relx=0.8,rely=0.2,relheight=0.1,relwidth=0.1)

        self.boton_salir = tk.Button(self.ventana,text="Salir",font=("Arial",12),command=lambda:self.salir(), bg="#9ACD32")
        self.boton_salir.place(relx=0.8,rely=0.8,relheight=0.1,relwidth=0.1)