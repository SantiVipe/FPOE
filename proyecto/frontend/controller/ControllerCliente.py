import requests
from tkinter import messagebox

class ClienteController():
    
    def __init__(self,ventanaPrincipal):
        self.ip = "192.168.1.2"
        self.url=f"http://{self.ip}:8000/api/cliente/"
        self.ventanaPrincipal=ventanaPrincipal
        
    def consultar_clientes(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            teclados = response.json()
            return teclados
        else:
            messagebox.showerror("Error", "Error al consultar los clientes.")
            return None

    def guardar_cliente(self, cliente_data):
        response = requests.post(self.url, json=cliente_data)
        if response.status_code == 201:
            messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
            return True
        else:
            messagebox.showerror("Error", "Error al guardar el cliente.")
            return False

    def eliminar_cliente_por_cedula(self, cedula):
        response = requests.get(self.url)
        if response.status_code == 200:
            clientes = response.json()
            cliente_a_eliminar = next((c for c in clientes if c["cedula"] == cedula), None)
            if cliente_a_eliminar:
                cliente_id = cliente_a_eliminar['id']
                url_delete = f"{self.url}{cliente_id}/"
                response_delete = requests.delete(url_delete)
                if response_delete.status_code == 204:
                    messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
                    return True
                else:
                    messagebox.showerror("Error", "Error al eliminar el cliente.")
            else:
                messagebox.showerror("Error", "No se encontró ningún cliente con la cédula proporcionada.")
        else:
            messagebox.showerror("Error", "Error al consultar los clientes.")
        return False

    def comprobar_cedula(self,cedula):
        response = requests.get(self.url)
        if response.status_code == 200:
            clientes = response.json()
            for cliente in clientes:
                if cliente['cedula'] == cedula:
                    return cliente['id']
        else:
            messagebox.showerror("Error", "Error al consultar los clientes.")
            return False
    def consultar_cliente_cedula(self,cedula):
        response = requests.get(self.url)
        if response.status_code == 200:
            clientes = response.json()
            cliente = next((cliente for cliente in clientes if cliente["cedula"] == cedula), None)
            if cliente:
                cliente_id = cliente['id']
                respuesta = requests.get(f"{self.url}{cliente_id}/")
                if respuesta.status_code == 200:
                    return respuesta.json()
            else:
                messagebox.showerror("Error","No hay ningún cliente registrado con la cédula ingresada.")
        else:
            messagebox.showerror("Error", f"No se encontró el cliente con ID: {cliente_id}")
            return None
    def actualizar_cliente(self,cliente_data):
        response = requests.get(self.url)
        if response.status_code == 200:
            clientes = response.json()
            cliente_a_actualizar = next((cliente for cliente in clientes if cliente["cedula"] == cliente_data["cedula"]), None)
            if cliente_a_actualizar:
                cliente_id = cliente_a_actualizar['id']
                actualizar = requests.put(f"{self.url}{cliente_id}/", json=cliente_data)
                if actualizar.status_code == 200:
                    return True
                else:
                    messagebox.showerror("Error", "Error al actualizar el cliente.")
                    return False