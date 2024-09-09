#!/usr/local/bin/python
# _*_ coding: utf-8 _*_

def contar_vocales(palabra: str) -> tuple[int, dict[str, int]]:
    """
    Cuenta la cantidad de vocales en una palabra.
    
    Parameters:
    -----------
    palabra : str
        Palabra de la cual se desea contar las vocales.
        
    Returns:
    --------
    tuple[0] : int
        Cantidad de vocales en la palabra.
    tuple[1] : dict[str, int]
        Vocal por cantidad de apariciones
        formato clave-valor de diccionario
    
    Example:
    --------
    palabra = "Hola"
    contar_vocales(palabra)
    """
    vocales = "aeiouAEIOU"
    contador = 0
    result: dict[str, int] = {}
    for letra in vocales:
        if letra in palabra:
            result[letra] = palabra.count(letra)
            contador += result.get(letra)
    return contador, result


if __name__ == "__main__":
    result: tuple = contar_vocales(input("Ingrese la palabra:\n>>> "))
    print("La palabra tiene un total de %s vocales\nSe reparten de la siguiente manera:\n%s\n%s" % (result[0],f"{'-'*35}", "\n".join([f'{k}:  {val}' for k, val in result[1].items() ] ) ))
