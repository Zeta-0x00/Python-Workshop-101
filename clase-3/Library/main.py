#!/usr/local/bin/python
#-*- codng: utf-8 -*-

from mylib import matematico, testeable
from sys import argv as get

if len(get) != 3:
    raise IndexError("Error, The first and second arguments for adition operation are mandatory!")

if __name__ == "__main__":
    first: int = int(get[1].strip()) if get[1].isdigit() else (lambda: 0,(_ for _ in ()).throw(ValueError(f"The argument {get[1]} must be an integer")))  # type: ignore
    second: int = int(get[2].strip()) if get[2].isdigit() else (lambda: 0,(_ for _ in ()).throw(ValueError(f"The argument {get[2]} must be an integer")))  # type: ignore
    print("La suma entre %s y %s es igual a %s" % (first,
                                                   second,
                                                   matematico.aritmetica.sumar(first, second)))
    t: testeable.tester = testeable.tester("Z - Test")
    t.sayHi()
    print("Nombre del objeto {a}".format(a=t.name))

