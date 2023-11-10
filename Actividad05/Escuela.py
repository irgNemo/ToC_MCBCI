class Escuela:
    def __init__(self) -> None:
        self._nombre = None
        self._pais = None

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): #TODO Validar que el nombre corresponde a valores alfabeticos
        self._nombre = nombre

    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, pais): #TODO Validar que contiene caracteres alfabeticos
        self._pais = pais