"""
Name 
    SGP: Sistema Gestor de Pinacotecas

Description
    El Sistema Gestor de Pinacotecas ayuda a gestionar la administración de diferentes
    pinacotecas. Principalmente la gestión de de cuadros, pintores, mecenas, clientes,
    escuelas, maestros y ventas.
"""

import Pinacoteca
import Persona
from Pintor import Pintor

WELLCOME_HEADER = "Sistema Gestor de Pinacotecas"
INSTRUCTION = "Por favor seleccione una de las siguientes opciones:"


def main():
    print("{header:^100}".format(header=WELLCOME_HEADER))
    print("{instruction}".format(instruction=INSTRUCTION))

    pinacoteca_obj = Pinacoteca.Pinacoteca("Galeria UDG", "Blvd. Gral. Marcelino García Barragán 1421", "Guadalajara", 12, 20)
    print(pinacoteca_obj)
    print(pinacoteca_obj._nombre)

   
if __name__ == "__main__":
    main()