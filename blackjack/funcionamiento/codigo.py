class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nombre: str = nombre
        self.fichas: int = fichas
        pass

    def inicialicazar_mano(self, cartas):
        pass

    def jugada_jugador(self):
        pass


class Carta:
    pinta: str
    valor: str
    lado: bool


class Mano:
    def __init__(self, cartas):
        self.cartas: cartas = cartas
        pass

    def es_blackjack(self) -> bool:
        pass

    def pedir_carta(self):
        pass

    def calcular_valor(self, cartas):
        pass

    def mostrar_carta(self, carta):
        pass


class Casa:
    def inicializar_mano(self):
        pass


class Baraja:
    def revolver(self):
        pass

    def repartir_carta(self, tapada: bool) -> Carta:
        pass


class Blackjack:
    def registrar_jugador(self, nmbre: str):
        pass

    def iniciar_juego(self, apuesta: int):
        pass

    def finalizar_juego(self):
        pass

    def comparar_manos(self, mano):
        pass

    def jugador_gana(self, nombre: str, apuesta: int):
        pass

    def casa_gana(self, nombre: str, apuesta: int):
        pass

    def empate(self, nombre: str, apuesta: int):
        pass
