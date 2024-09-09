from pseudorandom import generador_pseudo_aleatorio

def adivina_el_numero(seed: int) -> None:
    """
    Juego para adivinar un número generado aleatoriamente.

    Parameters:
    -----------
    seed: int
        Semilla para el generador pseudo-ale

    Returns:
    --------
    None

    Example:
    --------
    adivina_el_numero()
    Adivina el número (entre 1 y 10): 5
    Más bajo
    Adivina el número (entre 1 y 10): 8
    Más alto
    Adivina el número (entre 1 y 10): 266074466564
    Más bajo
    Adivina el número (entre 1 y 10): 266074466
    ¡Correcto!
    """
    numero_secreto: int = generador_pseudo_aleatorio(seed=seed)
    intento = None
    while intento != numero_secreto:
        try:
            intento = int(input("Adivina el número: "))
            if intento < numero_secreto:
                print("Más alto")
            elif intento > numero_secreto:
                print("Más bajo")
        except ValueError as err:
            print(f"Error: {err}")
            print("Por favor, ingresa un número entero")
    print("¡Correcto!")


if __name__ == "__main__":
    adivina_el_numero(45)
