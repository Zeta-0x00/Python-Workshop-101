# Creación de biblioteca

## Descripción
En este directorio se encuentran los archivos necesarios para la creación de la biblioteca de la práctica.

## Estructura

```yaml
❯ tree mylib
mylib
├── ciclos
│   ├── __init__.py
│   ├── __main__.py
│   └── ciclos.py
├── condicionales
│   ├── __init__.py
│   ├── __main__.py
│   └── demostracion.py
├── matematico
│   ├── __init__.py
│   ├── __main__.py
│   └── aritmetica.py
├── testeable
│   ├── __init__.py
│   ├── __main__.py
│   └── tester.py
├── __init__.py
└── __main__.py

5 directories, 14 files
```

## Contenido
- [ciclos.py](mylib/ciclos/ciclos.py): Contiene las funciones relacionadas con ciclos.
- [demostracion.py](mylib/condicionales/demostracion.py): Contiene las funciones relacionadas con condicionales.
- [aritmetica.py](mylib/matematico/aritmetica.py): Contiene las funciones relacionadas con operaciones matemáticas.
- [tester.py](mylib/testeable/tester.py): Contiene un ejemplo de encapsulamiento basado en POO

## \_\_init__.py
Este archivo es necesario para que Python considere el directorio como un paquete.

No requiere código, pero si se desea se puede agregar.
Ejemplo:
> mylib/ciclos/\_\_init__.py
```python
from .ciclos import *
```


## \_\_main__.py
Este archivo nos permite invocar el módulo desde línea de comandos con el argumento `-m`, ya que le otorga una funcionalidad por defecto (lo ideal es que para hacer la funcionalidad interactiva creemos un menu de ejecución en este archivo).
Ejemplo:
> mylib/\_\_main__.py
```python
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

```

## Uso

```python
from mylib.ciclos import ciclos

ciclos.ciclo_while_true()
```

## Creación (Compilación)

### Creación Entorno virtual

```bash
❯ python -m venv venv
❯ source venv/bin/activate
```

### Requerimientos

```bash
❯ pip install setuptools build twine
```

### setup.py

```python
#!/usr/local/bin/python
#-*- coding: utf-8 -*-

from setuptools import setup  # type: ignore

setup(
    name="mylib",
    version="0.0.1",
    packages=["mylib"],  # Lista de paquetes a incluir
    python_requires=">=3.12",
    author="Z",
    description="mylib",
    url="https://hawksec-academy.com/"
)
```
Si contemplamos la ubicación deberíamos tener la siguiente estructura:

```bash
❯ ls
mylib  setup.py  venv
```

el venv es el entorno virtual que creamos anteriormente, por lo que podemos ignorarlo.

### Creación de la biblioteca

```bash
❯ python -m build
...
Successfully built mylib-0.0.1.tar.gz and mylib-0.0.1-py3-none-any.whl
```

### Instalación de la biblioteca

```bash
❯ pip install dist/mylib-0.0.1-py3-none-any.whl
Processing ./dist/mylib-0.0.1-py3-none-any.whl
Installing collected packages: mylib
Successfully installed mylib-0.0.1
```

Con la bilioteca instalada deberíamos no solo de ser capaces de usarla desde un archivo `.py` sino también desde la terminal usando el argumento `-c` que permite ejecutar código y el `-m` que permite ejecutar un módulo.

> Usando `-m` como argumento para ejecutar el módulo
```bash
❯ python -m mylib
La suma entre 5 y 78 es igual a 83
Hello World!
	I'm __main__ from mylib
Nombre del objeto __main__ from mylib
❯ python -m mylib.testeable
Hello World!
	I'm __main__ in testeable
```

> Usando `-c` como argumento para ejecutar código
```bash
❯ python -c "from mylib import matematico; print(matematico.aritmetica.sumar(55, 234))"
289
```

### Desinstalación de la biblioteca

```bash
❯ pip uninstall mylib
```

### Desactivar entorno virtual

```bash
❯ deactivate
```

## Publicar en PyPi
Si fuera el caso que se desea publicar la biblioteca en los respositorios de PyPi, se deberá seguir los siguientes pasos:

- Una vez compilada la biblioteca, se deberá crear una cuenta en [PyPi](https://pypi.org/account/register/).

> Se publicará la biblioteca con el nombre `mylib` que está contenida en el directorio `dist` (la versión compilada con `build`)
> Para esto se usará `twine` que es un paquete que permite subir paquetes a PyPi.

```bash
❯ twine upload dist/*
```
Después de ejecutar el comando simplemente habrá que proporcioar las credenciales de la cuenta de PyPi y listo, la biblioteca estará disponible para ser instalada desde cualquier parte del mundo con el comando `pip install mylib`.