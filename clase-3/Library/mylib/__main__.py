#!/usr/local/bin/python
#-*- codng: utf-8 -*-

from mylib import matematico, testeable

if __name__ == "__main__":
	print("La suma entre %s y %s es igual a %s" % (5,
                                                   78,
                                                   matematico.aritmetica.sumar(5, 78)))
	t: testeable.tester = testeable.tester("__main__ from mylib")
	t.sayHi()
	print("Nombre del objeto {a}".format(a=t.name))

