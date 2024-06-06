import tkinter as tk
from controladores.Validaciones import Validaciones
from controladores.Comunicacion import Comunicacion
from modelos.Teclado import Teclado
from .MenuGuardar import MenuGuardar
from .MenuConsultarID import MenuConsultarID
from .ConsultarTeclados import ConsultarTeclados
from .MenuActualizar import MenuActualizar
class MenuPrincipal():
    # Funciones
    def guardar(self):
        guardar = MenuGuardar(self.ventana_principal,self.teclado,self.validacion,self.comunicacion)
    def consultarID(self):
        consultar_id = MenuConsultarID(self.ventana_principal,self.teclado,self.validacion,self.comunicacion)
    def consultarTeclados(self):
        consultar_teclados = ConsultarTeclados(self.ventana_principal,self.comunicacion)
    def actualizar(self):
        actualizar=MenuActualizar(self.ventana_principal,self.teclado,self.validacion,self.comunicacion)
    # Método Constructor
    def __init__(self):
        # Ventana
        self.ventana_principal = tk.Tk()
        self.ventana_principal.geometry("500x500")
        self.ventana_principal.title("Main")
        # Modelos
        self.teclado = Teclado(self.ventana_principal)
        # Controladores
        self.validacion = Validaciones()
        self.comunicacion = Comunicacion(self.ventana_principal)
        # Botones
        self.boton_guardar=tk.Button(self.ventana_principal,text="GUARDAR",command=lambda:self.guardar())
        self.boton_guardar.pack()
        self.boton_consultarID = tk.Button(self.ventana_principal,text="CONSULTAR ID",command=lambda:self.consultarID())
        self.boton_consultarID.pack()
        self.boton_consultarTeclados = tk.Button(self.ventana_principal,text="CONSULTAR TECLADOS",command=lambda:self.consultarTeclados())
        self.boton_consultarTeclados.pack()
        self.boton_actualizar = tk.Button(self.ventana_principal,text="ACTUALIZAR",command=lambda:self.actualizar())
        self.boton_actualizar.pack()

        self.ventana_principal.mainloop()