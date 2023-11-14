from enum import Enum
import sys
from Pintor import Pintor
from Cliente import Cliente
from Cuadro import Cuadro
from Escuela import Escuela
from Mecenas import Mecenas
from Persona import Persona
from Pinacoteca import Pinacoteca
from Venta import Venta
import re
import pickle


class Sgp:

    def __init__(self) -> None:
        #self._pinacotecas = []
        #self._clientes = []
        #self._cuadros = []
        #self._escuelas = []
        #self._mecenas = []
        #self._pintores = []
        #self._ventas = []
        self._bd = {"pinacotecas":[], "clientes":[], "cuadros": [], "escuelas":[], "mecenas": [], "pintores": [], "ventas": []}
        

    @property
    def pinacotecas(self):
        return self._pinacotecas
    
    @pinacotecas.setter
    def pinacotecas(self, pinacotecas): #TODO Validar que la variable pinacotecas sea una lista y contenga solo referencias a objetos de tipo Pinacoteca
        self._pinacotecas = pinacotecas

    def ejecutar(self):
        self._leer_de_disco("sgp_bd.txt")

        while True:
            accion = self._menu_general()
            if accion == self.MenuGral.SALIR:
                self._salvar_en_disco("sgp_bd.txt")
                break
            entidad = self._menu_entidades()
            if entidad == self.MenuEntidades.REGRESAR:
                continue
           
            self._controlador(accion, entidad)

    def _controlador(self, accion, entidad):
        if accion == self.MenuGral.ALTAS:
            self._alta(entidad)
        elif accion == self.MenuGral.BAJAS:
            self._baja(entidad)
        elif accion == self.MenuGral.MODIFICACIONES:
            self._modificaciones(entidad)
        elif accion == self.MenuGral.CONSULTAS:
            self._consultas(entidad)
    
    def _alta(self, entidad):
        nombre_clase = entidad.name.title()
        nueva_entidad = getattr(sys.modules[__name__], nombre_clase)
        dicc_atributos = vars(nueva_entidad)
        atributos = [atributo for atributo in dicc_atributos.keys() if not re.match("^__.+__$", atributo)]
        
        print("\nIntroduzca los valores del {}:\n".format(nombre_clase))
        atributo_valor = {}
        for atributo in atributos:
            atributo_valor[atributo] = input("\t{}: ".format(atributo.title()))

        for atributo, valor in atributo_valor.items():
            setattr(nueva_entidad, atributo, valor)
        
        self._agregar_a_lista(nueva_entidad, nombre_clase)

    def _agregar_a_lista(self, objeto, nombre_clase):
        nombre_clase = nombre_clase.lower() + "s"
        self._bd[nombre_clase].append(objeto)

    def _baja(self, entidad):
        pass

    def _modificaciones(self, entidad):
        pass
    
    def _consultas(self, entidad):
        entidad_str = entidad.name.lower() + "s"
        for obj in self._bd[entidad_str]:
            print(str(obj))

    def _menu_general(self):
        seleccion = None
        print("\nMenu de acciones\n")
        while True:
            for elemento_menu in self.MenuGral:
                print("{} - {}".format(elemento_menu.value, elemento_menu.name))
            try:
                seleccion = int(input("Seleccione un opcion: "))
                seleccion = self.MenuGral(seleccion)
                return seleccion
            except EOFError as err:
                print("Programa terminado ... Adios\n")
                break
            except KeyboardInterrupt as err:
                print("Programa terminado ... Adios\n")
                break
            except ValueError as err:
                print("Seleccion incorrecta ... intentelo nuevamente\n")
                continue
            except KeyError as err:
                print("Seleccion incorrecta ... intentelo nuevamente")
                continue
    
    def _menu_entidades(self):
        seleccion = None
        print("\nMenu de entidades\n")
        while True:
            for elemento_menu in self.MenuEntidades:
                print("{} - {}".format(elemento_menu.value, elemento_menu.name))
            try:
                seleccion = int(input("Seleccione una opcion: "))
                seleccion = self.MenuEntidades(seleccion)
                return self.MenuEntidades(seleccion)
            except EOFError as err:
                print("Programa terminado ... Adios\n")
                break
            except KeyboardInterrupt as err:
                print("Programa terminado ... Adios\n")
                break
            except ValueError as err:
                print("Seleccion incorrecta ... intentelo nuevamente\n")
                continue
            except KeyError as err:
                print("Seleccion incorrecta ... intentelo nuevamente\n")
                continue
        return seleccion
    
    def _salvar_en_disco(self, nombre_archivo):
        with open(nombre_archivo, "wb") as archivo:
            pickle.dump(self._bd, archivo)

    def _leer_de_disco(self, nombre_archivo):
        with open(nombre_archivo, "rb") as archivo:
            self._bd = pickle.load(archivo)

    class MenuGral(Enum):
        ALTAS = 1
        BAJAS = 2
        MODIFICACIONES = 3
        CONSULTAS = 4
        SALIR = 5

    class MenuEntidades(Enum):
        CLIENTE = 1
        CUADRO = 2
        ESCUELA = 3
        MECENAS = 4
        PERSONA = 5
        PINACOTECA = 6
        PINTOR = 7
        VENTA = 8
        REGRESAR = 9
