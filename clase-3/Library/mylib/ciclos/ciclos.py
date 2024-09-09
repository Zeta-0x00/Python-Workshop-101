#!/usr/local/bin/python
#-*- coding: utf-8 -*-

numeros: list[int] = [1, 2, 3, 4, 5]

def ciclo_while() -> None:
    print("Usando un bucle while:".center(80, "="))
    print("""codigo:\n\t\tnumeros: list[int] = [1, 2, 3, 4, 5]\n\t\tindice: int = 0\n\t\twhile indice < len(numeros):  # len() devuelve el largo del iterable
\n\t\t\tprint(f"Procesando números: {numeros[indice]}")\n\t\t\tindice += 1\nResultados:\n----------""")
    indice: int = 0
    while indice < len(numeros):  # len() devuelve el largo del iterable
        print(f"Procesando números: {numeros[indice]}")
        indice += 1

def ciclo_for() -> None:
    print("Usando un bucle for con rango:".center(80, "="))
    print("""codigo:\n\t\tnumeros: list[int] = [1, 2, 3, 4, 5]\n\t\tindice: int = 0\n\t\tfor i in range(len(numeros)):  # len() devuelve el largo del iterable\n\t\t\tprint(f"Procesando número en índice {i}: {numeros[i]}")\nResultados:\n----------""")
    for i in range(len(numeros)):  # len() devuelve el largo del iterable
        print(f"Procesando número en índice {i}: {numeros[i]}")



def ciclo_while_true() -> None:
    print("Usando un bucle while True:".center(80, "="))
    print("""codigo:\n\t\tnumeros: list[int] = [1, 2, 3, 4, 5]\n\t\tindice: int = 0\n\t\twhile True:\n\t\t\tif indice >= len(numeros):\n\t\t\t\tbreak\n\t\t\tprint(f"Procesando números: {numeros[indice]}")\n\t\t\tindice += 1\nResultados:\n----------""")
    indice: int = 0
    while True:
        if indice >= len(numeros):
            break
        print(f"Procesando números: {numeros[indice]}")
        indice += 1

def ciclo_foreach() -> None:
    print("Usando un bucle for: (foreach en cualquier otro lenguaje)".center(80, "="))
    print("""codigo:\n\t\tnumeros: list[int] = [1, 2, 3, 4, 5]\n\t\tfor numero in numeros:\n\t\t\tif numero % 2 == 0:  # División modular (%)\n\t\t\t\tprint(f"{numero} es par")\n\t\t\telse:\n\t\t\t\tprint(f"{numero} es impar")\nResultados:\n----------""")
    for numero in numeros:
        if numero % 2 == 0:  # División modular (%)
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")





if __name__ == "__main__":
    ciclo_while()
    print("\n\n")
    ciclo_while_true()
    print("\n\n")
    ciclo_for()
    print("\n\n")
    ciclo_foreach()
