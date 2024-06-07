from abc import ABC, abstractmethod
from clases.ataques import *
from random import randint
import sys

class Personaje(ABC):
    """Clase abstracta base para todos los personajes."""

    def __init__(self, nombre, descripcion, vida, fuerza, velocidad, iq, ataques):
        """
        Inicializa un personaje con sus atributos básicos.

        Args:
            nombre (str): Nombre del personaje.
            descripcion (str): Descripción del personaje.
            vida (int): Vida del personaje.
            fuerza (int): Fuerza del personaje.
            velocidad (int): Velocidad del personaje.
            iq (int): IQ del personaje.
            ataques (list): Lista de instancias de ataques del personaje.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.vida = int(vida)
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.iq = iq
        self.ataques = ataques  # Lista de instancias de ataques

    def mostrar_info(self):
        """Muestra la información del personaje."""
        print(f"""{self.nombre}: 
        Vida: {self.vida}
        Fuerza: {self.fuerza}
        Velocidad: {self.velocidad}
        IQ: {self.iq}""")

    @abstractmethod
    def elegir_ataque(self):
        """Método abstracto para elegir un ataque."""
        pass

    def ataque_enemigo(self):
        """Selecciona un ataque aleatorio del enemigo."""
        nro_ataque_elegido = randint(0, len(self.ataques) - 1)
        return self.ataques[nro_ataque_elegido]

    def probabilidad_esquivar(self):
        """Calcula la probabilidad de esquivar un ataque basado en el IQ."""
        probabilidad = self.iq * 5
        nro = randint(1, 100)
        return nro < probabilidad

    def restar_vida(self, dano):
        """Resta vida al personaje basado en el daño recibido.

        Args:
            dano (int): Cantidad de daño a restar.
        """
        print(f"{self.nombre} pierde {dano} de vida")
        self.vida -= dano

    def vivo_o_muerto(self, personaje):
        """Verifica si el personaje está vivo o muerto y finaliza el juego si es necesario.

        Args:
            personaje (Personaje): Personaje adversario.
        """
        if self.vida <= 0:
            print(f"\t\t\t{self.nombre} se ha quedado sin vida :c\n"
                  f"\t\t\t{personaje.nombre} HA GANADO")
            sys.exit()

class GalloFortachon(Personaje):
    """Clase específica para el Gallo Fortachón."""

    def __init__(self):
        super().__init__("Gallo Fortachon",
                         "Es capaz de dar golpes duros pero su velocidad se ve afectada por su robustez. No es muy inteligente y tiene mucha vida",
                         50, 6, 5, 4, [FuerzaBruta(), ArtilleriaPesada(), PolloAlSpiedo()])

    def elegir_ataque(self):
        """Permite al jugador elegir un ataque para el Gallo Fortachón."""
        while True:
            print("ELIGE UN ATAQUE")
            for i, ataque in enumerate(self.ataques, 1):
                print(f"{i}. {ataque.presentar_ataque()}")
            ataque_elegido = input("Seleccione un ataque: ")
            if ataque_elegido in ["1", "2", "3"]:
                return self.ataques[int(ataque_elegido) - 1]
            else:
                print("Opción inválida, seleccione de nuevo...")

class GalloVolador(Personaje):
    """Clase específica para el Gallo Volador."""

    def __init__(self):
        super().__init__("Gallo Volador", "Vuelo gracil que le permite atacar más rápido pero con fuerza limitada", 35,
                         4, 8, 6, [AlasFuertes(), PolloATierra(), Paracaidas()])

    def elegir_ataque(self):
        """Permite al jugador elegir un ataque para el Gallo Volador."""
        while True:
            print("ELIGE UN ATAQUE")
            for i, ataque in enumerate(self.ataques, 1):
                print(f"{i}. {ataque.presentar_ataque()}")
            ataque_elegido = input("Seleccione un ataque: ")
            if ataque_elegido in ["1", "2", "3"]:
                return self.ataques[int(ataque_elegido) - 1]
            else:
                print("Opción inválida, seleccione de nuevo...")

class GalloSabio(Personaje):
    """Clase específica para el Gallo Sabio."""

    def __init__(self):
        super().__init__("Gallo Sabio", "Emplea toda su sabiduría esquivando ataques, sin embargo tiene una vida corta",
                         30, 5, 6, 8, [PicoSabio(), GraznidoFeroz(), GolpeEquilibrado()])

    def elegir_ataque(self):
        """Permite al jugador elegir un ataque para el Gallo Sabio."""
        while True:
            print("ELIGE UN ATAQUE")
            for i, ataque in enumerate(self.ataques, 1):
                print(f"{i}. {ataque.presentar_ataque()}")
            ataque_elegido = input("Seleccione un ataque: ")
            if ataque_elegido in ["1", "2", "3"]:
                return self.ataques[int(ataque_elegido) - 1]
            else:
                print("Opción inválida, seleccione de nuevo...")

class Gallina(Personaje):
    """Clase específica para la Gallina."""

    def __init__(self):
        super().__init__("Gallina",
                         "Persevera y triunfarás, tiene todo lo que se debe tener para una batalla equilibrada", 40, 5,
                         7, 5, [Picotazo(), Ponedora(), PechugaAsada()])

    def elegir_ataque(self):
        """Permite al jugador elegir un ataque para la Gallina."""
        while True:
            print("ELIGE UN ATAQUE")
            for i, ataque in enumerate(self.ataques, 1):
                print(f"{i}. {ataque.presentar_ataque()}")
            ataque_elegido = input("Seleccione un ataque: ")
            if ataque_elegido in ["1", "2", "3"]:
                return self.ataques[int(ataque_elegido) - 1]
            else:
                print("Opción inválida, seleccione de nuevo...")
