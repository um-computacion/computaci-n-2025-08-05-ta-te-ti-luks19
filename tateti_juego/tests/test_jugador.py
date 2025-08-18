import pytest
from src.jugador import Jugador

def test_creacion_jugador_valido():
    """Verifica que se crea un jugador con nombre y símbolo válidos"""
    jugador = Jugador(nombre="Ana", simbolo="X")
    assert jugador.nombre == "Ana"
    assert jugador.simbolo == "X"

def test_jugador_simbolo_invalido():
    """Valida que el símbolo debe ser 'X' u 'O'"""
    with pytest.raises(ValueError):
        Jugador(nombre="Ana", simbolo="Z")