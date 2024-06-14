import tkinter as tk
class Cliente():
    
    def __init__(self,ventanaPrincipal):
        self.ventanaPrincipal=ventanaPrincipal
        self.nombre=tk.StringVar(ventanaPrincipal)
        self.apellido=tk.StringVar(ventanaPrincipal)
        self.cedula=tk.StringVar(ventanaPrincipal)
        self.telefono=tk.StringVar(ventanaPrincipal)
        self.email=tk.StringVar(ventanaPrincipal)