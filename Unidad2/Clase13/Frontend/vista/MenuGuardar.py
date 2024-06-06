import tkinter as tk
from tkinter.messagebox import askyesno,showinfo,showerror
class MenuGuardar():
    def salir(self):
        if askyesno("Salir de la aplicación", '¿Desea salir de la aplicación?'):
            self.ventana.destroy()

    def evento_presionar_tecla(self, evento):
        if self.modelo.teclado.get()=="" or self.modelo.switch.get()=="Seleccione" or self.modelo.keycaps.get()=="Seleccione" or self.modelo.formato.get()=="Seleccione" or self.modelo.conectividad.get()=="Seleccione":
            texto_validar_teclado = "No puede haber ningún campo vacío"
            self.boton_guardar.config(state=tk.DISABLED)
        elif self.validacion.validarLetras(self.modelo.teclado):
            texto_validar_teclado = ""
            self.boton_guardar.config(state=tk.NORMAL)
        else:
            texto_validar_teclado = "Sólo se permiten letras en el campo"
        self.labelValidacionTeclado.config(text=texto_validar_teclado, fg="red")
    def guardar(self):
        teclado = self.entry_teclado.get()
        switch = self.modelo.switch.get()
        keycaps = self.modelo.keycaps.get()
        formato = self.modelo.formato.get()
        conectividad = self.modelo.conectividad.get()

        # Llamada al método guardar de la clase Comunicacion
        resultado = self.comunicacion.guardar(teclado, switch, keycaps, formato, conectividad)
        if resultado:
            showinfo("Éxito", "Teclado guardado exitosamente.")
        else:
            showerror("Error", "Error al guardar el teclado.")
    def limpiar(self):
        self.modelo.teclado.set("")
        self.modelo.switch.set("Seleccione")
        self.modelo.keycaps.set("Seleccione")
        self.modelo.formato.set("Seleccione")
        self.modelo.conectividad.set("Seleccione")
        self.boton_guardar.config(state=tk.DISABLED)
        self.labelValidacionTeclado.config(text="No puede estar el campo vacío", fg="red")
    def __init__(self,menu,modelo,validacion,comunicacion):
        # Ventana
        self.ventana = tk.Toplevel(menu)
        self.ventana.geometry("500x500")
        self.ventana.title("Guardar Teclado")
        self.ventana.config(bg="aquamarine1")

        # Variables
        self.modelo = modelo
        self.validacion = validacion
        self.comunicacion = comunicacion

        # Labels
        self.label_titulo = tk.Label(self.ventana, text="Personalice su Teclado", bg="aquamarine1")
        self.label_titulo.place(relx=0.35, rely=0.05, relheight=0.1, relwidth=0.3)

        self.label_teclado = tk.Label(self.ventana, text="Teclado:", bg="aquamarine1")
        self.label_teclado.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.1)

        self.label_switch = tk.Label(self.ventana, text="Switch:", bg="aquamarine1")
        self.label_switch.place(relx=0.1, rely=0.33, relheight=0.1, relwidth=0.1)

        self.label_keycaps = tk.Label(self.ventana, text="Keycaps:", bg="aquamarine1")
        self.label_keycaps.place(relx=0.1, rely=0.45, relheight=0.1, relwidth=0.1)

        self.label_formato = tk.Label(self.ventana, text="Formato:", bg="aquamarine1")
        self.label_formato.place(relx=0.1, rely=0.57, relheight=0.1, relwidth=0.1)

        self.label_conectividad = tk.Label(self.ventana, text="Conectividad:", bg="aquamarine1")
        self.label_conectividad.place(relx=0.07, rely=0.7, relheight=0.1, relwidth=0.17)

        self.labelValidacionTeclado = tk.Label(self.ventana, text="", bg="aquamarine1")
        self.labelValidacionTeclado.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.15)
        self.labelValidacionTeclado.config(text="No puede estar el campo vacío",fg="red")

        # Entrys
        self.entry_teclado = tk.Entry(self.ventana, bg="aquamarine3", textvariable=self.modelo.teclado)
        self.entry_teclado.bind("<KeyRelease>", self.evento_presionar_tecla)
        self.entry_teclado.place(relx=0.3, rely=0.2, relheight=0.1, relwidth=0.45)

        self.modelo.switch.set("Seleccione")
        self.optionmenu_switch = tk.OptionMenu(self.ventana,self.modelo.switch,"Cherry MX Red","Cherry MX Brown","Cherry MX Blue",command=self.evento_presionar_tecla)
        self.optionmenu_switch.config(bg="aquamarine3")
        self.optionmenu_switch.place(relx=0.3, rely=0.33, relheight=0.1, relwidth=0.45)

        self.modelo.keycaps.set("Seleccione")
        self.optionmenu_keycaps = tk.OptionMenu(self.ventana,self.modelo.keycaps,"ABS","PBT","POM",command=self.evento_presionar_tecla)
        self.optionmenu_keycaps.config(bg="aquamarine3")
        self.optionmenu_keycaps.place(relx=0.3, rely=0.45, relheight=0.1, relwidth=0.45)

        self.modelo.formato.set("Seleccione")
        self.optionmenu_formato = tk.OptionMenu(self.ventana,self.modelo.formato,"Full-size","Tenkeyless (TKL)","75%","65%","60%","40%","Ergonómico","Portátil",command=self.evento_presionar_tecla)
        self.optionmenu_formato.config(bg="aquamarine3")
        self.optionmenu_formato.place(relx=0.3,rely=0.57,relheight=0.1,relwidth=0.45)

        self.modelo.conectividad.set("Seleccione")
        self.optionmenu_conectividad = tk.OptionMenu(self.ventana, self.modelo.conectividad, "Cableado", "Bluetooth","2.4G",command=self.evento_presionar_tecla)
        self.optionmenu_conectividad.config(bg="aquamarine3")
        self.optionmenu_conectividad.place(relx=0.3, rely=0.7, relheight=0.1, relwidth=0.45)
        # Buttons
        self.boton_guardar = tk.Button(self.ventana, text="Guardar", bg="aquamarine3",command=lambda:self.guardar())
        self.boton_guardar.config(state=tk.DISABLED)
        self.boton_guardar.place(relx=0.3, rely=0.83, relheight=0.12, relwidth=0.17)

        self.boton_salir = tk.Button(self.ventana, text="Salir", bg="aquamarine3", command=self.salir)
        self.boton_salir.place(relx=0.58, rely=0.83, relheight=0.12, relwidth=0.17)

        self.boton_limpiar = tk.Button(self.ventana,text="Limpiar",bg="aquamarine3",command=self.limpiar)
        self.boton_limpiar.place(relx=0.8,rely=0.83,relheight=0.12,relwidth=0.15)

        self.ventana.mainloop()
