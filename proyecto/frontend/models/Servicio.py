import tkinter as tk
class Servicio():
    
    def __init__(self,ventanaPrincipal):
        self.ventanaPrincipal=ventanaPrincipal
        self.nombre_servicio=tk.StringVar(ventanaPrincipal)
        self.cedula=tk.StringVar(ventanaPrincipal)
        self.descripcion=tk.StringVar(ventanaPrincipal)
        self.valor=tk.StringVar(ventanaPrincipal)