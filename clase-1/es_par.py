#!/usr/local/bin/python
#-*- coding: utf-8 -*-
def verificar_paridad(numero: int) -> str:
    """
    Determina la paridad de un número entero, clasificándolo como "par" o "impar".

    Parameters
    ----------
    numero : int
        El número entero cuya paridad se va a verificar.

    Returns
    -------
    str
        Una cadena que indica si el número es:
        - "par" si el número es divisible por 2 sin residuo.
        - "impar" si el número no es divisible por 2 sin residuo.

    Examples
    --------
    >>> verificar_paridad(10)
    'par'

    >>> verificar_paridad(7)
    'impar'

    >>> verificar_paridad(0)
    'par'
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"


if __name__ == "__main__":
    print(f"Nuestro número a evaluar es {(a := 165415136122423)} el cual es {verificar_paridad(a)}")
