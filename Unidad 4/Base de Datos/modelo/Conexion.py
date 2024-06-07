import mariadb as sql

class Conexion():
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = "tabla"
        self.__port = 3306

    def crear(self):
        self.__conexion = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = self.__database,
            port = self.__port)
        
    def cerrar(self):
        self.__conexion.close()

    def getConexion(self):
        return self.__conexion
