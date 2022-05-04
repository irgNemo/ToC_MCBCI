def main():
    entero = 6
    lista = [2,4,6]
    print("lista antes: " + str(id(lista)))
    print("entero antes: " + str(id(entero)))
    f(lista, entero)
    print(lista)
    print(entero)



def f(lista: list, elemento: int):
    elemento = 2
    lista.append(6)
    print("lista despues: " + str(id(lista)))
    print("entero despues: " + str(id(elemento)))

main()