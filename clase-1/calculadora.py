#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def Calculadora(num1: int | float, num2: int | float,
                operation: str) -> int | float:
    """
        Calculate 2 numbers with the operation given
    args
    ----
        num1:  int | float
            number 1
        num2:  int | float
            number 2
        operation:  str
            operation to do
    return
    ------
        result: int | float
                Result of the operation
    example
    -------
            Calculadora(5,2,"*")
    """
    match operation:
        case "+":
            return addition(num1, num2)
        case "-":
            return substraction(num1, num2)
        case "*":
            return multiplication(num1, num2)
        case "/":
            return division(num1, num2)
        case _:
            print(f"Operation out of oscope!\n\t{operation=}")
            return -1

def division(n: int | float, m: int | float) -> float:
    """
        Divide 2 numbers and return the result
    args
    ----
        n:  int | float
            number 1
        m:  int | float
            number 2
    return
    ------
        result: float
                Division result
    example
    -------
            division(5,0)
    """
    result: float = -1.0
    try:
        result = n / m
        print(f"División = {result:.3f}")
    except ZeroDivisionError as err:
        print(f"Error: {err}")
    finally:
        return result

def addition(n: int | float, m: int | float) -> int | float:
    """
        Add 2 numbers and return the result
    args
    ----
        n:  int | float
            number 1
        m:  int | float
            number 2
    return
    ------
        result: int | float
                Addition result
    example
    -------
            addition(5,2)
    """
    result: int | float = n + m
    print(f"Suma = {result}")
    return result

def substraction(n: int | float, m: int | float) -> int | float:
    """
        Substract 2 numbers and return the result
    args
    ----
        n:  int | float
            number 1
        m:  int | float
            number 2
    return
    ------
        result: int | float
                Substraction result
    example
    -------
            substraction(5,2)
    """
    result: int | float = n - m
    print(f"Resta = {result}")
    return result

def multiplication(n: int | float, m: int | float) -> int | float:
    """
        Multiply 2 numbers and return the result
    args
    ----
        n:  int | float
            number 1
        m:  int | float
            number 2
    return
    ------
        result: int | float
                Multiplication result
    example
    -------
            multiplication(5,2)
    """
    result: int | float = n * m
    print(f"Multiplicación = {result}")
    return result

if __name__ == "__main__":
    x: int | float = Calculadora(5,2,"/")
    print(f"{x=}")
    # help(division)
    

