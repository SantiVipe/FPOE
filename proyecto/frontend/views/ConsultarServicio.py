import os
import tkinter as tk
from tkinter import ttk, messagebox
from controller.ControllerServicio import ControllerServicio
import openpyxl as xls

class ConsultarServicio():
    def exportarExcel(self):
        datos=[]
        for servicio in self.tabla.get_children():
            datos.append([self.tabla.item(servicio)["values"][0],
                        self.tabla.item(servicio)["values"][1],
                        self.tabla.item(servicio)["values"][2],
                        self.tabla.item(servicio)["values"][3],
                        self.tabla.item(servicio)["values"][4]])
        libro = xls.Workbook()
        hoja = libro.active

        hoja.append(["No.","Nombre_Servicio","Cédula","Descripcion","Valor"])

        for fila in datos:
            hoja.append(fila)

        libro.save("servicio.xlsx")

        messagebox.showinfo("Confirmación","Datos exportados con éxito!")
        
    
    def __init__(self,ventanaPrincipal):
        self.ventana=tk.Toplevel(ventanaPrincipal)
        self.ventana.title("Consultar Servicios")
        self.ventana.config(bg="#AF7AC5")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","consultar.ico")
        self.ventana.iconbitmap(self.ruta_icono)

        self.label_titulo = tk.Label(self.ventana,text="Listado de Servicios",font=("Arial",12), bg="#AF7AC5")
        self.label_titulo.pack()

        self.tabla = ttk.Treeview(self.ventana,style="Custom.Treeview")
        self.tabla["columns"] = ["No.","Nombre_Servicio","Cédula","Descripcion","Valor"]
        self.tabla.heading("#1",text="No.")
        self.tabla.heading("#2",text="Nombre_Servicio")
        self.tabla.heading("#3",text="Cédula")
        self.tabla.heading("#4",text="Descripcion")
        self.tabla.heading("#5",text="Valor")

        self.comunicacion= ControllerServicio(self.ventana)
        self.listaServicios =self.comunicacion.consultar_servicios()
        i=1
        for servicio in self.listaServicios:
            self.tabla.insert('','end',values=[servicio['id'],servicio['nombre_servicio'],servicio['cedula_cliente'],servicio['descripcion'],servicio['valor']])
            i+=1
        
        self.tabla["show"] = "headings"
        self.tabla.column("#1",width=50)
        self.tabla.column("#2",width=100)
        self.tabla.column("#3",width=100)
        self.tabla.column("#4",width=100)
        self.tabla.column("#5",width=100)

        self.scrollBar = ttk.Scrollbar(self.ventana,orient="vertical",command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.pack(side="right",fill="y")

        self.tabla.pack(fill="both",expand=True)

        self.botonExportarExcel = tk.Button(self.ventana,text="Exportar a Excel",command=lambda:self.exportarExcel(),bg="#7D3C98")
        self.botonExportarExcel.pack()

        self.estilo = ttk.Style()
        self.estilo.configure("Custom.Treeview", background="#AF7AC5")


        

