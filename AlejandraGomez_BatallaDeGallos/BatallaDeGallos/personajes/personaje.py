from ataques.ataque import *  # Importa todas las clases de ataques del módulo ataques

class Personaje(ABC):
    def __init__(self, nombre, descripcion, vida, fuerza, velocidad, iq, ataques):
        """Inicializa un personaje con sus atributos.

        Args:
            nombre (str): Nombre del personaje.
            descripcion (str): Descripción del personaje.
            vida (int): Puntos de vida del personaje.
            fuerza (int): Nivel de fuerza del personaje.
            velocidad (int): Nivel de velocidad del personaje.
            iq (int): Nivel de inteligencia del personaje.
            ataques (list): Lista de objetos de tipo Ataque disponibles para el personaje.
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.vida = int(vida)
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.iq = iq
        self.ataques = ataques

    def mostrar_info(self):
        """Muestra la información del personaje."""
        print(f"""{self.nombre}: 
        Vida: {self.vida}
        Fuerza: {self.fuerza}
        Velocidad: {self.velocidad}
        IQ: {self.iq}""")

        """Clase abstracta para un festejo diferente por cada tipo de personaje. (Por crear en el futuro)"""
        def victoria(self):
            pass


class GalloFortachon(Personaje):
    def __init__(self):
        """Inicializa un Gallo Fortachon con atributos específicos y una lista de ataques predefinidos."""
        super().__init__("Gallo Fortachon",
                         "Es capaz de dar golpes duros pero su velocidad se ve afectada por su robustez. No es muy inteligente y tiene mucha vida",
                         50, 6, 5, 4, [FuerzaBruta(), ArtilleriaPesada(), PolloAlSpiedo()])


class GalloVolador(Personaje):
    def __init__(self):
        """Inicializa un Gallo Volador con atributos específicos y una lista de ataques predefinidos."""
        super().__init__("Gallo Volador", "Vuelo gracil que le permite atacar más rápido pero con fuerza limitada", 35,
                         4, 8, 6, [AlasFuertes(), PolloATierra(), Paracaidas()])


class GalloSabio(Personaje):
    def __init__(self):
        """Inicializa un Gallo Sabio con atributos específicos y una lista de ataques predefinidos."""
        super().__init__("Gallo Sabio", "Emplea toda su sabiduría esquivando ataques, sin embargo tiene una vida corta",
                         30, 5, 6, 8, [PicoSabio(), GraznidoFeroz(), GolpeEquilibrado()])


class Gallina(Personaje):
    def __init__(self):
        """Inicializa una Gallina con atributos específicos y una lista de ataques predefinidos."""
        super().__init__("Gallina",
                         "Persevera y triunfarás, tiene todo lo que se debe tener para una batalla equilibrada", 40, 5,
                         7, 5, [Picotazo(), Ponedora(), PechugaAsada()])
