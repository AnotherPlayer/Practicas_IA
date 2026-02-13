import math

class LogicaGato:
    
    def __init__(self):
        self.reiniciar_estado()

    def reiniciar_estado(self):
        self.tablero = [""] * 9
        self.turno_actual = "X"
        self.ganador = None
        self.juego_terminado = False

    def realizar_movimiento(self, indice, jugador):
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

    # ALGORITMO MINIMAX (NIVEL DIOS)
    def obtener_movimiento_ia(self, simbolo_ia):
        """
        Calcula el mejor movimiento posible usando Minimax.
        """
        mejor_puntaje = -math.inf
        mejor_movimiento = None
        
        # Recorremos todas las casillas vacías para ver cuál da mejor resultado
        for i in range(9):
            if self.tablero[i] == "":
                self.tablero[i] = simbolo_ia # Probamos mover aquí
                puntaje = self.minimax(self.tablero, 0, False, simbolo_ia)
                self.tablero[i] = "" # Deshacemos el movimiento
                
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_movimiento = i
        
        return mejor_movimiento

    def minimax(self, tablero, profundidad, es_maximizando, simbolo_ia):
        # 1. Verificar si el juego terminó en esta simulación
        resultado = self.verificar_estado_simulado(simbolo_ia)
        if resultado != None:
            return resultado

        simbolo_rival = "O" if simbolo_ia == "X" else "X"

        # 2. Si es turno de la IA (Maximizando)
        if es_maximizando:
            mejor_puntaje = -math.inf
            for i in range(9):
                if tablero[i] == "":
                    tablero[i] = simbolo_ia
                    puntaje = self.minimax(tablero, profundidad + 1, False, simbolo_ia)
                    tablero[i] = ""
                    mejor_puntaje = max(puntaje, mejor_puntaje)
            return mejor_puntaje
        
        # 3. Si es turno del Humano (Minimizando - Asumimos que el humano juega perfecto)
        else:
            mejor_puntaje = math.inf
            for i in range(9):
                if tablero[i] == "":
                    tablero[i] = simbolo_rival
                    puntaje = self.minimax(tablero, profundidad + 1, True, simbolo_ia)
                    tablero[i] = ""
                    mejor_puntaje = min(puntaje, mejor_puntaje)
            return mejor_puntaje

    def verificar_estado_simulado(self, simbolo_ia):
        """
        Retorna puntuación: +10 si gana IA, -10 si gana Humano, 0 si Empate.
        """
        simbolo_rival = "O" if simbolo_ia == "X" else "X"
        
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        
        # Checar si alguien ganó
        for a, b, c in combinaciones:
            if self.tablero[a] == self.tablero[b] == self.tablero[c]:
                if self.tablero[a] == simbolo_ia:
                    return 10
                elif self.tablero[a] == simbolo_rival:
                    return -10
        
        # Checar empate
        if "" not in self.tablero:
            return 0
            
        return None # El juego sigue