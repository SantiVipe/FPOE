import os
import tkinter as tk
from tkinter import messagebox
from controller.ControllerCliente import ClienteController
from controller.ControllerServicio import ControllerServicio
from models.Servicio import Servicio
class CrearServicio():
    def guardar(self):
        cliente_id = self.comunicacionCliente.comprobar_cedula(self.entry_cedula.get())
        nombre = self.servicio.nombre_servicio.get()
        descripcion = self.servicio.descripcion.get()
        valor = self.servicio.valor.get()

        if not self.entry_cedula.get() or not nombre or not descripcion or not valor:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        try:
            valor = float(valor.replace("$", "").replace(".", ""))
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser un número.")
            return
        if cliente_id:
            servicio_data = {
                "nombre_servicio": nombre,
                "cedula_cliente": cliente_id,
                "descripcion": descripcion,
                "valor": valor
            }

            # Guardar el servicio
            guardado_exitoso = self.comunicacionServicio.guardar_servicio(servicio_data)
            if guardado_exitoso:
                messagebox.showinfo("Éxito", "Servicio guardado correctamente.")
                self.ventana.destroy()
    def buscar(self):
        cedula = self.servicio.cedula.get()
        cliente = self.comunicacionCliente.consultar_cliente_cedula(cedula)
        if cliente:
            self.entry_cedula.config(state="disabled")
            self.optionmenu_nombre.config(state="normal")
            self.boton_guardar.config(state="normal")
        else:
            messagebox.showerror("Error", "El cliente con la cédula proporcionada no existe.")
            return
    def salir(self):
        if messagebox.askyesno("Confirmación","¿Desea salir de la aplicación?"):
            self.ventana.destroy()
    def actualizar_campos(self, seleccion):
        if seleccion == "Básico":
            self.servicio.descripcion.set("Incluye: - Lavado Externo e Interior")
            self.servicio.valor.set("15.000$")
        elif seleccion == "Estandar":
            self.servicio.descripcion.set("Incluye: - Lavado Externo- Interior y Aspirada - Perfumado ")
            self.servicio.valor.set("30.000$")
        elif seleccion == "Premium":
            self.servicio.descripcion.set("Incluye: - Lavado Externo Completo - Interior y Aspirada - Perfumado")
            self.servicio.valor.set("60.000$")
        elif seleccion == "VIP":
            self.servicio.descripcion.set("Incluye:- Lavado Externo Completo- Interior Detallado y Aspirada- Perfumería Premium")
            self.servicio.valor.set("100.000$")
        else:
            self.servicio.descripcion.set("")
            self.servicio.valor.set("")
    def __init__(self,ventanaPrincipal):
        self.ventana = tk.Toplevel(ventanaPrincipal)
        self.ventana.geometry("500x500")
        self.ventana.title("Crear Servicio")
        self.ventana.config(bg="#98FB98")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","crear_servicio.ico")
        self.ventana.iconbitmap(self.ruta_icono)

        self.servicio = Servicio(self.ventana)

        self.comunicacionCliente = ClienteController(self.ventana)
        self.comunicacionServicio = ControllerServicio(self.ventana)

        self.label_titulo = tk.Label(self.ventana,text="Registrar Servicio",font=("Arial",12), bg="#98FB98")
        self.label_titulo.place(relx=0.5,rely=0.05,anchor="center")

        self.label_cedula = tk.Label(self.ventana,text="Cédula:",font=("Arial",12), bg="#9ACD32")
        self.label_cedula.place(relx=0.1,rely=0.35,relheight=0.1,relwidth=0.2)

        self.label_nombre = tk.Label(self.ventana,text="Servicio",font=("Arial",12), bg="#9ACD32")
        self.label_nombre.place(relx=0.1,rely=0.55,relheight=0.1,relwidth=0.2)

        self.entry_cedula = tk.Entry(self.ventana,textvariable=self.servicio.cedula,font=("Arial",12), bg="#E5F3E2")
        self.entry_cedula.place(relx=0.4,rely=0.35,relheight=0.1,relwidth=0.3)

        self.servicio.nombre_servicio.set("Seleccione")
        self.optionmenu_nombre = tk.OptionMenu(self.ventana,self.servicio.nombre_servicio,"Básico","Estandar","Premium","VIP",command=self.actualizar_campos)
        self.optionmenu_nombre.place(relx=0.4,rely=0.55,relheight=0.1,relwidth=0.3)
        self.optionmenu_nombre.config(bg="lightblue",font=("Arial",12))
        self.optionmenu_nombre.config(state="disabled")

        self.boton_buscar = tk.Button(self.ventana,text="Buscar",font=("Arial",12),bg="#9ACD32",command=lambda:self.buscar())
        self.boton_buscar.place(relx=0.3,rely=0.8,relheight=0.1,relwidth=0.1)

        self.boton_guardar = tk.Button(self.ventana,text="Guardar",font=("Arial",12),bg="#9ACD32",command=lambda:self.guardar())
        self.boton_guardar.place(relx=0.45,rely=0.8,relheight=0.1,relwidth=0.1)
        self.boton_guardar.config(state="disabled")
        
        self.boton_salir = tk.Button(self.ventana,text="Salir",font=("Arial",12),bg="#9ACD32",command=lambda:self.salir())
        self.boton_salir.place(relx=0.6,rely=0.8,relheight=0.1,relwidth=0.1)

