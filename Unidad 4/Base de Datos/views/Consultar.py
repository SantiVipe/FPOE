import tkinter as tk
from tkinter import ttk,messagebox
import openpyxl as xls
class Consultar():
    def exportarExcel(self):
        datos = []
        for persona in self.tabla.get_children():
            datos.append([self.tabla.item(persona)["values"][0],
                        self.tabla.item(persona)["values"][1],
                        self.tabla.item(persona)["values"][2]])
        
        libro = xls.Workbook()
        hoja = libro.active

        hoja.append(["No.","Cédula","Nombre"])

        for fila in datos:
            hoja.append(fila)

        libro.save("personas.xlsx")

        messagebox.showinfo("Confirmación","Datos exportados con éxito!")

    def __init__(self,ventana,persona):
        # Ventana
        self.ventana = tk.Toplevel(ventana)
        self.ventana.title("Consultar Personas")
        # Variables
        self.persona = persona
        # Labels
        self.label_titulo = tk.Label(self.ventana,text="Listado de Personas",font=("Arial",12))
        self.label_titulo.pack()
        # Tabla
        self.tabla = ttk.Treeview(self.ventana)
        self.tabla["columns"] = ["No.","Cédula","Nombre"]
        self.tabla.heading("#1",text="No.")
        self.tabla.heading("#2",text="Cédula")
        self.tabla.heading("#3",text="Nombre")

        self.listaPersonas = self.persona.consultar()
        i=1
        for persona in self.listaPersonas:
            self.tabla.insert('','end',values=[i,persona[0],persona[1]])
            i+=1

        self.tabla["show"] = "headings"
        self.tabla.column("#1",width=50)
        self.tabla.column("#2",width=100)
        self.tabla.column("#3",width=200)

        self.scrollBar = ttk.Scrollbar(self.ventana,orient="vertical",command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.pack(side="right",fill="y")

        self.tabla.pack(fill="both",expand=True)

        self.boton_exportar = ttk.Button(self.ventana,text="Exportar a Excel",command=lambda:self.exportarExcel())
        self.boton_exportar.pack()

        self.ventana.mainloop()