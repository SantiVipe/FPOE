import tkinter as tk
from tkinter.messagebox import askyesno,showerror
class Guardar():
    def salir(self):
        if askyesno("Salir de la aplicación","¿Desea salir de la aplicación?"):
            self.ventana.destroy()
    def buscar(self):
        cedula = self.entry_cedula.get()
        if not self.persona.buscar(cedula, warning=False):
            self.boton_guardar.config(state="normal")
            self.entry_nombre.config(state="normal")
            self.entry_cedula.config(state="disabled")
        else:
            showerror("Error","Ya hay una persona con ese número de cédula.")
            self.boton_guardar.config(state="disabled")
            self.entry_nombre.config(state="disabled")
            self.entry_cedula.config(state="normal")
    def guardar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        if cedula=="":
            showerror("Error","El campo de la cédula está vacía")
        elif nombre:
            self.persona.guardar(cedula, nombre)
            self.entry_nombre.delete(0,tk.END)
            self.boton_guardar.config(state="disabled")
            self.entry_nombre.config(state="disabled")
            self.entry_cedula.config(state="normal")
            self.entry_cedula.delete(0,tk.END)
        else:
            showerror("Error", "Nombre inválido, corrija e intente nuevamente.")
    def __init__(self,ventana,persona):
        # Ventana
        self.ventana = tk.Toplevel(ventana)
        self.ventana.title("Guardar Persona")
        self.ventana.geometry("1000x500")
        # Variables
        self.persona = persona
        # Labels
        self.label_titulo = tk.Label(self.ventana,text="Guardar Persona",font=("Arial",12))
        self.label_titulo.place(relx=0.5,rely=0.1,anchor="center")

        self.label_cedula = tk.Label(self.ventana,text="Cédula:",font=("Arial",12))
        self.label_cedula.place(relx=0.2,rely=0.2,relheight=0.2,relwidth=0.2)
        
        self.label_nombre = tk.Label(self.ventana,text="Nombre:",font=("Arial",12))
        self.label_nombre.place(relx=0.2,rely=0.6,relheight=0.2,relwidth=0.2)
        # Entrys
        self.entry_cedula = tk.Entry(self.ventana,font=("Arial",12))
        self.entry_cedula.place(relx=0.5,rely=0.2,relheight=0.2,relwidth=0.3)

        self.entry_nombre = tk.Entry(self.ventana,font=("Arial",12))
        self.entry_nombre.place(relx=0.5,rely=0.6,relheight=0.2,relwidth=0.3)
        self.entry_nombre.config(state="disabled")
        # Buttons
        self.boton_buscar = tk.Button(self.ventana,text="BUSCAR",font=("Arial",12),command=lambda:self.buscar())
        self.boton_buscar.place(relx=0.1,rely=0.85,relheight=0.1,relwidth=0.2)

        self.boton_guardar = tk.Button(self.ventana,text="GUARDAR",font=("Arial",12),command=lambda:self.guardar())
        self.boton_guardar.place(relx=0.4,rely=0.85,relheight=0.1,relwidth=0.2)
        self.boton_guardar.config(state="disabled")

        self.boton_salir = tk.Button(self.ventana,text="SALIR",font=("Arial",12),command=lambda:self.salir())
        self.boton_salir.place(relx=0.7,rely=0.85,relheight=0.1,relwidth=0.2)

        self.ventana.mainloop()