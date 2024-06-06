import re
class Validaciones():
    def __init__(self):
        pass

    def validarLetras(self,valor):
        patron = re.compile("^[A-Za-zñÑáéíóú]*$")
        if valor.get()!="":
            resultado = patron.match(valor.get()) is not None
            return resultado
    def validarNumeros(self,valor):
        if valor !="":
            patron = re.compile('^[0-9]*$')
            resultado = patron.match(str(valor)) is not None
            return resultado