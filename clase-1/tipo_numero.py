#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def tipo_de_numero(numero: int) -> str:
    """
    Determina el tipo de número dado, clasificándolo como "positivo", "negativo" o "cero".

    Parameters
    ----------
    numero : int
        El número entero a clasificar.

    Returns
    -------
    str
        Una cadena que indica si el número es:
        - "positivo" si el número es mayor que cero.
        - "negativo" si el número es menor que cero.
        - "cero" si el número es igual a cero.

    Examples
    --------
    >>> tipo_de_numero(10)
    'positivo'

    >>> tipo_de_numero(-5)
    'negativo'

    >>> tipo_de_numero(0)
    'cero'
    """
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

if __name__ == "__main__":
    print(f"Numero a evaluar {(a := -123)} por lo que es {tipo_de_numero(a)}")
