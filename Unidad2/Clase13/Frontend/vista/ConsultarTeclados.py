import tkinter as tk
from tkinter.ttk import Treeview,Scrollbar
class ConsultarTeclados():

    def __init__(self,menu,comunicacion):
        # Ventana
        self.ventana = tk.Toplevel(menu)
        self.ventana.title("Consultar Teclados")

        # Variables
        self.comunicacion = comunicacion

        # Labels
        self.labelTitulo = tk.Label(self.ventana,text="Listado de Teclados",font=("Arial",14))
        self.labelTitulo.pack()

        # Tabla
        self.tabla = Treeview(self.ventana)
        self.tabla["columns"] = ["No.","Teclado","Switch","Keycaps","Formato","Conectividad"]
        self.tabla.heading("#1",text="No.")
        self.tabla.heading("#2",text="Teclado")
        self.tabla.heading("#3",text="Switch")
        self.tabla.heading("#4",text="Keycaps")
        self.tabla.heading("#5",text="Formato")
        self.tabla.heading("#6",text="Conectividad")

        self.listaTeclados = self.comunicacion.consultar_teclados()
        i=1
        for teclado in self.listaTeclados:
            self.tabla.insert('','end',values=[i,teclado['teclado'],teclado['switch'],teclado['keycaps'],teclado['formato'],teclado['conectividad']])
            i+=1
        
        self.tabla["show"] = "headings"
        self.tabla.column("#1",width=50)
        self.tabla.column("#2",width=200)
        self.tabla.column("#3",width=150)
        self.tabla.column("#4",width=150)
        self.tabla.column("#5",width=200)
        self.tabla.column("#6",width=150)

        # ScrollBar
        self.scrollBar = Scrollbar(self.ventana,orient="vertical",command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.pack(side="right",fill="y")

        self.tabla.pack(fill="both",expand=True)

        self.ventana.mainloop()