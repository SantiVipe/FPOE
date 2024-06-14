import os
import tkinter as tk
from tkinter.messagebox import showerror, showinfo, askyesno
from tkinter import ttk
from controller.ControllerServicio import ControllerServicio
from controller.ControllerCliente import ClienteController
from models.Servicio import Servicio

class ActualizarServicios():

    def actualizar(self):
        servicio_seleccionado = self.combo_servicios.get()
        servicio_id = self.servicios_dict.get(servicio_seleccionado)

        if not servicio_id:
            showerror("Error", "No se ha seleccionado un servicio válido.")
            return
        
        cliente_id = self.controlador_cliente.comprobar_cedula(self.entryCedula.get())
        nombre = self.nombre_opcion.get()
        descripcion = self.servicio.descripcion.get()
        valor = self.servicio.valor.get()

        if not self.entryCedula.get() or not nombre or not descripcion or not valor:
            showerror("Error", "Todos los campos son obligatorios.")
            return
        
        try:
            valor = float(valor.replace("$", "").replace(".", ""))
        except ValueError:
            showerror("Error", "El valor debe ser un número.")
            return
        
        if cliente_id:
            servicio_data = {
                "nombre_servicio": nombre,
                "cedula_cliente": cliente_id,
                "descripcion": descripcion,
                "valor": valor
            }
            actualizacion_exitosa = self.controlador.actualizar(servicio_id,servicio_data)
            if actualizacion_exitosa:
                showinfo("Éxito", "Servicio actualizado correctamente.")
                self.ventana.destroy()

    def buscar(self):
        cedula = str(self.entryCedula.get())
        if cedula:
            cliente = self.controlador_cliente.comprobar_cedula(cedula)
            if not cliente:
                showerror("Error", "El cliente con la cédula proporcionada no existe.")
                return

            # Consultar los servicios asociados a la cédula
            servicios_cliente = self.controlador.consultar_servicios_por_cedula(cedula)
            
            if not servicios_cliente:
                showerror("Error", "No se encontraron servicios asociados a esta cédula.")
                return

            self.servicios_dict = {servicio['nombre_servicio']: servicio['id'] for servicio in servicios_cliente}
            self.combo_servicios.config(state="normal")
            self.combo_servicios['values'] = list(self.servicios_dict.keys())

            servicio_seleccionado = self.combo_servicios.get()
            if not servicio_seleccionado:
                showerror("Error", "Por favor, seleccione un servicio.")
                return
            servicio_id = self.servicios_dict[servicio_seleccionado]
            servicio = self.controlador.consultar_servicio_por_id(servicio_id)
            if servicio:
                self.optionmenu_nombre.config(state="normal")
                self.nombre_opcion.set(servicio["nombre_servicio"])
                self.servicio.descripcion.set(servicio["descripcion"])
                self.servicio.valor.set(servicio["valor"])
                self.entryCedula.config(state="disabled")
                self.boton_buscar.config(state="normal")
                self.boton_actualizar.config(state="normal")
                self.optionmenu_nombre.config(state="normal")
        else:
            showerror("Error", "Por favor, ingrese la cédula del cliente.")

    def salir(self):
        if askyesno("Confirmación", "¿Desea salir de la aplicación?"):
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

    def __init__(self, ventanaPrincipal):
        self.ventana= tk.Toplevel(ventanaPrincipal)
        self.ventana.geometry=("500x500")
        self.ventana.focus_set()
        self.ventana.title("Actualizar Servicio")
        self.ventana.config(bg="#2C3E50")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","actualizar_servicio.ico")
        self.ventana.iconbitmap(self.ruta_icono)
        
        self.servicios_dict= {}

        self.servicio= Servicio(self.ventana)
        self.controlador= ControllerServicio(self.ventana)
        self.controlador_cliente = ClienteController(self.ventana)

        self.labelTitulo = tk.Label(self.ventana, text="Actualizar Servicio", font=("Arial", 12), bg="#2C3E50")
        self.labelTitulo.place(relx=0.5, rely=0.05, anchor="center")

        self.labelCedula= tk.Label(self.ventana, text="Cedula:", bg="lightblue")
        self.labelCedula.place(relx=0.1, rely=0.25, relheight=0.1, relwidth=0.2)
        self.entryCedula= tk.Entry(self.ventana,font= ("Arial",12), textvariable= self.servicio.cedula)
        self.entryCedula.place(relx=0.4, rely=0.25, relheight=0.1, relwidth=0.3)

        self.labelServicios = tk.Label(self.ventana,text="Servicios:", bg="lightblue")
        self.labelServicios.place(relx=0.1,rely=0.45,relheight=0.1,relwidth=0.2)
        self.combo_servicios = ttk.Combobox(self.ventana,background="lightblue")
        self.combo_servicios.place(relx=0.4,rely=0.45,relheight=0.1,relwidth=0.3) 
        self.combo_servicios.config(state="disabled") 

        self.labelOption = tk.Label(self.ventana,text="Seleccione:",font=("Arial",12), bg="lightblue")
        self.labelOption.place(relx=0.1,rely=0.65,relheight=0.1,relwidth=0.2)
        self.nombre_opcion = tk.StringVar(self.ventana)
        self.optionmenu_nombre = tk.OptionMenu(self.ventana,self.nombre_opcion,"Básico","Estandar","Premium","VIP",command=self.actualizar_campos)
        self.optionmenu_nombre.place(relx=0.4,rely=0.65,relheight=0.1,relwidth=0.3)
        self.optionmenu_nombre.config(bg="lightblue",font=("Arial",12))
        self.optionmenu_nombre.config(state="disabled")

        self.boton_buscar = tk.Button(self.ventana,text="Buscar",font=("Arial",12),command=lambda:self.buscar(), relief="ridge", bg="lightblue")
        self.boton_buscar.place(relx=0.8,rely=0.25,relheight=0.1,relwidth=0.1)
        
        self.boton_actualizar = tk.Button(self.ventana, text="Actualizar", font=("Arial", 12), command=lambda:self.actualizar(), relief="ridge", bg="lightblue")
        self.boton_actualizar.place(relx=0.8, rely=0.45, relheight=0.1, relwidth=0.1)
        self.boton_actualizar.config(state="disabled")
        
        self.boton_salir = tk.Button(self.ventana, text="Salir", font=("Arial", 12), command=lambda:self.salir(), relief="ridge", bg="lightblue")
        self.boton_salir.place(relx=0.8, rely=0.65, relheight=0.1, relwidth=0.1)
        