import threading
import time
import requests
import os

class BackupController:
    def __init__(self, clientes_url, servicios_url):
        self.clientes_url = clientes_url
        self.servicios_url = servicios_url
        self.carpeta = "backups"
        self.carpeta_backup()
        self.iniciar_hilo()

    def carpeta_backup(self):
        if not os.path.exists(self.carpeta):
            os.makedirs(self.carpeta)

    def iniciar_hilo(self):
        backup_thread = threading.Thread(target=self.informacion_backup)
        backup_thread.daemon = True
        backup_thread.start()

    def informacion_backup(self):
        while True:
            try:
                # Realiza la petición para obtener los datos de clientes
                response_clientes = requests.get(self.clientes_url)
                if response_clientes.status_code == 200:
                    clientes_data = response_clientes.json()
                else:
                    clientes_data = []

                # Realiza la petición para obtener los datos de servicios
                response_servicios = requests.get(self.servicios_url)
                if response_servicios.status_code == 200:
                    servicios_data = response_servicios.json()
                else:
                    servicios_data = []

                # Guarda los datos en archivos planos
                clientes_file_path = os.path.join(self.carpeta, "clientes.txt")
                servicios_file_path = os.path.join(self.carpeta, "servicios.txt")

                with open(clientes_file_path, "w") as clientes_file:
                    clientes_file.write(str(clientes_data))

                with open(servicios_file_path, "w") as servicios_file:
                    servicios_file.write(str(servicios_data))

                print("Backup realizado exitosamente.")

            except Exception as e:
                print("Error en la copia de seguridad:", str(e))

            # Espera un minuto antes de hacer la siguiente copia de seguridad
            time.sleep(60)

