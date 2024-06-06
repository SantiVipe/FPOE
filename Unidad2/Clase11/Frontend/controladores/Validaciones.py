import re
class Validaciones():
    def __init__(self):
        pass

    def validarLetras(valor):
        patron = re.compile("^[A-Za-zñÑáéíóú]*$")
        resultado = patron.match(valor.get()) is not None
        return resultado