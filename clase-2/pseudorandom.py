#!/usr/bin/python
#-*- coding: utf-8 -*-

def generador_pseudo_aleatorio(seed: int) -> int:
    """
    Genera un número pseudoaleatorio a partir de una semilla.

    Parámetros:
    ----------
    seed : int
        Semilla para el generador de números pseudoaleatorios.

    Returns:
    --------
    int
        Número pseudoaleatorio generado a partir de la semilla.

    Example:
    --------
    seed = 42
    for _ in range(10):
        seed = generador_pseudo_aleatorio(seed)
        print(seed)
    """
    if not seed:
        return -1
    a: int = 1103515245
    c: int = 12345
    m: int = 2**31
    seed = (a * seed + c) % m
    return seed

generador = lambda x: (x* 1103515245 + 12345) % 2**31

if __name__ == "__main__":
    #x: int = generador_pseudo_aleatorio(45)
    #print(f"Número aleatorio (normal) es: {x}")
    #print(f"Número aleatorio (lambda) es: {generador(45)}")
    seed = 42
    for _ in range(10):
        seed = generador_pseudo_aleatorio(seed)
        print(seed)