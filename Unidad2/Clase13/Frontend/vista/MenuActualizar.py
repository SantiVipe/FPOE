import tkinter as tk
from tkinter.messagebox import askyesno, showinfo, showerror
import requests
class MenuActualizar():
    def salir(self):
        if askyesno("Salir de la aplicación", '¿Desea salir de la aplicación?'):
            self.ventana.destroy()

    def evento_presionar_tecla(self, evento):
        texto_validar_teclado = ""
        texto_validar_id = ""
        if self.entry_id.get()=="":
            texto_validar_id="No puede haber ningún campo vacío"
            self.boton_buscar.config(state=tk.DISABLED)
        elif self.validacion.validarNumeros(self.entry_id.get()):
            texto_validar_id=""
            self.boton_buscar.config(state=tk.NORMAL)
            if self.modelo.teclado.get() == "" or self.modelo.switch.get() == "Seleccione" or self.modelo.keycaps.get() == "Seleccione" or self.modelo.formato.get() == "Seleccione" or self.modelo.conectividad.get() == "Seleccione":
                texto_validar_teclado = "No puede haber ningún campo vacío"
                self.boton_actualizar.config(state=tk.DISABLED)

            elif self.validacion.validarLetras(self.modelo.teclado):
                texto_validar_teclado = ""
                self.boton_actualizar.config(state=tk.NORMAL)
            else:
                if not self.validacion.validarLetras(self.modelo.teclado):
                    texto_validar_teclado = "Sólo se permiten letras en el campo"
                self.boton_actualizar.config(state=tk.DISABLED)
        else:
            if not self.validacion.validarNumeros(self.entry_id.get()):
                texto_validar_id = "Sólo se permiten números en el campo"
            self.boton_buscar.config(state=tk.DISABLED)
        self.labelValidacionTeclado.config(text=texto_validar_teclado)
        self.labelValidacionID.config(text=texto_validar_id)

    def buscar(self):
        self.entry_id.config(state="disabled")
        self.entry_teclado.config(state="normal")
        self.optionmenu_switch.config(state="normal")
        self.optionmenu_keycaps.config(state="normal")
        self.optionmenu_formato.config(state="normal")
        self.optionmenu_conectividad.config(state="normal")
        id = self.entry_id.get()
        datos = self.comunicacion.buscarTeclado(id)
        if datos:
            self.entry_teclado.delete(0,tk.END)
            self.entry_teclado.insert(0,datos['teclado'])
            self.modelo.switch.set(datos['switch'])
            self.modelo.keycaps.set(datos['keycaps'])
            self.modelo.formato.set(datos['formato'])
            self.modelo.conectividad.set(datos['conectividad'])
            self.boton_actualizar.config(state="normal")
        else:
            showerror("Error", "Teclado no encontrado.")

    def actualizar(self):
        id = self.entry_id.get()
        teclado = self.entry_teclado.get()
        switch = self.modelo.switch.get()
        keycaps = self.modelo.keycaps.get()
        formato = self.modelo.formato.get()
        conectividad = self.modelo.conectividad.get()

        print(f"ID: {id}")
        print(f"Teclado: {teclado}")
        print(f"Switch: {switch}")
        print(f"Keycaps: {keycaps}")
        print(f"Formato: {formato}")
        print(f"Conectividad: {conectividad}")

        # Llamada al método actualizar de la clase Comunicacion
        try:
            resultado = self.comunicacion.actualizar(id, teclado, switch, keycaps, formato, conectividad)
            if resultado:
                showinfo("Éxito", "Teclado actualizado exitosamente.")
            else:
                showerror("Error", "Error al actualizar el teclado.")
        except requests.exceptions.HTTPError as err:
            showerror("Error", f"Error HTTP: {err}")
        except Exception as e:
            showerror("Error", f"Error inesperado: {e}")

            

    def limpiar(self):
        self.entry_id.delete(0, tk.END)
        self.entry_teclado.delete(0, tk.END)
        self.modelo.switch.set("Seleccione")
        self.modelo.keycaps.set("Seleccione")
        self.modelo.formato.set("Seleccione")
        self.modelo.conectividad.set("Seleccione")
        self.boton_actualizar.config(state=tk.DISABLED)
        self.labelValidacionTeclado.config(text="No puede estar el campo vacío")
        self.labelValidacionID.config(text="No puede estar el campo vacío")

    def __init__(self, menu, modelo, validacion, comunicacion):
        # Ventana
        self.ventana = tk.Toplevel(menu)
        self.ventana.geometry("500x500")
        self.ventana.title("Actualizar Teclado")
        self.ventana.config(bg="aquamarine1")

        # Variables
        self.modelo = modelo
        self.validacion = validacion
        self.comunicacion = comunicacion

        # Labels
        self.label_titulo = tk.Label(self.ventana, text="Actualizar Teclado", bg="aquamarine1")
        self.label_titulo.place(relx=0.4, rely=0, relheight=0.1, relwidth=0.2)

        self.label_id = tk.Label(self.ventana, text="ID:", bg="aquamarine1")
        self.label_id.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.1)

        self.label_teclado = tk.Label(self.ventana, text="Teclado:", bg="aquamarine1")
        self.label_teclado.place(relx=0.1, rely=0.25, relheight=0.1, relwidth=0.1)

        self.label_switch = tk.Label(self.ventana, text="Switch:", bg="aquamarine1")
        self.label_switch.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.1)

        self.label_keycaps = tk.Label(self.ventana, text="Keycaps:", bg="aquamarine1")
        self.label_keycaps.place(relx=0.1, rely=0.55, relheight=0.1, relwidth=0.1)

        self.label_formato = tk.Label(self.ventana, text="Formato:", bg="aquamarine1")
        self.label_formato.place(relx=0.1, rely=0.7, relheight=0.1, relwidth=0.1)

        self.label_conectividad = tk.Label(self.ventana, text="Conectividad:", bg="aquamarine1")
        self.label_conectividad.place(relx=0.1, rely=0.85, relheight=0.1, relwidth=0.1)

        self.labelValidacionID = tk.Label(self.ventana, text="", bg="aquamarine1",fg="red")
        self.labelValidacionID.place(relx=0.3, rely=0.2, relheight=0.05, relwidth=0.45)

        self.labelValidacionTeclado = tk.Label(self.ventana, text="", bg="aquamarine1",fg="red")
        self.labelValidacionTeclado.place(relx=0.3, rely=0.35, relheight=0.05, relwidth=0.45)
        self.labelValidacionTeclado.config(state="disabled")

        # Entrys
        self.entry_id = tk.Entry(self.ventana, bg="aquamarine3")
        self.entry_id.bind("<KeyRelease>", self.evento_presionar_tecla)
        self.entry_id.place(relx=0.3, rely=0.1, relheight=0.1, relwidth=0.45)

        self.entry_teclado = tk.Entry(self.ventana, bg="aquamarine3", textvariable=self.modelo.teclado)
        self.entry_teclado.bind("<KeyRelease>", self.evento_presionar_tecla)
        self.entry_teclado.place(relx=0.3, rely=0.25, relheight=0.1, relwidth=0.45)
        self.entry_teclado.config(state="disabled")

        self.modelo.switch.set("Seleccione")
        self.optionmenu_switch = tk.OptionMenu(self.ventana, self.modelo.switch, "Cherry MX Red", "Cherry MX Brown", "Cherry MX Blue", command=self.evento_presionar_tecla)
        self.optionmenu_switch.config(bg="aquamarine3")
        self.optionmenu_switch.place(relx=0.3, rely=0.4, relheight=0.1, relwidth=0.45)
        self.optionmenu_switch.config(state="disabled")

        self.modelo.keycaps.set("Seleccione")
        self.optionmenu_keycaps = tk.OptionMenu(self.ventana, self.modelo.keycaps, "ABS", "PBT", "POM", command=self.evento_presionar_tecla)
        self.optionmenu_keycaps.config(bg="aquamarine3")
        self.optionmenu_keycaps.place(relx=0.3, rely=0.55, relheight=0.1, relwidth=0.45)
        self.optionmenu_keycaps.config(state="disabled")

        self.modelo.formato.set("Seleccione")
        self.optionmenu_formato = tk.OptionMenu(self.ventana, self.modelo.formato, "Full-size", "Tenkeyless (TKL)", "75%", "65%", "60%", "40%", "Ergonómico", "Portátil", command=self.evento_presionar_tecla)
        self.optionmenu_formato.config(bg="aquamarine3")
        self.optionmenu_formato.place(relx=0.3, rely=0.7, relheight=0.1, relwidth=0.45)
        self.optionmenu_formato.config(state="disabled")

        self.modelo.conectividad.set("Seleccione")
        self.optionmenu_conectividad = tk.OptionMenu(self.ventana, self.modelo.conectividad, "Cableado", "Bluetooth", "2.4G", command=self.evento_presionar_tecla)
        self.optionmenu_conectividad.config(bg="aquamarine3")
        self.optionmenu_conectividad.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.45)
        self.optionmenu_conectividad.config(state="disabled")

        # Buttons
        self.boton_buscar = tk.Button(self.ventana, text="Buscar", bg="aquamarine3", command=self.buscar)
        self.boton_buscar.config(state=tk.DISABLED)
        self.boton_buscar.place(relx=0.8, rely=0.1, relheight=0.1, relwidth=0.1)

        self.boton_actualizar = tk.Button(self.ventana, text="Actualizar", bg="aquamarine3", command=self.actualizar)
        self.boton_actualizar.config(state=tk.DISABLED)
        self.boton_actualizar.place(relx=0.25, rely=0.8, relheight=0.1, relwidth=0.1)

        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar", bg="aquamarine3", command=self.limpiar)
        self.boton_limpiar.place(relx=0.45, rely=0.8, relheight=0.1, relwidth=0.1)

        self.boton_salir = tk.Button(self.ventana, text="Salir", bg="aquamarine3", command=self.salir)
        self.boton_salir.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.1)

        self.ventana.mainloop()