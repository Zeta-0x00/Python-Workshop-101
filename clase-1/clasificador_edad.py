#!/usr/local/bin/python
#-*- coding: utf-8 -*-
def clasificar_edad(edad: int) -> str:
    """
    Clasifica a una persona en una categoría de edad basada en su edad cronológica.

    Parameters
    ----------
    edad : int
        La edad de la persona a clasificar. Debe ser un entero positivo.

    Returns
    -------
    str
        Una cadena que describe la categoría de edad:
        - "niño" para edades menores a 12 años.
        - "adolescente" para edades de 12 a 17 años.
        - "adulto" para edades de 18 a 64 años.
        - "adulto mayor" para edades de 65 años o más.

    Examples
    --------
    >>> clasificar_edad(10)
    'niño'

    >>> clasificar_edad(15)
    'adolescente'

    >>> clasificar_edad(30)
    'adulto'

    >>> clasificar_edad(70)
    'adulto mayor'
    """
    if edad < 0:
        raise ValueError("La edad debe ser un entero positivo.")
    if edad < 12:
        return "niño"
    elif edad < 18:
        return "adolescente"
    elif edad < 65:
        return "adulto"
    else:
        return "adulto mayor"

if __name__ == "__main__":
    print(f"La edad es {(a := 29)} por lo que nuestro individuo es {clasificar_edad(a)}")
