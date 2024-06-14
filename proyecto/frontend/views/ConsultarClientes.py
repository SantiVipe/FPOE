import os
import tkinter as tk
from tkinter import ttk,messagebox
from controller.ControllerCliente import ClienteController
import openpyxl as xls

class ConsultarCliente():
    def exportarExcel(self):
        datos=[]
        for cliente in self.tabla.get_children():
            datos.append([self.tabla.item(cliente)["values"][0],
                        self.tabla.item(cliente)["values"][1],
                        self.tabla.item(cliente)["values"][2],
                        self.tabla.item(cliente)["values"][3],
                        self.tabla.item(cliente)["values"][4],
                        self.tabla.item(cliente)["values"][5]])
        libro = xls.Workbook()
        hoja = libro.active

        hoja.append(["No.","Nombre","Apellido","Cédula","Teléfono","Email"])

        for fila in datos:
            hoja.append(fila)

        libro.save("clientes.xlsx")

        messagebox.showinfo("Confirmación","Datos exportados con éxito!")
        
    def __init__(self,ventanaPrincipal):
        self.ventana = tk.Toplevel(ventanaPrincipal)
        self.ventana.title("Consultar Clientes")
        self.ventana.config(bg="#AF7AC5")

        self.ruta = os.path.dirname(os.path.abspath(__file__))
        self.ruta_icono = os.path.join(self.ruta,"..","iconos","consultar.ico")
        self.ventana.iconbitmap(self.ruta_icono)

        self.label_titulo = tk.Label(self.ventana,text="Listado de Clientes",font=("Arial",12),bg="#AF7AC5")
        self.label_titulo.pack()

        self.tabla = ttk.Treeview(self.ventana,style="Custom.Treeview")
        self.tabla["columns"] = ["No.","Nombre","Apellido","Cédula","Teléfono","Email"]
        self.tabla.heading("#1",text="No.")
        self.tabla.heading("#2",text="Nombre")
        self.tabla.heading("#3",text="Apellido")
        self.tabla.heading("#4",text="Cédula")
        self.tabla.heading("#5",text="Teléfono")
        self.tabla.heading("#6",text="Email")

        self.comunicacion = ClienteController(self.ventana)
        self.listaClientes = self.comunicacion.consultar_clientes()
        i=1
        for cliente in self.listaClientes:
            self.tabla.insert('','end',values=[cliente['id'],cliente['nombre'],cliente['apellido'],cliente['cedula'],cliente['telefono'],cliente['correo']])
            i+=1
        
        self.tabla["show"] = "headings"
        self.tabla.column("#1",width=50)
        self.tabla.column("#2",width=100)
        self.tabla.column("#3",width=100)
        self.tabla.column("#4",width=100)
        self.tabla.column("#5",width=100)
        self.tabla.column("#6",width=150)

        self.scrollBar = ttk.Scrollbar(self.ventana,orient="vertical",command=self.tabla.yview)
        self.tabla.config(yscrollcommand=self.scrollBar.set)
        
        self.scrollBar.pack(side="right",fill="y")

        self.tabla.pack(fill="both",expand=True)

        self.botonExportarExcel = tk.Button(self.ventana,text="Exportar a Excel",command=lambda:self.exportarExcel(),bg="#7D3C98")
        self.botonExportarExcel.pack()

        self.estilo = ttk.Style()
        self.estilo.configure("Custom.Treeview", background="#AF7AC5")

        