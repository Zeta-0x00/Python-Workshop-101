#!/usr/local/bin/python
#-*- coding: utf-8 -*-

from typing import Callable

def sumar(a: int, b: int) -> int:
    """Suma dos números enteros"""
    return a + b

def restar(a: int, b: int) -> int:
    """Resta dos números enteros"""
    return a - b

cuadrado: Callable[[int], int] = lambda x: x*x

if __name__ == "__main__":
    print(f"La suma de {(a := 3)} y {(b := 5)} es igual a {sumar(a,b)}")
    print(f"La resta entre {(c := 30)} y {(d := 13)} es igual a {restar(c, d)}")
    print(f"El cuadrado de {(e := 5)} es igual a {cuadrado(e)}")
