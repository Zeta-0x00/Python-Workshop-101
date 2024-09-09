#!/usr/local/bin/python
#-*- coding: utf-8 -*-

from typing import Callable

def invertir_cadena_v1(cadena: str) -> str:
	"""
	Invierte una cadena de texto.
	Parameters:
	-----------
		cadena: str
		Cadena de texto a invertir.
	Returns:
	--------
		str
		Cadena de texto invertida.
	Example:
	--------
		invertir_cadena("Hola")
		aloH
	"""
	return cadena[::-1]
invertir_cadena_v2: Callable[[str], str] = lambda cadena: cadena[::-1]

if __name__ == "__main__":
	print(invertir_cadena_v1("Hola"))
	print(invertir_cadena_v2("Hola"))
	print(invertir_cadena_v1("Python"))
	print(invertir_cadena_v2("Python"))
	print(invertir_cadena_v1("¡Hola, mundo!"))
	print(invertir_cadena_v2("¡Hola, mundo!"))