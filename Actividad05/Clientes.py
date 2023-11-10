class Cliente:
    def __init__(self) -> None:
        self._nombre = None
        self._fecha_nacimiento = None
        self._residencia = None

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): #TODO Validar que el nombre correspodna a una cadena alfabetica
        self._nombre = nombre

    @property
    def fecha_nacimeinto(self):
        return self._fecha_nacimiento
    
    @fecha_nacimeinto.setter
    def fecha_nacieminto(self, fecha_nacimeinto): #TODO Validar que la fecha de nacieminto corresponda a dd/mm/aaaa
        self._fecha_nacimiento = fecha_nacimeinto