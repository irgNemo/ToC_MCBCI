#! /usr/bin/env python

def main():
    valores = pedir_datos("Introduce un valor entero o flotante; o ^D para terminar: ")
    media = promedio(valores)
    ds = desviacion_estandar(valores, media)
    print("\nPromedio: ", media, " Desviacion estandar: ", ds)

def promedio(lista):
    sumatoria = 0.0
    for valor in lista:
        sumatoria += valor
    
    return sumatoria / len(lista)


def desviacion_estandar(lista, media):
    sumatoria = 0
    for valor in lista:
        sumatoria += (valor - media)**2
    
    return (sumatoria / (len(lista)))**(1/2)

def pedir_datos(mensaje):
    lista = []
    valor = None
    while True:
        try:
            valor = input(mensaje)
            valor = float(valor)
        except EOFError as err:
            break   
        except ValueError as err:
            print("Solo se aceptan valores enteros o flotantes")
            continue
                
        lista.append(valor)
    
    return lista


if __name__ == "__main__":
    main()


