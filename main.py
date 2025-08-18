from src.jugador import Jugador
from src.tateti import Tateti

def main():
    print("\n=== TA-TE-TI ===")
    
    # Registro de jugadores
    jugador1 = Jugador(input("Nombre Jugador 1 (X): "), "X")
    jugador2 = Jugador(input("Nombre Jugador 2 (O): "), "O")
    
    juego = Tateti(jugador1, jugador2)
    
    # Bucle principal
    while True:
        print(f"\nTurno de: {juego.jugador_actual.nombre}")
        print(juego.tablero.mostrar())
        
        try:
            fila = int(input("Fila (0-2): "))
            col = int(input("Columna (0-2): "))
            
            if juego.jugar(fila, col):
                print(juego.tablero.mostrar())
                if juego.ganador:
                    print(f"\n¡{juego.ganador.nombre} gana!")
                else:
                    print("\n¡Empate!")
                break
                
        except ValueError:
            print("Error: Ingresa números entre 0 y 2")

if __name__ == "__main__":
    main()