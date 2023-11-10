from Persona import Persona

class Pintor(Persona):
    def __init__(self, nombre = None, pais = None, fecha_de_nacimiento = None, fecha_de_defuncion = None, ciudad = None):
        super().__init__(nombre, pais, fecha_de_nacimiento)
        self._fecha_de_defuncion = None
        self._ciudad = None
        self._maestro = None
        self._alumnos = []
        self._mecenas = []
        self._escuela_fecha = ()
    
    @property
    def fecha_de_defuncion(self):
        return self._fecha_de_defuncion
    
    @fecha_de_defuncion.setter
    def fecha_de_defuncion(self, fecha_de_defuncion):
        self._fecha_de_defuncion = fecha_de_defuncion
    
    @property
    def maestro(self):
        return self._maestro
    
    @maestro.setter
    def maestro(self, maestro): #TODO Validar que la variable maestro es una lista y que contiene elementos de la clase Pintor
        self._maestro = maestro

    @property
    def alumnos(self):
        return self._alumnos
    
    @alumnos.setter
    def alumnos(self, alumnos): #TODO Validar que la variable alumnos es una lista y que cada elemento es de tipo Pintor
        self._alumnos = alumnos

    @property
    def mecenas(self):
        return self._mecenas
    
    @mecenas.setter
    def mecenas(self, mecenas): #TODO Validar que la variable mecenas es una lista y contiene tuplas de valores (Mecenas, dd/mm/aaaa)
        self._mecenas = mecenas

    def agregar_mecenas(self, mecenas, fecha): #TODO Validar que la variable mecenas sea de tipo Mecenas y que la fecha tenga el formato dd/mm/aaaaa
        self._mecenas.append((mecenas, fecha))
    
    @property
    def escuela_fecha(self):
        return self._escuela_fecha
        
    @escuela_fecha.setter
    def escuela_fecha(self, escuela, fecha): #TODO Validar que escuela sea una cadena alfabetica y la fecha tenga el formato dd/mm/aaaa
        self._escuela_fecha = escuela, fecha
