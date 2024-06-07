from clases.Personajes import GalloFortachon, GalloVolador, GalloSabio, Gallina
import sys
from random import randint



def mostrar_inicio():
    """Muestra el menú principal del juego."""
    while True:
        print("\nBienvenido al combate de Gallos")
        print("1. Iniciar Partida")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            iniciar_partida()
        elif opcion == "2":
            finalizar_ejecucion()
        else:
            print("Opción inválida, ingrésela de nuevo...")


def iniciar_partida():
    """Inicia la selección de personajes."""
    while True:
        print("""\nSELECCIONA TU PERSONAJE:
            1. Gallo Fortachón
            2. Gallo Volador
            3. Gallo Sabio
            4. Gallina
            5. Volver al menú principal""")

        opcion = input("Seleccione su personaje: ")
        if opcion == "1":
            gallo_fortachon_instancia.mostrar_info()
            elegir_personaje(gallo_fortachon_instancia)
        elif opcion == "2":
            gallo_volador_instancia.mostrar_info()
            elegir_personaje(gallo_volador_instancia)
        elif opcion == "3":
            gallo_sabio_instancia.mostrar_info()
            elegir_personaje(gallo_sabio_instancia)
        elif opcion == "4":
            gallina_instancia.mostrar_info()
            elegir_personaje(gallina_instancia)
        elif opcion == "5":
            mostrar_inicio()
        else:
            print("Opción inválida, ingrésela de nuevo...")


def finalizar_ejecucion():
    """Finaliza la ejecución del programa."""
    print("\nSaliendo del programa...")
    sys.exit()


def elegir_personaje(jugador):
    """Permite al jugador elegir un personaje y asigna un enemigo aleatorio para el combate.

    Args:
        jugador (Personaje): Instancia del personaje elegido por el jugador.
    """
    while True:
        opcion = input("¿Desea elegir este personaje? (si/no)\n")
        if opcion.lower() == "si":
            enemigo = jugador
            while enemigo == jugador:
                nro_enemigo = randint(1, 4)
                if nro_enemigo == 1:
                    enemigo = gallo_fortachon_instancia
                elif nro_enemigo == 2:
                    enemigo = gallo_volador_instancia
                elif nro_enemigo == 3:
                    enemigo = gallo_sabio_instancia
                else:
                    enemigo = gallina_instancia
            combate(jugador, enemigo)
        elif opcion.lower() == "no":
            iniciar_partida()
        else:
            print("Ingrese una opción correcta...")


def calcular_velocidad(vel_ataque, vel_personaje):
    """Calcula la velocidad del ataque.

    Args:
        vel_ataque (int): Velocidad del ataque.
        vel_personaje (int): Velocidad del personaje.

    Returns:
        int: Velocidad combinada.
    """
    return vel_ataque + vel_personaje


def calcular_dano_inflingido(fuerza_ataque, fuerza_personaje):
    """Calcula el daño infligido en el ataque.

    Args:
        fuerza_ataque (int): Fuerza del ataque.
        fuerza_personaje (int): Fuerza del personaje.

    Returns:
        int: Daño combinado.
    """
    return fuerza_ataque + fuerza_personaje


def combate(jugador, enemigo):
    """Ejecuta el combate entre el jugador y el enemigo.

    Args:
        jugador (Personaje): Instancia del personaje del jugador.
        enemigo (Personaje): Instancia del personaje enemigo.
    """
    print(f"""\t\t\t\tEL COMBATE EMPIEZA
            {jugador.nombre} VS. {enemigo.nombre}""")

    while jugador.vida > 0 and enemigo.vida > 0:
        print(f"""\t\t\t\tVIDA ACTUAL
            JUGADOR (tú): {jugador.nombre} = {jugador.vida}
            ENEMIGO : {enemigo.nombre} = {enemigo.vida}\n""")

        # Cálculos del jugador
        ataque_elegido_jugador = jugador.elegir_ataque()
        velocidad_jugador = calcular_velocidad(ataque_elegido_jugador.velocidad, jugador.velocidad)
        probabilidad_jugador = jugador.probabilidad_esquivar()
        dano_inflingido_jugador = calcular_dano_inflingido(ataque_elegido_jugador.fuerza, jugador.fuerza)

        # Cálculos del enemigo
        ataque_elegido_enemigo = enemigo.ataque_enemigo()
        velocidad_enemigo = calcular_velocidad(ataque_elegido_enemigo.velocidad, enemigo.velocidad)
        probabilidad_enemigo = enemigo.probabilidad_esquivar()
        dano_inflingido_enemigo = calcular_dano_inflingido(ataque_elegido_enemigo.fuerza, enemigo.fuerza)

        if velocidad_enemigo >= velocidad_jugador:
            print(f"\n{enemigo.nombre} ataca con {ataque_elegido_enemigo.nombre} a {jugador.nombre}")
            if probabilidad_jugador:
                print("El jugador ha esquivado el ataque...")
                print(f"\n{jugador.nombre} ataca con {ataque_elegido_jugador.nombre} a {enemigo.nombre}")
                if probabilidad_enemigo:
                    print("El enemigo ha esquivado el ataque")
                else:
                    enemigo.restar_vida(dano_inflingido_jugador)
                    enemigo.vivo_o_muerto(jugador)
            else:
                jugador.restar_vida(dano_inflingido_enemigo)
                jugador.vivo_o_muerto(enemigo)
                print(f"\n{jugador.nombre} ataca con {ataque_elegido_jugador.nombre} a {enemigo.nombre}")
                if probabilidad_enemigo:
                    print("El enemigo ha esquivado el ataque")
                else:
                    enemigo.restar_vida(dano_inflingido_jugador)
                    enemigo.vivo_o_muerto(jugador)
        else:
            print(f"\n{jugador.nombre} ataca con {ataque_elegido_jugador.nombre} a {enemigo.nombre}")
            if probabilidad_enemigo:
                print("El enemigo ha esquivado el ataque")
                print(f"\n{enemigo.nombre} ataca con {ataque_elegido_enemigo.nombre} a {jugador.nombre}")
                if probabilidad_jugador:
                    print("El jugador ha esquivado el ataque...")
                else:
                    jugador.restar_vida(dano_inflingido_enemigo)
                    jugador.vivo_o_muerto(enemigo)
            else:
                enemigo.restar_vida(dano_inflingido_jugador)
                enemigo.vivo_o_muerto(jugador)
                print(f"\n{enemigo.nombre} ataca con {ataque_elegido_enemigo.nombre} a {jugador.nombre}")
                if probabilidad_jugador:
                    print("El jugador ha esquivado el ataque...")
                else:
                    jugador.restar_vida(dano_inflingido_enemigo)
                    jugador.vivo_o_muerto(enemigo)


gallo_fortachon_instancia = GalloFortachon()
gallo_volador_instancia = GalloVolador()
gallo_sabio_instancia = GalloSabio()
gallina_instancia = Gallina()

if __name__ == "__main__":
    mostrar_inicio()
