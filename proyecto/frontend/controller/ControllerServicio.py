import requests
from tkinter import messagebox

class ControllerServicio():
    def __init__(self,ventanaPrincipal):
        self.ip="192.168.1.2"
        self.url = f"http://{self.ip}:8000/api/servicios/"
        self.ventanaPrincipal = ventanaPrincipal

    def consultar_servicios(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            servicios = response.json()
            servicios_con_cedula = []
            for servicio in servicios:
                cliente_id = servicio['cedula_cliente']
                cliente_response = requests.get(f"http://{self.ip}:8000/api/cliente/{cliente_id}/")
                if cliente_response.status_code == 200:
                    cliente = cliente_response.json()
                    servicio['cedula_cliente'] = cliente['cedula']
                    servicios_con_cedula.append(servicio)
            return servicios_con_cedula
        else:
            messagebox.showerror("Error", "Error al consultar los servicios.")
            return None
        
    def guardar_servicio(self, servicio_data):
        try:
            response = requests.post(self.url, json=servicio_data)
            if response.status_code == 201:
                return True
            else:
                messagebox.showerror("Error", f"Error al guardar el servicio: {response.json()}")
                return False
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error en la solicitud: {str(e)}")
            return False
        
    def comprobar_cedula(self,cedula):
        response = requests.get(self.url)
        if response.status_code == 200:
            servicios = response.json()
            for servicio in servicios:
                if servicio['cedula_cliente'] == cedula:
                    return servicio['id']
        else:
            messagebox.showerror("Error", "Error al consultar los servicio.")
            return False
        
    def consultar_cedula(self, cedula):
        response = requests.get(self.url)
        if response.status_code == 200:
            servicios = response.json()
            for servicio in servicios:
                if servicio['cedula']==cedula:
                    return servicio
            messagebox.showerror("Error", "No se encontró ningún servicio con la cédula proporcionada.")
        else:
            messagebox.showerror("Error", "Error al consultar los servicios.")
        return None
        
    def eliminar_servicio(self, servicio_id):
        try:
            response = requests.delete(f"{self.url}{servicio_id}/")
            if response.status_code == 204:
                return True
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el servicio.")
                return False
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error en la solicitud: {str(e)}")
            return False
    def consultar_servicios_por_cedula(self, cedula):
        try:
            # Obtener el ID del cliente usando su cédula
            response_cliente = requests.get(f"http://{self.ip}:8000/api/cliente/?cedula={cedula}")
            if response_cliente.status_code == 200:
                cliente = response_cliente.json()
                if cliente:
                    cliente_id = cliente[0]['id']  # Suponiendo que la consulta devuelve una lista con un solo cliente
                    # Obtener los servicios asociados a ese cliente
                    response_servicios = requests.get(f"{self.url}?cedula_cliente={cliente_id}")
                    if response_servicios.status_code == 200:
                        return response_servicios.json()
                    else:
                        messagebox.showerror("Error", "Error al obtener los servicios asociados al cliente.")
                else:
                    messagebox.showerror("Error", "No se encontró ningún cliente con la cédula proporcionada.")
            else:
                messagebox.showerror("Error", "Error al obtener el cliente.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error en la solicitud: {str(e)}")
        return []
    def consultar_servicio_por_id(self, servicio_id):
        try:
            url = f"{self.url}{servicio_id}"
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
            servicio = response.json()
            return servicio
        except requests.RequestException as e:
            print(f"Error al consultar el servicio: {e}")
            return None
    def actualizar(self, servicio_id, servicio_data):
        try:
            url = f"{self.url}{servicio_id}/"
            response = requests.put(url, json=servicio_data)
            response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
            return response.json()
        except requests.RequestException as e:
            print(f"Error al actualizar el servicio: {e}")
            return None