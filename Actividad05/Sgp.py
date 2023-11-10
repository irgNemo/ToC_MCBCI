from enum import Enum

class Sgp:
    MENU_CLASES = enumerate(["Cliente", "Cuadro", "Escuela", "Mecenas", "Persona", "Pinoteca", "Pintor", "Venta"])

    def __init__(self) -> None:
        pass

    def menu_general(self):
        for val, name in MenuGral:
            print(val)

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
