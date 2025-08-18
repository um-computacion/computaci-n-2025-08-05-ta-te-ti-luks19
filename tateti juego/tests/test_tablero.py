from src.tablero import Tablero

def test_tablero_vacio():
    t = Tablero()
    assert t.mostrar() == " | | \n-+-+-\n | | \n-+-+-\n | | "

def test_movimiento_valido():
    t = Tablero()
    t.realizar_movimiento(0, 0, "X")
    assert t.celdas[0][0] == "X"

def test_hay_ganador():
    t = Tablero()
    for i in range(3):
        t.realizar_movimiento(0, i, "X")
    assert t.hay_ganador("X")