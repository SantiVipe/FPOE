import tkinter as tk
from tkinter.messagebox import askyesno,showerror
class Eliminar():
    def buscar(self):
        cedula = self.entry_cedula.get()
        persona = self.persona.buscar(cedula, warning=False)
        if  persona!=None:
            self.boton_eliminar.config(state="normal")
            self.entry_nombre.config(state="normal")
            self.entry_nombre.insert(0,persona[1])
            self.entry_nombre.config(state="disabled")
            self.entry_cedula.config(state="disabled")
        else:
            showerror("Error","El número de la cédula es incorrecta.")
            self.boton_eliminar.config(state="disabled")
            self.entry_nombre.config(state="disabled")
            self.entry_cedula.config(state="normal")
    def eliminar(self):
        cedula = self.entry_cedula.get()
        if cedula=="":
            showerror("Error","El campo de la cédula está vacía")
        
        elif cedula:
            self.persona.borrar(cedula)
            self.entry_nombre.config(state="normal")
            self.entry_nombre.delete(0,tk.END)
            self.entry_nombre.config(state="disabled")
            self.boton_eliminar.config(state="disabled")
            self.entry_cedula.config(state="normal")
            self.entry_cedula.delete(0,tk.END)
        else:
            showerror("Error", "Nombre inválido, corrija e intente nuevamente.")
        
    def salir(self):
        if askyesno("Confirmación","¿Desea salir de la aplicación?"):
            self.ventana.destroy()
    def __init__(self,ventana,persona):
        # Ventana
        self.ventana = tk.Toplevel(ventana)
        self.ventana.title("Eliminar Personas")
        self.ventana.geometry("1000x500")
        # Variables
        self.persona = persona
        # Labels
        self.label_titulo = tk.Label(self.ventana,text="Eliminar Persona",font=("Arial",12))
        self.label_titulo.place(relx=0.5,rely=0.05,anchor="center")
        
        self.label_cedula = tk.Label(self.ventana,text="Cédula:",font=("Arial",12))
        self.label_cedula.place(relx=0.1,rely=0.2,relheight=0.2,relwidth=0.1)

        self.label_nombre = tk.Label(self.ventana,text="Nombre:",font=("Arial",12))
        self.label_nombre.place(relx=0.1,rely=0.6,relheight=0.2,relwidth=0.1)

        self.entry_cedula = tk.Entry(self.ventana,font=("Arial",12))
        self.entry_cedula.place(relx=0.3,rely=0.2,relheight=0.2,relwidth=0.4)

        self.entry_nombre = tk.Entry(self.ventana,font=("Arial",12))
        self.entry_nombre.place(relx=0.3,rely=0.6,relheight=0.2,relwidth=0.4)
        self.entry_nombre.config(state="disabled")
        
        self.boton_buscar = tk.Button(self.ventana,text="BUSCAR",font=("Arial",12),command=lambda:self.buscar())
        self.boton_buscar.place(relx=0.25,rely=0.85,relheight=0.1,relwidth=0.1)

        self.boton_eliminar = tk.Button(self.ventana,text="ELIMINAR",font=("Arial",12),command=lambda:self.eliminar())
        self.boton_eliminar.place(relx=0.45,rely=0.85,relheight=0.1,relwidth=0.1)
        self.boton_eliminar.config(state="disabled")

        self.boton_salir = tk.Button(self.ventana,text="SALIR",font=("Arial",12),command=lambda:self.salir())
        self.boton_salir.place(relx=0.65,rely=0.85,relheight=0.1,relwidth=0.1)

        self.ventana.mainloop()