from modelo.Conexion import Conexion
from tkinter import messagebox

class Persona():
    
    def __init__(self, cedula, nombre):
        self.cedula= cedula
        self.nombre= nombre

    def guardar(self, cedula, nombre):
        mi= Conexion()
        mi.crear()
        con= mi.getConexion()
        cursor=con.cursor()
        try:
            cursor.execute("INSERT INTO persona (cedula, nombre) VALUES (%s, %s)", (cedula, nombre))
            con.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Confirmacion", "La persona se registró exitosamente")
            else:
                messagebox.showerror("Error", "No se pudo registrar la persona")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {e}")
        finally:
            mi.cerrar()

    def actualizar(self, cedula, nombre):
        mi= Conexion()
        mi.crear()
        con= mi.getConexion()
        cursor=con.cursor()
        cursor.execute("UPDATE persona SET nombre=? WHERE cedula=?",(nombre,cedula))
        con.commit()
        messagebox.showinfo("Confirmacion","La persona se actualizado exitosamente")
        mi.cerrar()

    def borrar(self, cedula):
        mi= Conexion()
        mi.crear()
        con= mi.getConexion()
        cursor=con.cursor()
        cursor.execute("DELETE FROM persona WHERE cedula="+(cedula))
        con.commit()
        messagebox.showinfo("Confirmacion","La {} 'persona' se actualizado exitosamente".format(cursor.rowcount))
        mi.cerrar()

    def consultar(self):
        mi= Conexion()
        mi.crear()
        con= mi.getConexion()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM persona")
        listaPersonas=cursor.fetchall()
        return listaPersonas

    def buscar(self, cedula,warning=True):
        mi = Conexion()
        mi.crear()
        con = mi.getConexion()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM persona WHERE cedula ="+cedula)
        listaPersonas = cursor.fetchall()
        persona=None
        if len(listaPersonas) > 0:
            persona = listaPersonas[0]
        elif warning:
            messagebox.showwarning("Advertencia", f"No se ha encontrado una persona con cédula {cedula}, intente de nuevo...")
        mi.cerrar()
        return persona