"""
Name 
    SGP: Sistema Gestor de Pinacotecas

Description
    El Sistema Gestor de Pinacotecas ayuda a gestionar la administración de diferentes
    pinacotecas. Principalmente la gestión de de cuadros, pintores, mecenas, clientes,
    escuelas, maestros y ventas.
"""

from Sgp import Sgp


WELLCOME_HEADER = "Sistema Gestor de Pinacotecas"
INSTRUCTION = "Por favor seleccione una de las siguientes opciones:"

def main():
    print("{header:^100}".format(header=WELLCOME_HEADER))
    print("{instruction}".format(instruction=INSTRUCTION))

    sgp = Sgp()
    sgp.menu_general()

   
if __name__ == "__main__":
    main()