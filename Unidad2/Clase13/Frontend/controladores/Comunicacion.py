import requests
import tkinter.messagebox as alerta
class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/v1/teclado'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, teclado,switch,keycaps,formato,conectividad):
        try:
            print(teclado,switch,keycaps,formato,conectividad)
            data = {
                'teclado': teclado,
                'switch': switch,
                'keycaps': keycaps,
                'formato': formato,
                'conectividad': conectividad
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def eliminar(self, id):
        try:
            response = requests.delete(self.url + '/' + str(id))
            if response.status_code == 204:
                alerta.showinfo("Éxito", "Teclado eliminado exitosamente.")
            else:
                alerta.showerror("Error", f"Error al eliminar el teclado: {response.status_code}")
        except Exception as e:
            print(f"Error al eliminar: {e}")
            alerta.showerror("Error", "Error al eliminar el teclado.")

    def buscarTeclado(self,id):
        response = requests.get(self.url + '/' + str(id))
        response.raise_for_status()
        teclado = response.json()
        if not teclado:
            raise ValueError("Respuesta JSON vacía")
        return teclado
    
    def consultar(self, id):
        try:
            response = requests.get(self.url + '/' + str(id))
            response.raise_for_status()  # Esto lanzará un error para códigos de estado HTTP 4xx/5xx
            data = response.json()
            if not data:
                raise ValueError("Respuesta JSON vacía")
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            alerta.showerror("Error", f"Error HTTP al consultar el teclado: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            alerta.showerror("Error", f"Error de solicitud al consultar el teclado: {req_err}")
        except ValueError as json_err:
            print(f"Error al analizar JSON: {json_err}")
            alerta.showerror("Error", "Error al consultar el teclado: Respuesta JSON no válida.")
        except Exception as e:
            print(f"Error al consultar: {e}")
            alerta.showerror("Error", "Error al consultar el teclado.")
        return None
    
    def consultar_teclados(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                teclado = response.json()
                return teclado  # Devolver la lista de teclados directamente
            else:
                alerta.showerror("Error", "Error al consultar los teclados.")
        except Exception as e:
            print(f"Error al consultar teclados: {e}")
            alerta.showerror("Error", "Error al consultar los teclados.")
        return []  # Devolver una lista vacía si ocurre un error
    
    def actualizar(self,id, teclado, switch, keycaps, formato, conectividad):
        data = {
            'teclado': teclado,
            'switch': switch,
            'keycaps': keycaps,
            'formato': formato,
            'conectividad': conectividad
        }
        print(f"URL: {self.url}/{id}")
        print(f"Data: {data}")
        try:
            response = requests.put(f"{self.url}/{id}/", json=data)
            print(f"Response: {response.text}")  # Imprimir la respuesta del servidor
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except Exception as e:
            print(f"Other error occurred: {e}")
            return None
