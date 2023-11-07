from Persona import Persona

class Pintor(Persona):
    def __init__(self, nombre = None, pais = None, fecha_de_nacimiento = None, fecha_de_defuncion = None, ciudad = None):
        super().__init__(nombre, pais, fecha_de_nacimiento)
        self._fecha_de_defuncion = None
        self._ciudad = None
    
    @property
    def fecha_de_defuncion(self):
        return self._fecha_de_defuncion
    
    @fecha_de_defuncion.setter
    def fecha_de_defuncion(self, fecha_de_defuncion):
        self._fecha_de_defuncion = fecha_de_defuncion
    
