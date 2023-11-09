import re

class Persona:
    def __init__(self, nombre = None, pais = None, fecha_nacimiento = None) -> None:
        self._nombre = nombre
        self._pais = pais
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self):
        return self.nombre
    
    @nombre.setter
    def nombre(self, nombre):
        match = re.match("[a-zA-Z ]+", nombre)
        assert match, "El nombre debe de contener valores alfabeticos y espacio"
        self._nombre = nombre

    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, pais):
        self._pais = pais

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_naciemiento):
        self._fecha_nacimiento = fecha_naciemiento

    def __str__(self) -> str:
        return "Nombre: {}".format(self.nombre)