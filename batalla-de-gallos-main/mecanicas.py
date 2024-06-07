def calcular_velocidad(velocidad_ataque, velocidad_jugador):
    """Calcula la velocidad combinada del ataque y el jugador.

    Args:
        velocidad_ataque (int): Velocidad del ataque.
        velocidad_jugador (int): Velocidad del jugador.

    Returns:
        int: Velocidad combinada.
    """
    return (velocidad_ataque + velocidad_jugador) / 2


def calcular_dano_inflingido(fuerza_ataque, fuerza_personaje):
    """Calcula el daño infligido por el ataque.

    Args:
        fuerza_ataque (int): Fuerza del ataque.
        fuerza_personaje (int): Fuerza del personaje.

    Returns:
        int: Daño infligido.
    """
    return int(((fuerza_ataque * 1.5) / 2) * (fuerza_personaje / 2))
