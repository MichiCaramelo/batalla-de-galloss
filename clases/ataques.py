class Ataque:
    """Clase base para los ataques."""

    def __init__(self, nombre_ataque, fuerza_ataque, velocidad_ataque):
        """
        Inicializa un ataque con sus atributos básicos.

        Args:
            nombre_ataque (str): Nombre del ataque.
            fuerza_ataque (int): Fuerza del ataque.
            velocidad_ataque (int): Velocidad del ataque.
        """
        self.nombre = nombre_ataque
        self.fuerza = int(fuerza_ataque)
        self.velocidad = int(velocidad_ataque)

    def presentar_ataque(self):
        """Presenta el ataque con sus atributos."""
        return f"{self.nombre}: fuerza {self.fuerza}, velocidad {self.velocidad}"

class FuerzaBruta(Ataque):
    """Clase para el ataque Fuerza Bruta."""

    def __init__(self):
        super().__init__("Fuerza Bruta", 8, 2)

class ArtilleriaPesada(Ataque):
    """Clase para el ataque Artillería Pesada."""

    def __init__(self):
        super().__init__("Artilleria Pesada", 6, 4)

class PolloAlSpiedo(Ataque):
    """Clase para el ataque Pollo al Spiedo."""

    def __init__(self):
        super().__init__("Pollo al Spiedo", 4, 6)

class AlasFuertes(Ataque):
    """Clase para el ataque Alas Fuertes."""

    def __init__(self):
        super().__init__("Alas Fuertes", 7, 3)

class PolloATierra(Ataque):
    """Clase para el ataque Pollo a Tierra."""

    def __init__(self):
        super().__init__("Pollo a Tierra", 6, 4)

class Paracaidas(Ataque):
    """Clase para el ataque Paracaídas."""

    def __init__(self):
        super().__init__("Paracaidas", 5, 5)

class PicoSabio(Ataque):
    """Clase para el ataque Pico Sabio."""

    def __init__(self):
        super().__init__("Pico Sabio", 6, 4)

class GraznidoFeroz(Ataque):
    """Clase para el ataque Graznido Feroz."""

    def __init__(self):
        super().__init__("Graznido Feroz", 5, 5)

class GolpeEquilibrado(Ataque):
    """Clase para el ataque Golpe Equilibrado."""

    def __init__(self):
        super().__init__("Golpe Equilibrado", 4, 6)

class Picotazo(Ataque):
    """Clase para el ataque Picotazo."""

    def __init__(self):
        super().__init__("Picotazo", 6, 4)

class Ponedora(Ataque):
    """Clase para el ataque Ponedora."""

    def __init__(self):
        super().__init__("Ponedora", 5, 5)

class PechugaAsada(Ataque):
    """Clase para el ataque Pechuga Asada."""

    def __init__(self):
        super().__init__("Pechuga Asada", 4, 6)
