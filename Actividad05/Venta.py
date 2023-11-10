class Venta:
    def __init__(self) -> None:
        self._id_venta = None # El id_venta debe ser unico para cada venta
        self._cuadro = None
        self._precio = None
        self._fecha = None
        self._cliente = None
    
    @property
    def id_venta(self):
        return self._id_venta
    
    @id_venta.setter
    def id_venta(self, id_venta):
        self._id_venta = id_venta

    @property
    def cuadro(self):
        return self._cuadro
    
    @cuadro.setter
    def cuadro(self, cuadro): #TODO Validar que la variable cuadro corresponda a la clase Cuadro
        self._cuadro = cuadro
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self, fecha): #TODO Validar que la fecha tenga el formato dd//mm/aaaa 
        self._fecha = fecha