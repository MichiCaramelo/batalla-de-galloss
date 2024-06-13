from abc import ABC, abstractmethod
from random import randint
from personajes.personaje import GalloFortachon, GalloVolador, GalloSabio, Gallina

class Controlable():
    def __init__(self, nombre, descripcion, vida, fuerza, velocidad, iq, ataques, puntos_experiencia):
        """Inicializa un personaje controlable con sus atributos.

        Args:
            nombre (str): Nombre del personaje.
            descripcion (str): Descripción del personaje.
            vida (int): Puntos de vida del personaje.
            fuerza (int): Nivel de fuerza del personaje.
            velocidad (int): Nivel de velocidad del personaje.
            iq (int): Nivel de inteligencia del personaje.
            ataques (list): Lista de objetos de tipo Ataque disponibles para el personaje.
            puntos_experiencia (int): Puntos de experiencia del personaje.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.vida = int(vida)
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.iq = iq
        self.ataques = ataques
        self.puntos_experiencia = puntos_experiencia

    @abstractmethod
    def seleccionar_personaje(self, *args, **kwargs):
        """Método abstracto para seleccionar un personaje."""
        pass

    @abstractmethod
    def seleccionar_ataque(self, personaje):
        """Método abstracto para seleccionar un ataque."""
        pass

    def calcular_velocidad(self, velocidad_ataque, velocidad_jugador):
        """Calcula la velocidad promedio entre un ataque y el personaje para determinar quién ataca primero.

        Args:
            velocidad_ataque (int): Velocidad del ataque.
            velocidad_jugador (int): Velocidad del personaje.

        Returns:
            float: Velocidad promedio.
        """
        return (velocidad_ataque + velocidad_jugador) / 2

    def probabilidad_esquivar(self, jugador):
        """Calcula la probabilidad de esquivar un ataque basado en el IQ del personaje.

        Args:
            jugador (Controlable): Personaje que va a intentar esquivar.

        Returns:
            bool: True si el personaje esquiva el ataque, False si no.
        """
        probabilidad = jugador.iq * 5
        nro = randint(1, 100)
        return nro < probabilidad

    def calcular_dano_inflingido(self, fuerza_ataque, fuerza_personaje):
        """Calcula el daño infligido por un ataque en relación con la fuerza del personaje.

        Args:
            fuerza_ataque (int): Fuerza del ataque.
            fuerza_personaje (int): Fuerza del personaje.

        Returns:
            int: Daño infligido al personaje.
        """
        return int(((fuerza_ataque * 1.5) / 2) * (fuerza_personaje / 2))

    def restar_vida(self, danho):
        """Resta puntos de vida al personaje.

        Args:
            danho (int): Cantidad de vida a restar.
        """
        print(f"{self.nombre} pierde {danho} de vida")
        self.vida -= danho

    def vivo_o_muerto(self, personaje):
        """Verifica si el personaje está vivo o muerto.

        Args:
            personaje (Controlable): Personaje contra el que se evalúa la vida.

        Returns:
            bool: True si el personaje ha muerto, False si está vivo.
        """
        if self.vida <= 0:
            print(f"\t\t\t{self.nombre} se ha quedado sin vida :c\n"
                  f"\t\t\t{personaje.nombre} HA GANADO")
            return True
        return False


class Jugador(Controlable):
    def __init__(self, usr_name, personaje, puntos_experiencia):
        """Inicializa un jugador con su nombre de usuario, basado en un personaje elegido.

        Args:
            usr_name (str): Nombre de usuario del jugador.
            personaje (Controlable): Personaje seleccionado por el jugador.
            puntos_experiencia (int): Puntos de experiencia inicial del jugador.
        """
        super().__init__(personaje.nombre, personaje.descripcion, personaje.vida, personaje.fuerza, personaje.velocidad, personaje.iq, personaje.ataques, puntos_experiencia)
        self.usr_name = usr_name
        self.vida_inicial = personaje.vida

    def seleccionar_personaje(self, usr_name, opcion):
        """Permite al jugador seleccionar un personaje de la lista y confirmar su elección.

        Args:
            usr_name (str): Nombre de usuario del jugador.
            opcion (int): Índice del personaje seleccionado en la lista.

        Returns:
            Jugador: Jugador creado con el personaje seleccionado.
        """
        lista_personajes = [GalloFortachon(), GalloVolador(), GalloSabio(), Gallina()]
        lista_personajes[opcion].mostrar_info()
        while True:
            opcion_confirmacion = input("¿Desea elegir este personaje? (si/no): ")
            if opcion_confirmacion.lower() == "si":
                jugador = Jugador(usr_name, lista_personajes[opcion], 0)
                return jugador
            elif opcion_confirmacion.lower() == "no":
                return None
            else:
                print("Ingrese una opción correcta...")

    def seleccionar_ataque(self):
        """Permite al jugador seleccionar un ataque de su lista de ataques disponibles.

        Returns:
            Ataque: Ataque seleccionado por el jugador.
        """
        while True:
            print("ELIGE UN ATAQUE")
            for i, ataque in enumerate(self.ataques, 1):
                print(f"{i}. {ataque.presentar_ataque()}")
            ataque_elegido = input("Seleccione un ataque: ")
            if ataque_elegido in ["1", "2", "3"]:
                return self.ataques[int(ataque_elegido) - 1]
            else:
                print("Opción inválida, seleccione de nuevo...")

    def restablecer_vida(self):
        """Restablece la vida del jugador a su valor inicial y muestra un mensaje de confirmación.

        Returns:
            int: Vida restablecida del jugador.
        """
        self.vida = self.vida_inicial
        print(f"La vida de {self.nombre} se ha restablecido a {self.vida}")
        return self.vida


class Enemigo(Controlable):
    def __init__(self, personaje, puntos_experiencia):
        """Inicializa un enemigo basado en un personaje.

        Args:
            personaje (Controlable): Personaje enemigo.
            puntos_experiencia (int): Puntos de experiencia del enemigo.
        """
        super().__init__(personaje.nombre, personaje.descripcion, personaje.vida, personaje.fuerza, personaje.velocidad, personaje.iq, personaje.ataques, puntos_experiencia)

    def seleccionar_personaje(self, jugador):
        """Selecciona un personaje aleatorio como enemigo, diferente al del jugador.

        Args:
            jugador (Jugador): Jugador principal del juego.

        Returns:
            Enemigo: Enemigo seleccionado para la ronda.
        """
        lista_personajes = [GalloFortachon(), GalloVolador(), GalloSabio(), Gallina()]
        enemigo = Enemigo(lista_personajes[0], 0)  # Inicializa la variable enemigo
        nombre_enemigo = self.nombre
        while jugador.nombre == nombre_enemigo:
            nro_enemigo = randint(0, len(lista_personajes) - 1)
            enemigo = Enemigo(lista_personajes[nro_enemigo], 0)
            nombre_enemigo = enemigo.nombre
        return enemigo

    def seleccionar_ataque(self):
        """Selecciona un ataque aleatorio de la lista de ataques del enemigo.

        Returns:
            Ataque: Ataque seleccionado por el enemigo.
        """
        nro_ataque_elegido = randint(0, len(self.ataques) - 1)
        return self.ataques[nro_ataque_elegido]
