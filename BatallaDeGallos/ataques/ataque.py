from abc import ABC, abstractmethod  # Importa la clase ABC y el decorador abstractmethod

class Ataque(ABC):
    def __init__(self, nombre, descripcion, danho, velocidad, fuerza, tipo):
        """Inicializa un ataque con sus atributos.

        Args:
            nombre (str): Nombre del ataque.
            descripcion (str): Descripción del ataque.
            danho (int): Daño infligido por el ataque.
            velocidad (int): Velocidad del ataque.
            fuerza (int): Fuerza del ataque.
            tipo (str): Tipo de ataque (físico, aéreo, intelectual, básico).
        """
        self.nombre = nombre
        self.descripcion = descripcion
        self.danho = danho
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.tipo = tipo

    def presentar_ataque(self):
        """Devuelve una representación del ataque."""
        return f"{self.nombre}: {self.descripcion}"


class FuerzaBruta(Ataque):
    def __init__(self):
        """Inicializa un ataque de Fuerza Bruta con atributos específicos."""
        super().__init__("Fuerza Bruta", "Ataque físico poderoso", 10, 5, 2, "Físico")


class ArtilleriaPesada(Ataque):
    def __init__(self):
        """Inicializa un ataque de Artillería Pesada con atributos específicos."""
        super().__init__("Artillería Pesada", "Ataque físico extremadamente poderoso", 15, 4, 3, "Físico")


class PolloAlSpiedo(Ataque):
    def __init__(self):
        """Inicializa un ataque de Pollo al Spiedo con atributos específicos."""
        super().__init__("Pollo al Spiedo", "Ataque que cocina al enemigo lentamente", 8, 3, 4, "Físico")


class AlasFuertes(Ataque):
    def __init__(self):
        """Inicializa un ataque de Alas Fuertes con atributos específicos."""
        super().__init__("Alas Fuertes", "Ataque con un aleteo poderoso", 9, 6, 2, "Aéreo")


class PolloATierra(Ataque):
    def __init__(self):
        """Inicializa un ataque de Pollo a Tierra con atributos específicos."""
        super().__init__("Pollo a Tierra", "Ataque aéreo rápido y directo", 7, 8, 3, "Aéreo")


class Paracaidas(Ataque):
    def __init__(self):
        """Inicializa un ataque de Paracaídas con atributos específicos."""
        super().__init__("Paracaídas", "Ataque con un aterrizaje sorpresa", 6, 9, 4, "Aéreo")


class PicoSabio(Ataque):
    def __init__(self):
        """Inicializa un ataque de Pico Sabio con atributos específicos."""
        super().__init__("Pico Sabio", "Ataque inteligente y preciso", 8, 7, 2, "Intelectual")


class GraznidoFeroz(Ataque):
    def __init__(self):
        """Inicializa un ataque de Graznido Feroz con atributos específicos."""
        super().__init__("Graznido Feroz", "Ataque que intimida al enemigo", 7, 8, 3, "Intelectual")


class GolpeEquilibrado(Ataque):
    def __init__(self):
        """Inicializa un ataque de Golpe Equilibrado con atributos específicos."""
        super().__init__("Golpe Equilibrado", "Ataque balanceado", 9, 6, 4, "Intelectual")


class Picotazo(Ataque):
    def __init__(self):
        """Inicializa un ataque de Picotazo con atributos específicos."""
        super().__init__("Picotazo", "Ataque básico con el pico", 6, 7, 2, "Básico")


class Ponedora(Ataque):
    def __init__(self):
        """Inicializa un ataque de Ponedora con atributos específicos."""
        super().__init__("Ponedora", "Ataque que genera huevos explosivos", 7, 6, 3, "Básico")


class PechugaAsada(Ataque):
    def __init__(self):
        """Inicializa un ataque de Pechuga Asada con atributos específicos."""
        super().__init__("Pechuga Asada", "Ataque que calienta al enemigo", 8, 5, 4, "Básico")
