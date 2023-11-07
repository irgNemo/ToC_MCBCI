"""
Name 
    Pinacotecas

Description
    The pinacotecas system allow the managment of mexican pinacotecas
"""

import Pinacoteca
import Persona
from Pintor import Pintor

WELLCOME_HEADER = "PINACOTECAS MANAGMENT PROGRAM"
INSTRUCTION = "Please select any of the following optiones:"


def main():
    print("{header:^100}".format(header=WELLCOME_HEADER))
    print("{instruction}".format(instruction=INSTRUCTION))

    pinacoteca_obj = Pinacoteca.Pinacoteca()
    pinacoteca_obj.nombre = "Mi pinoteca"
    print(pinacoteca_obj)
    print(pinacoteca_obj._nombre)

    persona_obj = Persona.Persona()
    persona_obj.nombre = "Israel Roman"

    pintor_obj = Pintor()
    pintor_obj = "Juan perez"
    print(pintor_obj)

    pintor2_obj = Pintor(nombre = "Jose Clemente Orizco")
    print(pintor2_obj)


if __name__ == "__main__":
    main()