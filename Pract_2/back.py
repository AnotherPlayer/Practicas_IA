import random

class LogicaGato:
    def __init__(self):
        self.reiniciar_estado()

    def reiniciar_estado(self):
        self.tablero = [""] * 9
        self.turno_actual = "X"
        self.ganador = None
        self.juego_terminado = False

    def realizar_movimiento(self, indice, jugador):
        """Intenta hacer un movimiento para el jugador dado."""
        if self.tablero[indice] == "" and not self.juego_terminado:
            if self.turno_actual != jugador:
                return False

            self.tablero[indice] = self.turno_actual
            
            if self.verificar_ganador():
                self.juego_terminado = True
                self.ganador = self.turno_actual
            elif "" not in self.tablero:
                self.juego_terminado = True
                self.ganador = "Empate"
            else:
                self.cambiar_turno()
            return True
        return False

    def cambiar_turno(self):
        self.turno_actual = "O" if self.turno_actual == "X" else "X"

    def verificar_ganador(self):
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combinaciones:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] and self.tablero[a] != "":
                return True
        return False

    # --- IA ACTUALIZADA ---
    def obtener_movimiento_ia(self, simbolo_ia):
        """
        Ahora la IA recibe su símbolo ("X" o "O") para saber
        con qué ficha atacar y de qué ficha defenderse.
        """
        simbolo_rival = "O" if simbolo_ia == "X" else "X"
        vacios = [i for i, x in enumerate(self.tablero) if x == ""]
        
        # 1. Intentar Ganar (Usando su propio símbolo)
        for i in vacios:
            self.tablero[i] = simbolo_ia 
            if self.verificar_ganador():
                self.tablero[i] = ""
                return i
            self.tablero[i] = "" 

        # 2. Bloquear (Viendo si el rival gana)
        for i in vacios:
            self.tablero[i] = simbolo_rival 
            if self.verificar_ganador():
                self.tablero[i] = ""
                return i
            self.tablero[i] = ""

        # 3. Elegir Centro
        if 4 in vacios:
            return 4

        # 4. Aleatorio
        return random.choice(vacios) if vacios else None