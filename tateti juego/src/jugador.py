class Jugador:
    def __init__(self, nombre: str, simbolo: str):
        """Inicializa un jugador con validación de símbolo.

        Args:
            nombre (str): Nombre del jugador
            simbolo (str): Debe ser 'X' u 'O'

        Raises:
            ValueError: Si el símbolo es inválido o el nombre está vacío
        """
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if simbolo.upper() not in ("X", "O"):  # Corregido: era "O};
            raise ValueError("Símbolo debe ser 'X' u 'O'")  # Corregido: era "O}
        self.nombre = nombre.strip()
        self.simbolo = simbolo.upper()