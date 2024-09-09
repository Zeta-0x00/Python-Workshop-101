#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-

a: int = 10
b: bool = (a == 5) #Debería ser False
c: str = f'format string y \'a\' posee el valor de {a}'
d: str = r'Esto es un raw string \' \t no debería tener \\ problema por \n los backslash lo pillas?'
f: object = type(b); e: str = 'String normal y\n el \\ b\'ackslash trae\t problemas'

print(a)
print(b)
print(c)
print(d)
print(e)

print('Format string estilo C para saber si el tipo de dato de b %s y su valor %s' % (f, b))



