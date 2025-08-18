class Tablero:
    def __init__(self):
        self.celdas = [[None]*3 for _ in range(3)]
    
    def mostrar(self):
        return "\n-+-+-\n".join("|".join(c or " " for c in fila) for fila in self.celdas)
    
    def movimiento_valido(self, fila, col):
        return 0 <= fila < 3 and 0 <= col < 3 and self.celdas[fila][col] is None
    
    def realizar_movimiento(self, fila, col, simbolo):
        if not self.movimiento_valido(fila, col):
            raise ValueError("Movimiento inválido")
        self.celdas[fila][col] = simbolo
    
    def hay_ganador(self, simbolo):
        for i in range(3):
            if all(self.celdas[i][j] == simbolo for j in range(3)):
                return True
            if all(self.celdas[j][i] == simbolo for j in range(3)):
                return True
        if all(self.celdas[i][i] == simbolo for i in range(3)):
            return True
        if all(self.celdas[i][2-i] == simbolo for i in range(3)):
            return True
        return False
    
    def empate(self):
        return all(None not in fila for fila in self.celdas)