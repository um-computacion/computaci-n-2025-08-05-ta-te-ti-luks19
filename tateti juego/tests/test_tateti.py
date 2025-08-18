import pytest
from src.tateti import Tateti
from src.jugador import Jugador
from src.tablero import Tablero

@pytest.fixture
def juego():
    jugador1 = Jugador("Ana", "X")
    jugador2 = Jugador("Luis", "O")
    return Tateti(jugador1, jugador2)

def test_inicializacion(juego):
    assert juego.jugador_actual.nombre == "Ana"
    assert isinstance(juego.tablero, Tablero)

def test_cambio_turno(juego):
    juego.cambiar_turno()
    assert juego.jugador_actual.nombre == "Luis"

def test_jugada_valida(juego):
    assert juego.jugar(0, 0) is False  # No gana aún
    assert juego.jugador_actual.nombre == "Luis"

def test_jugada_ganadora(juego):
    jugadas_ganadoras = [(0, 0), (1, 1), (0, 1), (2, 2), (0, 2)]
    for fila, col in jugadas_ganadoras[:3]:
        juego.jugar(fila, col)
    assert juego.jugar(0, 2) is True  # Ana gana
    assert juego.ganador.nombre == "Ana"

def test_empate(juego):
    jugadas = [(0,0), (0,1), (0,2), 
               (1,1), (1,0), (1,2), 
               (2,1), (2,0), (2,2)]
    for fila, col in jugadas[:-1]:
        juego.jugar(fila, col)
    assert juego.jugar(2, 2) is True  # Empate
    assert juego.ganador is None