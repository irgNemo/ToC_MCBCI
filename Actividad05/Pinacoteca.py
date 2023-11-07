class Pinacoteca:
    def __init__(self) -> None:
        print("Objeto pinacoteca creado")
        self._nombre = None
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self) -> str:
        return "Datos de la pinoteca \n Nombre: {} ".format(self._nombre)