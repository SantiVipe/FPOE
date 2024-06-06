import tkinter as tk
class Teclado():
    
    def __init__(self,ventanaPrincipal):
        self.ventanaPrincipal=ventanaPrincipal
        self.teclado=tk.StringVar(ventanaPrincipal)
        self.switch=tk.StringVar(ventanaPrincipal)
        self.keycaps=tk.StringVar(ventanaPrincipal)
        self.formato=tk.StringVar(ventanaPrincipal)
        self.conectividad=tk.StringVar(ventanaPrincipal)