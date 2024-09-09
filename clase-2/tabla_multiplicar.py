def tabla_multiplicar(numero: int) -> None:
    """
    Imprime la tabla de multiplicar del número ingresado.

    Parameters:
    -----------
    numero : int
        Número entero del cual se desea conocer la tabla de multiplicar.

    Returns:
    --------
    None

    Example:
    --------
    numero = 7
    tabla_multiplicar(numero)
    """
    for i in range(1, 11): # Tabla de multiplicar del 1 al 10
        print(f"{numero} x {i:2} = {numero * i:2}")  # f-string {i:2} para alinear a la derecha



if __name__ == "__main__":
    try:
        i = int(input("Ingrese la tabla que desea consultar:\n> "))
        tabla_multiplicar(i)
    except:
        print("Ingresaste algo que no es un número entero...")
    finally:
        print("¡Hasta luego!")
