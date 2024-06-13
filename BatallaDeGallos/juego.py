import personajes
from personajes.personaje import GalloFortachon, GalloVolador, GalloSabio, Gallina
from personajes.controlable import Jugador, Enemigo, Controlable
import ataques
from ataques.ataque import Ataque
import sys

class Juego:
    def mostrar_inicio(self):
        """Muestra el menú de inicio y espera que el usuario elija una opción válida."""
        print("""BIENVENIDOS A LA BATALLA DE GALLOS
                    1. Jugar Modo Historia
                    2. Jugar Una Ronda
                    3. Salir del programa""")
        while True:
            opcion = input("Elija una opción: ")
            if opcion in ["1", "2", "3"]:
                return opcion
            else:
                print("Opción inválida, ingrese nuevamente...")

    def iniciar_partida(self, opcion_menu, usr_name: str) -> None:
        """Inicia la partida según la opción del menú y el nombre de usuario.

        Args:
            opcion_menu (str): Opción seleccionada por el usuario ("1", "2", "3", "4" o "5").
            usr_name (str): Nombre del usuario ingresado.
        """
        while True:
            lista_personajes = [GalloFortachon(), GalloVolador(), GalloSabio(), Gallina()]
            if usr_name == " ":
                usr_name = input("Ingrese su Nombre: ")
            instancia_jugador = Jugador(usr_name, lista_personajes[0], 0)
            i = 0
            print(f"""MENU DE PERSONAJES:""")
            while i < 4:
                print(f"""      {i + 1}. {lista_personajes[i].nombre}: {lista_personajes[i].descripcion}""")
                i += 1
            print(f"""      5. Volver al inicio """)
            opcion = input("Seleccione una opción: ")
            if opcion in ["1", "2", "3", "4"]:
                jugador = instancia_jugador.seleccionar_personaje(usr_name, int(opcion) - 1)
                if jugador is None:
                    self.iniciar_partida(opcion, usr_name)
                    break
                print(f"""\t\t\t\t{jugador.usr_name} ES {jugador.nombre}""")
                if opcion_menu == "1":
                    self.jugar_rondas(jugador)
                else:
                    self.jugar_una_ronda(jugador)
            elif opcion == "5":
                valor = self.mostrar_inicio()
                if valor:
                    self.iniciar_partida(usr_name)
                else:
                    self.finalizar_ejecucion()
            else:
                print("Opción inválida, seleccione de nuevo...")

    def jugar_una_ronda(self, jugador: Jugador) -> None:
        """Juega una sola ronda del juego.

        Args:
            jugador (Jugador): Jugador que participa en la ronda.
        """
        lista_personajes = [GalloFortachon(), GalloVolador(), GalloSabio(), Gallina()]
        instancia_enemigo = Enemigo(lista_personajes[0], 0)
        enemigo = instancia_enemigo.seleccionar_personaje(jugador)
        i = self.combate(jugador, enemigo, 0)
        self.finalizar_ejecucion()

    def jugar_rondas(self, jugador: Jugador) -> None:
        """Juega múltiples rondas del juego, enfrentando al jugador con diferentes enemigos.

        Args:
            jugador (Jugador): Jugador que participa en las rondas.
        """
        lista_personajes = [GalloFortachon(), GalloVolador(), GalloSabio(), Gallina()]
        i = 0
        j = 1
        while i < len(lista_personajes):
            if lista_personajes[i].nombre == jugador.nombre:
                i += 1
                continue  # Saltar la iteración si el personaje es el mismo que el del jugador
            else:
                input(f"\t\t\t\tINICIAR RONDA {j}\nPresione ENTER para continuar")
                enemigo = Enemigo(lista_personajes[i], 0)
                i = self.combate(jugador, enemigo, i)
                jugador.restablecer_vida()  # Restablecer la vida del jugador después de cada combate
                j += 1
                if j == 4:
                    print("\n \t\t\tHAS COMBATIDO A TODOS LOS ENEMIGOS")
                else:
                    print("\n\t\t\t\tFIN DE ESTA RONDA\n")
        self.finalizar_ejecucion()

    def combate(self, jugador: Controlable, enemigo: Controlable, i: int) -> int:
        """Simula un combate entre un jugador y un enemigo.

        Args:
            jugador (Controlable): Jugador que participa en el combate.
            enemigo (Controlable): Enemigo contra el que el jugador está luchando.
            i (int): Índice actual del enemigo en la lista de personajes.

        Returns:
            int: Nuevo índice actualizado del enemigo en la lista de personajes.
        """
        controlable = Controlable(" ", " ", 0, 0, 0, 0, [], 0)
        print(f"""\t\t\t\tEL COMBATE EMPIEZA
                {jugador.usr_name} VS. {enemigo.nombre}""")

        while jugador.vida > 0 and enemigo.vida > 0:
            print(f"""\t\t\t\tVIDA ACTUAL
                JUGADOR (tú): {jugador.usr_name} = {jugador.vida}
                ENEMIGO : {enemigo.nombre} = {enemigo.vida}\n""")
            # Calculos Jugador
            ataque_jugador = jugador.seleccionar_ataque()
            velocidad_jugador = jugador.calcular_velocidad(ataque_jugador.velocidad, jugador.velocidad)
            # Calculos Enemigo
            ataque_enemigo = enemigo.seleccionar_ataque()
            velocidad_enemigo = enemigo.calcular_velocidad(ataque_enemigo.velocidad, enemigo.velocidad)

            # Determina quién ataca primero basado en la velocidad calculada
            if velocidad_jugador >= velocidad_enemigo:
                controlable_primero = jugador
                ataque_primero = ataque_jugador
                controlable_segundo = enemigo
                ataque_segundo = ataque_enemigo
            else:
                controlable_primero = enemigo
                ataque_primero = ataque_enemigo
                controlable_segundo = jugador
                ataque_segundo = ataque_jugador

            # Realiza los ataques y maneja la lógica del combate
            esquivar_primero = controlable.probabilidad_esquivar(controlable_primero)
            danho_primero = controlable.calcular_dano_inflingido(ataque_primero.fuerza, controlable_primero.fuerza)

            esquivar_segundo = controlable.probabilidad_esquivar(controlable_segundo)
            danho_segundo = controlable.calcular_dano_inflingido(ataque_segundo.fuerza, controlable_segundo.fuerza)

            # Procesa los ataques y verifica si alguien ha perdido la vida
            if not esquivar_segundo:
                controlable_segundo.restar_vida(danho_primero)
                if controlable_segundo.vivo_o_muerto(controlable_primero):
                    if controlable_segundo.nombre == jugador.nombre:
                        print("\t\t\t\tHAS PERDIDO")
                        self.finalizar_ejecucion()
                    else:
                        break
            else:
                print(f"{controlable_segundo.nombre} ha esquivado el ataque")

            if not esquivar_primero:
                controlable_primero.restar_vida(danho_segundo)
                if controlable_primero.vivo_o_muerto(controlable_segundo):
                    if controlable_primero.nombre == jugador.nombre:
                        print("\t\t\t\tHAS PERDIDO")
                        self.finalizar_ejecucion()
                    else:
                        break
            else:
                print(f"{controlable_primero.nombre} ha esquivado el ataque")
        return i + 1

    def finalizar_ejecucion(self):
        """Finaliza la ejecución del programa."""
        print("\nSaliendo del programa...")
        sys.exit()
