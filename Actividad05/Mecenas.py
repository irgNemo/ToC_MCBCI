class Mecenas:
    def __init__(self) -> None:
        self._nombre = None
        self._pais = None
        self._ciudad_nacimienito = None
        self._fecha_fallecimiento = None
        self._patrocinados = []

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): #TODO Validar que la cadena correspodnda a valores alfabeticos
        self._nombre = nombre
    
    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def pais(self, pais): #TODO Validar que la cadena de texto corresponda a valores alfabeticos
        self._pais = pais
    
    @property
    def ciudad_nacimiento(self):
        return self._ciudad_nacimienito
    
    @ciudad_nacimiento.setter
    def ciudad_nacimeinto(self, ciudad_nacimiento): #TODO Validar que la cadena de texto corresponda a valores alfabeticos
        self._ciudad_nacimienito = ciudad_nacimiento

    @property
    def fecha_fallecimiento(self):
        return self._fecha_fallecimiento

    @fecha_fallecimiento.setter
    def fecha_fallecimiento(self, fecha_fallecimiento): #TODO Validar que la cadena de texto corresponda a valores alfabeticos
        self._fecha_fallecimiento = fecha_fallecimiento

    @property
    def patrocinados(self):
        return self._patrocinados
    
    @patrocinados.setter
    def patrocinados(self, patrocinados): #TODO Validar que la variable patrocinado sea una lista y que contenga referencias a tipos de datos Pintor
        self._patrocinados = patrocinados

    def agregar_patrocinado(self, patrocinado): #TODO Validar que la variable patrocinado sea de tipo Pintor
        self._patrocinados.append(patrocinado)