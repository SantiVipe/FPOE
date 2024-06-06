import tkinter as tk
from tkinter.messagebox import askyesno
from modelos.Teclado import Teclado
from controladores.Validaciones import Validaciones

class Interfaz:
    def mostrar_interfaz():
        def salir():
            if askyesno("Salir de la aplicación", '¿Desea salir de la aplicación?'):
                ventana.destroy()

        def evento_presionar_tecla(evento):
            if Validaciones.validarLetras(modelo.teclado):
                texto_validar_teclado = ""
            else:
                texto_validar_teclado = "Sólo se permiten letras en el campo"
            labelValidacionTeclado.config(text=texto_validar_teclado, fg="red")

            if Validaciones.validarLetras(modelo.switch):
                texto_validar_switch = ""
            else:
                texto_validar_switch = "Solo se aceptan los switches previos"
            labelValidacionSwitch.config(text=texto_validar_switch, fg="red")

            if Validaciones.validarLetras(modelo.keycaps):
                texto_validar_keycaps = ""
            else:
                texto_validar_keycaps = "Solo se aceptan las keycaps previas"
            labelValidacionKeycaps.config(text=texto_validar_keycaps, fg="red")

            if Validaciones.validarLetras(modelo.formato):
                texto_validar_formato = ""
            else:
                texto_validar_formato = "Solo se aceptan los formatos previos"
            labelValidacionFormato.config(text=texto_validar_formato, fg="red")

            if Validaciones.validarLetras(modelo.conectividad):
                texto_validar_conectividad = ""
            else:
                texto_validar_conectividad = "Solo se permiten los conectores previos"
            labelValidacionConectividad.config(text=texto_validar_conectividad, fg="red")

        # Ventana
        ventana = tk.Tk()
        ventana.geometry("500x500")
        ventana.title("App")
        ventana.config(bg="aquamarine1")

        # Variables
        modelo = Teclado(ventana)

        # Labels
        label_titulo = tk.Label(ventana, text="Personalice su Teclado", bg="aquamarine1")
        label_titulo.place(relx=0.35, rely=0.05, relheight=0.1, relwidth=0.3)

        label_teclado = tk.Label(ventana, text="Teclado:", bg="aquamarine1")
        label_teclado.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.1)

        label_switch = tk.Label(ventana, text="Switch:", bg="aquamarine1")
        label_switch.place(relx=0.1, rely=0.33, relheight=0.1, relwidth=0.1)

        label_keycaps = tk.Label(ventana, text="Keycaps:", bg="aquamarine1")
        label_keycaps.place(relx=0.1, rely=0.45, relheight=0.1, relwidth=0.1)

        label_formato = tk.Label(ventana, text="Formato:", bg="aquamarine1")
        label_formato.place(relx=0.1, rely=0.57, relheight=0.1, relwidth=0.1)

        label_conectividad = tk.Label(ventana, text="Conectividad:", bg="aquamarine1")
        label_conectividad.place(relx=0.07, rely=0.7, relheight=0.1, relwidth=0.17)

        labelValidacionTeclado = tk.Label(ventana, text="", bg="aquamarine1")
        labelValidacionTeclado.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.15)

        labelValidacionSwitch = tk.Label(ventana, text="", bg="aquamarine1")
        labelValidacionSwitch.place(relx=0.8, rely=0.33, relheight=0.1, relwidth=0.15)

        labelValidacionKeycaps = tk.Label(ventana, text="", bg="aquamarine1")
        labelValidacionKeycaps.place(relx=0.8, rely=0.45, relheight=0.1, relwidth=0.15)

        labelValidacionFormato = tk.Label(ventana, text="", bg="aquamarine1")
        labelValidacionFormato.place(relx=0.8, rely=0.57, relheight=0.1, relwidth=0.15)

        labelValidacionConectividad = tk.Label(ventana, text="", bg="aquamarine1")
        labelValidacionConectividad.place(relx=0.8, rely=0.7, relheight=0.1, relwidth=0.15)

        # Entrys
        entry_teclado = tk.Entry(ventana, bg="aquamarine3", textvariable=modelo.teclado)
        entry_teclado.bind("<KeyRelease>", evento_presionar_tecla)
        entry_teclado.place(relx=0.3, rely=0.2, relheight=0.1, relwidth=0.45)

        entry_switch = tk.Entry(ventana, bg="aquamarine3", textvariable=modelo.switch)
        entry_switch.bind("<KeyRelease>", evento_presionar_tecla)
        entry_switch.place(relx=0.3, rely=0.33, relheight=0.1, relwidth=0.45)

        entry_keycaps = tk.Entry(ventana, bg="aquamarine3", textvariable=modelo.keycaps)
        entry_keycaps.bind("<KeyRelease>", evento_presionar_tecla)
        entry_keycaps.place(relx=0.3, rely=0.45, relheight=0.1, relwidth=0.45)

        entry_formato = tk.Entry(ventana, bg="aquamarine3", textvariable=modelo.formato)
        entry_formato.bind("<KeyRelease>", evento_presionar_tecla)
        entry_formato.place(relx=0.3, rely=0.57, relheight=0.1, relwidth=0.45)

        entry_conectividad = tk.Entry(ventana, bg="aquamarine3", textvariable=modelo.conectividad)
        entry_conectividad.bind("<KeyRelease>", evento_presionar_tecla)
        entry_conectividad.place(relx=0.3, rely=0.7, relheight=0.1, relwidth=0.45)

        # Buttons
        boton_guardar = tk.Button(ventana, text="Guardar", bg="aquamarine3")
        boton_guardar.place(relx=0.3, rely=0.83, relheight=0.12, relwidth=0.17)

        boton_salir = tk.Button(ventana, text="Salir", bg="aquamarine3", command=salir)
        boton_salir.place(relx=0.58, rely=0.83, relheight=0.12, relwidth=0.17)

        ventana.mainloop()
