from src.jugador import Jugador
from src.tablero import Tablero

class Tateti:
    def __init__(self, jugador1: Jugador, jugador2: Jugador):
        self.jugador_actual = jugador1
        self.jugador_siguiente = jugador2
        self.tablero = Tablero()
        self.ganador = None

    def cambiar_turno(self):
        self.jugador_actual, self.jugador_siguiente = self.jugador_siguiente, self.jugador_actual

    def jugar(self, fila: int, col: int) -> bool:
        if self.ganador or self.tablero.empate():
            return False

        try:
            simbolo = self.jugador_actual.simbolo
            self.tablero.realizar_movimiento(fila, col, simbolo)

            if self.tablero.hay_ganador(simbolo):
                self.ganador = self.jugador_actual
                return True

            if self.tablero.empate():
                return True

            self.cambiar_turno()
            return False

        except ValueError:
            return False