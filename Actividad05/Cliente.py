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
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimeinto): #TODO Validar que la fecha de nacieminto corresponda a dd/mm/aaaa
        self._fecha_nacimiento = fecha_nacimeinto

    @property
    def residencia(self):
        return self._residencia
    
    @residencia.setter
    def residencia(self, residencia): #TODO Validar que la residencia sea alfabetico
        self._residencia = residencia
    
    def __str__(self) -> str:
        return "\tNombre: {}\n\tFecha de nacimiento: {}\n\tResidencia: {}\n".format(self._nombre, self._fecha_nacimiento, self._residencia)