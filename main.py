from src.jugador import Jugador
from src.tateti import Tateti

def main():
    print("\n=== TA-TE-TI (Presiona Ctrl+C para salir) ===")
    
    jugador1 = Jugador(input("Nombre Jugador 1 (X): "), "X")
    jugador2 = Jugador(input("Nombre Jugador 2 (O): "), "O")
    juego = Tateti(jugador1, jugador2)

    try:
        while True:
            print(f"\nTurno de: {juego.jugador_actual.nombre}")
            print(juego.tablero.mostrar())
            
            entrada = input("Fila y columna (0-2) o 'salir': ").lower()
            if entrada == 'salir':
                print("\n¡Juego finalizado!")
                juego.terminar_juego()
                break

            try:
                fila, col = map(int, entrada.split())
                resultado = juego.jugar(fila, col)
                
                if resultado is None:
                    print("¡Movimiento inválido! Casilla ocupada o coordenadas incorrectas.")
                    continue
                    
                if resultado:
                    print(juego.tablero.mostrar())
                    if juego.ganador:
                        print(f"\n¡{juego.ganador.nombre} gana!")
                    else:
                        print("\n¡Empate!")
                    break

            except ValueError:
                print("Error: Ingresa dos números (0-2) o 'salir'")

    except KeyboardInterrupt:
        print("\n\n¡Juego interrumpido por el usuario!")

if __name__ == "__main__":
    main()