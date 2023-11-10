from enum import Enum

class Sgp:

    def __init__(self) -> None:
        pass

    def ejecutar(self):
        self.menu_general()

    def menu_general(self):
        seleccion = None
        print("Menu de acciones:")
        while True:
            for elemento_menu in self.MenuGral:
                print("{} - {}".format(elemento_menu.value, elemento_menu.name))
            seleccion = input("Seleccione un opcion: ")                         
            if seleccion == self.MenuGral.SALIR.value:
                break
        return seleccion
    
    def menu_entidades(self):
        seleccion = None
        print("Menu de entidades\n")
        while True:
            for elemento_menu in self.MenuEntidades:
                print("{} - {}".format(elemento_menu.value, elemento_menu.name))
            seleccion = input("Seleccione una opcion:")
            if seleccion == self.MenuEntidades.SALIR:
                break

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
        PINOTECA = 6
        PINTOR = 7
        VENTA = 8
        SALIR = 9
