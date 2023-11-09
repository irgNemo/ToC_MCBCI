from Cuadro import Cuadro
from Venta import Venta

class Pinacoteca:
    def __init__(self, nombre, direccion, ciudad, largo, ancho) -> None:
        self._nombre = nombre
        self._direccion = direccion
        self._ciudad = ciudad
        self._largo = largo
        self._ancho = ancho
        self._cuadros = []
        self._clientes = []
        self._ventas = []
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre) -> None: #TODO Validar el nombre con valores alfabeticos
        if not nombre.isalpha():
            print("El nombre no corresponde a valores alfabeticos")
            return None
        self._nombre = nombre

    @property
    def direccion(self) -> str: 
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion) -> None: #TODO Validar la direccion con caracteres alfanuméricos
        if not direccion.isalnum():
            print("EL valor no corresponde a un valor alfanunmérico")
            return None
        self._direccion = direccion

    @property
    def ciudad(self) -> str:
        return self._ciudad
    
    @ciudad.setter
    def ciudad(self, ciudad): #TODO Validar la ciudad con caracteres alfabeticos
        self._ciudad = ciudad

    @property
    def largo(self) -> float:
        return self._largo
    
    @largo.setter
    def largo(self, largo): #TODO Validar el largo con valores numéricos
        self._largo = largo
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho): #TODO Validar el ancho con valores numéricos
        self._ancho = ancho
    
    @property
    def cuadros(self) -> list:
        return self._cuadros
    
    @cuadros.setter
    def cuadros(self, cuadros) -> bool:
        if not isinstance(cuadros, list):
            print("La valor que asignaste no corresponde a una lista")
            return False
        
        if not all(isinstance(cuadro, Cuadro) for cuadro in cuadros):
            print("No todos los elementos de la lista son cuadros")
            return False
        
        self._cuadros = cuadros
        return True

    @property
    def ventas(self) -> list:
        return self._ventas
    
    @ventas.setter
    def ventas(self, ventas) -> None: #TODO Validar que sea una lista y que contenga solo valores de tipo Venta
        self._ventas = ventas

    def agregar_cuadro(self, cuadro) -> bool: #TODO Validar que el cuadro sea de tipo cuadro
        if not isinstance(cuadro, Cuadro):
            print("El valor asignado no corresponde al tipo de dato Cuadro")
            return False
        self.cuadros.append(cuadro)
        return True
    
    def quitar_cuadro(self, nombre) -> bool: #TODO Validar que el nombre no sea vacio
        if not isinstance(nombre, str) or nombre == "":
            print("Indicar el nombre del cuadro que desear remover")
            return False
        
        for cuadro in self.cuadros:
            if cuadro.nombre == nombre:
                self.cuadros.remove(cuadro)
                return True
        
        print("Cuadro no encontrado")
        return False
    
    def agregar_venta(self, venta) -> bool: #TODO Validar que sea una lista y que los elementos correspondan a valores de tipo Venta
        if not isinstance(venta, Venta):
            print("El valor no corresponde al tipo de datos Venta")
            return False
        self._ventas.append(venta)
        return True

    def quitar_venta(self, id_venta) -> bool: #TODO Validar que el id_venta sea diferente de vacio y numerico y remover el objeto de la lista
        if not (isinstance(id_venta, str) and id_venta.isdigit()):
            print("El valor no es un numérico")
            return False
        
        for venta in self.ventas:
            if venta.id_venta == id_venta:
                self.ventas.remove(venta)
                return True
    
    def __str__(self) -> str:
        return "Datos de la pinoteca \n Nombre: {} ".format(self._nombre)