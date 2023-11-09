class Cuadro:
    def __init__(self) -> None:
        self._codigo = None # Este valor debe ser unico para cada cuadro
        self._nombre = None
        self._largo = None
        self._ancho = None
        self._fecha_creacion = None
        self._tecnica = None
        self._pintor = None
    
    @property
    def codigo(self): 
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo): #TODO Validar que sea único, es decir que no exista ningun otro cuadro en con el mismo código
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre): #TODO Validar que es alfabetico
        self._nombre = nombre

    @property
    def largo(self):
        return self._largo

    @largo.setter
    def largo(self, largo): #TODO Validar que sea máximo un metro
        self._largo = largo

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho): #TODO Validar que sea máximo un metro
        self._ancho = ancho

    @property
    def fecha_creacion(self):
        return self._fecha_creacion
    
    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion): #TODO Validar que tenga formato de fecha latinoamericana dd/mm/aaaa
        self._fecha_creacion = fecha_creacion

    @property
    def tecnica(self):
        return self._tecnica
    
    @tecnica.setter
    def tecnica(self, tecnica):
        self._tecnica = tecnica

    @property
    def pintor(self):
        return self._pintor
    
    @pintor.setter
    def pintor(self, pintor): #TODO Validar que este resgitsrado el pintor en la base de datos
        self._pintor = pintor