import os
import tkinter as tk
from tkinter import messagebox,ttk
from controller.ControllerServicio import ControllerServicio
from models.Servicio import Servicio

class BorrarServicio():

    def borrar(self):
        cedula = self.entryCedula.get()
        if not cedula:
            messagebox.showerror("Error", "Por favor, ingrese una cédula.")
            return
        
        servicios_cliente = self.controlador.consultar_servicios_por_cedula(cedula)
        if not servicios_cliente:
            messagebox.showerror("Error", "No se encontraron servicios asociados a esta cédula.")
            return

        servicios_dict = {servicio['nombre_servicio']: servicio['id'] for servicio in servicios_cliente}
        self.combo_servicios.config(state="normal")
        self.combo_servicios['values'] = list(servicios_dict.keys())

        servicio_seleccionado = self.combo_servicios.get()
        if not servicio_seleccionado:
            messagebox.showerror("Error", "Por favor, seleccione un servicio.")
            return
        
        servicio_id = servicios_dict[servicio_seleccionado]

        if messagebox.askyesno("Confirmar", f"¿Está seguro de que desea eliminar el servicio '{servicio_seleccionado}'?"):
            servicio_eliminado = self.controlador.eliminar_servicio(servicio_id)
            if servicio_eliminado:
                messagebox.showinfo("Éxito", f"El servicio '{servicio_seleccionado}' ha sido eliminado correctamente.")
                self.ventana.destroy()
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el servicio '{servicio_seleccionado}'.")

    def __init__(self, ventanaPrincipal):
        self.ventana= tk.Toplevel(ventanaPrincipal)
        self.ventana.geometry("500x500")
        self.ventana.focus_set()
        self.ventana.title("Borrar Servicio")
        self.ventana.config(bg="#FFCCCC")
        
        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","eliminar_cliente.ico")
        self.ventana.iconbitmap(self.ruta_icono)

        self.controlador = ControllerServicio(self.ventana)
        self.servicio = Servicio(self.ventana)

        self.labelTitulo = tk.Label(self.ventana,text="Borrar Servicio",font=("Arial",12), bg="#FFCCCC")
        self.labelTitulo.place(relx=0.5,rely=0.05,anchor="center")

        self.labelCedula = tk.Label(self.ventana,text="Cedula:",font=("Arial",12), bg="#CC3333")
        self.labelCedula.place(relx=0.1,rely=0.35,relheight=0.1,relwidth=0.2)

        self.labelCombo= tk.Label(self.ventana,font=("Arial",12),text="Servicios:")
        self.labelCombo.place(relx=0.1,rely=0.55,relheight=0.1,relwidth=0.2)

        self.entryCedula = tk.Entry(self.ventana,font=("Arial",12), bg="#FFCCCC")
        self.entryCedula.place(relx= 0.4,rely=0.35,relheight=0.1,relwidth=0.3)

        self.combo_servicios = ttk.Combobox(self.ventana,background="lightblue")
        self.combo_servicios.place(relx=0.4,rely=0.55,relheight=0.1,relwidth=0.3) 
        self.combo_servicios.config(state="disabled") 

        self.boton_borrar = tk.Button(self.ventana,text="Borrar",font=("Arial",12),command=lambda:self.borrar(),bg="#CC3333")
        self.boton_borrar.place(relx=0.35,rely=0.8,relheight=0.1,relwidth=0.1)

        self.boton_salir = tk.Button(self.ventana,text="Salir",font=("Arial",12),command=lambda:self.salir(),bg="#CC3333")
        self.boton_salir.place(relx=0.55,rely=0.8,relheight=0.1,relwidth=0.1)