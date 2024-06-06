import tkinter as tk
from tkinter.messagebox import askyesno
class MenuConsultarID():
    
    def consultarID(self):
        teclado = self.comunicacion.consultar(self.entry_id.get())
        if teclado is not None and isinstance(teclado, dict) and 'teclado' in teclado:
            self.entry_teclado.config(state="normal")
            self.entry_teclado.delete(0, tk.END)  # Asegúrate de limpiar el campo antes de insertar
            self.entry_teclado.insert(0, teclado['teclado'])
            self.entry_teclado.config(state="disabled")
        else:
            self.labelValidacionID.config(text="Error al consultar: No se encontró el teclado")

    def evento_presionar_tecla(self,evento):
        if (self.entry_id).get()=="":
            texto_validar_id = "No se permiten espacion en blanco"
            self.boton_consultar_id.config(state="disabled")
        elif self.validacion.validarNumeros(self.entry_id.get()):
            texto_validar_id = ""
            self.boton_consultar_id.config(state="normal")
        else:
            texto_validar_id = "Sólo se permiten números en el campo"
            self.boton_consultar_id.config(state="disabled")
        self.labelValidacionID.config(text=texto_validar_id)

    def salir(self):
        if askyesno("Salir de la aplicación", '¿Desea salir de la aplicación?'):
            self.ventana.destroy()

    def limpiar(self):
        self.entry_id.delete(0,tk.END)
        self.entry_teclado.config(state="normal")
        self.entry_teclado.delete(0,tk.END)
        self.entry_teclado.config(state="disabled")
        self.boton_consultar_id.config(state="disabled")
        
    def __init__(self,menu,modelo,validacion,comunicacion):
        # Ventana

        self.ventana = tk.Toplevel(menu)
        self.ventana.geometry("500x500")
        self.ventana.title("Consultar por ID")
        self.ventana.config(bg="aquamarine1")

        # Variables
        self.modelo = modelo
        self.validacion = validacion
        self.comunicacion = comunicacion

        # Labels

        self.label_titulo = tk.Label(self.ventana,text="Consultar Teclado",bg="aquamarine1",font=("Arial",20))
        self.label_titulo.place(relx=0.4,rely=0.1,relheight=0.1,relwidth=0.2)

        self.label_id = tk.Label(self.ventana,text="ID:",bg="aquamarine1",font=("Arial",16))
        self.label_id.place(relx=0.2,rely=0.35,relheight=0.1,relwidth=0.1)

        self.label_teclado = tk.Label(self.ventana,text="Teclado:",bg="aquamarine1",font=("Arial",16))
        self.label_teclado.place(relx=0.2,rely=0.55,relheight=0.1,relwidth=0.1)

        self.labelValidacionID = tk.Label(self.ventana,text="",bg="aquamarine1",fg="red",font=("Arial",12))
        self.labelValidacionID.place(relx=0.4,rely=0.45,relheight=0.1,relwidth=0.2)

        # Entrys

        self.entry_id = tk.Entry(self.ventana,bg="aquamarine3")

        self.entry_id.place(relx=0.4,rely=0.35,relheight=0.1,relwidth=0.2)

        self.entry_teclado = tk.Entry(self.ventana,state="disabled")
        self.entry_teclado.bind("<KeyRelease>", self.evento_presionar_tecla)
        self.entry_teclado.place(relx=0.4,rely=0.55,relheight=0.1,relwidth=0.2)

        # Botones

        self.boton_consultar_id = tk.Button(self.ventana,text="Consultar ID",font=("Arial",12),command=lambda:self.consultarID())
        self.boton_consultar_id.place(relx=0.35,rely=0.8,relheight=0.1,relwidth=0.1)
        self.boton_consultar_id.config(state="disabled")

        self.boton_salir = tk.Button(self.ventana, text="Salir",font=("Arial",12), bg="aquamarine3", command=self.salir)
        self.boton_salir.place(relx=0.55, rely=0.8, relheight=0.1, relwidth=0.1)

        self.boton_limpiar = tk.Button(self.ventana,text="Limpiar",font=("Arial",12),bg="aquamarine3",command=self.limpiar)
        self.boton_limpiar.place(relx=0.8,rely=0.8,relheight=0.1,relwidth=0.1)

        self.ventana.mainloop()