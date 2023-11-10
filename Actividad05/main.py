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
    print("\n{header:^100}\n".format(header=WELLCOME_HEADER))

    sgp = Sgp()
    sgp.ejecutar()

   
if __name__ == "__main__":
    main()