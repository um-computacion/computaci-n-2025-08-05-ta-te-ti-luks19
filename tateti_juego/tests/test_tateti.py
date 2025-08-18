import pytest
from src.tateti import Tateti
from src.jugador import Jugador

@pytest.fixture
def juego():
    return Tateti(Jugador("Ana", "X"), Jugador("Luis", "O"))

def test_terminar_juego(juego):
    juego.terminar_juego()
    assert juego.juego_terminado is True
    assert juego.jugar(0, 0) is True  # No permite más movimientos

def test_jugada_invalida(juego):
    assert juego.jugar(3, 3) is None  # Coordenadas inválidas
    juego.jugar(0, 0)
    assert juego.jugar(0, 0) is None  # Casilla ocupada

def test_salida_voluntaria(juego):
    juego.terminar_juego()
    assert juego.jugador_actual.nombre == "Ana"  # No cambió el turno