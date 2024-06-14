import os
import tkinter as tk
from tkinter.messagebox import showerror, showinfo, askyesno
from controller.ControllerCliente import ClienteController
from models.Cliente import Cliente

class ActualizarCliente():
    
    def actualizar_cliente(self):
        cliente_data = {
            "nombre": self.entryNombre.get(),
            "apellido": self.entryApellido.get(),
            "cedula": self.entryCedula.get(),
            "telefono": self.entryTelefono.get(),
            "correo": self.entryEmail.get()
        }
        if all(cliente_data.values()):
            if self.controlador.actualizar_cliente(cliente_data):
                showinfo("Éxito", "Cliente actualizado correctamente.")
                self.ventana.destroy()
        else:
            showerror("Error", "Por favor, completa todos los campos.")
    def buscar(self):
        cedula = self.entryCedula.get()
        if cedula:
            cliente = self.controlador.consultar_cliente_cedula(cedula)
            if cliente:
                self.entryNombre.config(state="normal")
                self.entryNombre.delete(0,tk.END)
                self.entryNombre.insert(0, cliente["nombre"])
                self.entryApellido.config(state="normal")
                self.entryApellido.delete(0,tk.END)
                self.entryApellido.insert(0, cliente["apellido"])
                self.entryTelefono.config(state="normal")
                self.entryTelefono.delete(0,tk.END)
                self.entryTelefono.insert(0, cliente["telefono"])
                self.entryEmail.config(state="normal")
                self.entryEmail.delete(0,tk.END)
                self.entryEmail.insert(0, cliente["correo"])
                self.entryCedula.config(state="disabled")
                self.boton_buscar.config(state="disabled")
        else:
            showerror("Error", "Por favor, ingrese la cédula del cliente.")
    def salir(self):
        if askyesno("Confirmación", "¿Desea salir de la aplicación?"):
            self.ventana.destroy()

    def __init__(self, ventanaPrincipal):
        self.ventana = tk.Toplevel(ventanaPrincipal)
        self.ventana.geometry("300x400")
        self.ventana.focus_set()
        self.ventana.title("Editar Cliente")
        self.ventana.config(bg="#2C3E50")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","actualizar_cliente.ico")
        self.ventana.iconbitmap(self.ruta_icono)
        
        self.cliente = Cliente(self.ventana)
        self.controlador = ClienteController(self.ventana)
        
        self.labelTitulo = tk.Label(self.ventana, text="Editar Cliente", font=("Arial", 12), bg="#2C3E50")
        self.labelTitulo.place(relx=0.5, rely=0.05, anchor="center")
        
        self.labelCedula = tk.Label(self.ventana, text="Cedula:", font=("Arial", 12), bg="lightblue")
        self.labelCedula.place(relx=0.1, rely=0.15, relheight=0.1, relwidth=0.2)
        self.entryCedula = tk.Entry(self.ventana, font=("Arial", 12),textvariable=self.cliente.cedula, bg="#CCDDFF")
        self.entryCedula.place(relx=0.4, rely=0.15, relheight=0.1, relwidth=0.3)
        self.entryCedula.bind("<Return>", lambda event: self.boton_buscar.invoke())

        
        self.labelNombre = tk.Label(self.ventana, text="Nombre:", font=("Arial", 12), bg="lightblue")
        self.labelNombre.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.2)
        self.entryNombre = tk.Entry(self.ventana, font=("Arial", 12),textvariable=self.cliente.nombre, bg="#CCDDFF")
        self.entryNombre.place(relx=0.4, rely=0.3, relheight=0.1, relwidth=0.3)
        self.entryNombre.bind("<Return>", lambda event: self.entryApellido.focus_set())
        self.entryNombre.config(state="disabled")
        
        self.labelApellido = tk.Label(self.ventana, text="Apellido:", font=("Arial", 12), bg="lightblue")
        self.labelApellido.place(relx=0.1, rely=0.45, relheight=0.1, relwidth=0.2)
        self.entryApellido = tk.Entry(self.ventana, font=("Arial", 12),textvariable=self.cliente.apellido, bg="#CCDDFF")
        self.entryApellido.place(relx=0.4, rely=0.45, relheight=0.1, relwidth=0.3)
        self.entryApellido.bind("<Return>", lambda event: self.entryTelefono.focus_set())
        self.entryApellido.config(state="disabled")
        
        self.labelTelefono = tk.Label(self.ventana, text="Teléfono:", font=("Arial", 12), bg="lightblue")
        self.labelTelefono.place(relx=0.1, rely=0.6, relheight=0.1, relwidth=0.2)
        self.entryTelefono = tk.Entry(self.ventana, font=("Arial", 12),textvariable=self.cliente.telefono, bg="#CCDDFF")
        self.entryTelefono.place(relx=0.4, rely=0.6, relheight=0.1, relwidth=0.3)
        self.entryTelefono.bind("<Return>", lambda event: self.entryEmail.focus_set())
        self.entryTelefono.config(state="disabled")
        
        self.labelEmail = tk.Label(self.ventana, text="Email:", font=("Arial", 12), bg="lightblue")
        self.labelEmail.place(relx=0.1, rely=0.75, relheight=0.1, relwidth=0.2)
        self.entryEmail = tk.Entry(self.ventana, font=("Arial", 12),textvariable=self.cliente.email, bg="#CCDDFF")
        self.entryEmail.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.3)
        self.entryEmail.config(state="disabled")

        self.boton_buscar = tk.Button(self.ventana,text="Buscar",font=("Arial",12),command=lambda:self.buscar(), relief="ridge", bg="lightblue")
        self.boton_buscar.place(relx=0.8,rely=0.15,relheight=0.1,relwidth=0.1)
        
        self.boton_guardar = tk.Button(self.ventana, text="Guardar", font=("Arial", 12), command=lambda:self.actualizar_cliente(), relief="ridge", bg="lightblue")
        self.boton_guardar.place(relx=0.8, rely=0.45, relheight=0.1, relwidth=0.1)
        
        self.boton_salir = tk.Button(self.ventana, text="Salir", font=("Arial", 12), command=lambda:self.salir(), relief="ridge", bg="lightblue")
        self.boton_salir.place(relx=0.8, rely=0.75, relheight=0.1, relwidth=0.1)

