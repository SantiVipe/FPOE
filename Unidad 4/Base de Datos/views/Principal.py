import tkinter as tk 
from controladores.Persona import Persona
from views.Guardar import Guardar
from views.Consultar import Consultar
from views.Actualizar import Actualizar
from views.Eliminar import Eliminar
class Principal():
    def guardar(self):
        guardar = Guardar(self.ventana,self.persona)
    def consultar(self):
        consultar = Consultar(self.ventana,self.persona)
    def actualizar(self):
        actualizar = Actualizar(self.ventana,self.persona)
    def eliminar(self):
        eliminar = Eliminar(self.ventana,self.persona)
    def __init__(self):
        # Ventana
        self.ventana = tk.Tk()
        self.ventana.title("Menú Principal")
        self.ventana.geometry("1000x500")
        # Variables
        self.persona = Persona("Santi","1115358303")
        # Labels
        self.label_titulo = tk.Label(self.ventana,text="Gestionar Base de Datos",font=("Arial",12))
        self.label_titulo.place(relx=0.4,rely=0.05,relwidth=0.2)
        #Botones
        self.boton_guardar = tk.Button(self.ventana,text="GUARDAR",font=("Arial",12),command=lambda:self.guardar())
        self.boton_guardar.place(relx=0.2,rely=0.2,relheight=0.2,relwidth=0.2)

        self.boton_actualizar = tk.Button(self.ventana,text="ACTUALIZAR",font=("Arial",12),command=lambda:self.actualizar())
        self.boton_actualizar.place(relx=0.6,rely=0.2,relheight=0.2,relwidth=0.2)

        self.boton_eliminar = tk.Button(self.ventana,text="ELIMINAR",font=("Arial",12),command=lambda:self.eliminar())
        self.boton_eliminar.place(relx=0.2,rely=0.6,relheight=0.2,relwidth=0.2)
        
        self.boton_consultar = tk.Button(self.ventana,text="CONSULTAR",font=("Arial",12),command=lambda:self.consultar())
        self.boton_consultar.place(relx=0.6,rely=0.6,relheight=0.2,relwidth=0.2)

        self.ventana.mainloop()