import tkinter as tk
import os
from PIL import Image,ImageTk
import pygame
import threading
from .CrearCliente import CrearCliente
from .ActualizarCliente import ActualizarCliente
from .ActualizarServicios import ActualizarServicios
from .BorrarCliente import BorrarCliente
from .BorrarServicio import BorrarServicio
from .ConsultarClientes import ConsultarCliente
from .ConsultarServicio import ConsultarServicio
from .CrearServicio import CrearServicio
from controller.BackupController import BackupController
class ventanaPrincipal():
    def ingresarCliente(self):
        CrearCliente(self.ventana)
    def actualizarCliente(self):
        ActualizarCliente(self.ventana)
    def actualizarServicios(self):
        ActualizarServicios(self.ventana)
    def removerCliente(self):
        BorrarCliente(self.ventana)
    def removerServicio(self):
        BorrarServicio(self.ventana)
    def consultarClientes(self):
        ConsultarCliente(self.ventana)
    def consultarServicios(self):
        ConsultarServicio(self.ventana)
    def ingresarServicio(self):
        CrearServicio(self.ventana)

    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Lavelopues S.A.S")
        self.ventana.geometry("800x600")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        
        self.ruta_imagen = os.path.join(self.ruta,"..","iconos","lavalo.png")
        self.imagen = Image.open(self.ruta_imagen)
        self.imagen=ImageTk.PhotoImage(self.imagen)

        self.lblImagen=tk.Label(self.ventana,image=self.imagen)
        self.lblImagen.pack()

        self.ruta_icono = os.path.join(self.ruta,"..","iconos","Jabon.ico")
        self.ventana.iconbitmap(self.ruta_icono)

        ip = "192.168.1.2"
        clientes_url = f"http://{ip}:8000/api/cliente/"
        servicios_url = f"http://{ip}:8000/api/servicios/"
        self.backup_controller = BackupController(clientes_url, servicios_url)
        
        self.menu=tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)
        menu_clientes=tk.Menu(self.menu)
        menu_clientes.config(bg="aquamarine3")
        self.menu.add_cascade(label="Gestionar Clientes",menu=menu_clientes)
        menu_clientes.add_command(label="Ingresar Clientes",command=lambda:self.ingresarCliente())
        menu_clientes.add_separator()
        menu_clientes.add_command(label="Remover Clientes",command=lambda:self.removerCliente())
        menu_clientes.add_separator()
        menu_clientes.add_command(label="Actualizar Clientes",command=lambda:self.actualizarCliente())
        menu_clientes.add_separator()
        menu_clientes.add_command(label="Consultar Clientes",command=lambda:self.consultarClientes())

        menu_servicios=tk.Menu(self.menu)
        menu_servicios.config(bg="aquamarine3")
        self.menu.add_cascade(label="Gestionar Servicios",menu=menu_servicios)
        menu_servicios.add_command(label="Ingresar Servicios",command=lambda:self.ingresarServicio())
        menu_servicios.add_separator()
        menu_servicios.add_command(label="Remover Servicios",command=lambda:self.removerServicio())
        menu_servicios.add_separator()
        menu_servicios.add_command(label="Actualizar Servicios",command=lambda:self.actualizarServicios())
        menu_servicios.add_separator()
        menu_servicios.add_command(label="Consultar Servicios",command=lambda:self.consultarServicios())

        self.ventana.mainloop()
