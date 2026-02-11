import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                             QVBoxLayout, QWidget, QGridLayout, QMessageBox)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

from back import LogicaGato

# VENTANA DEL MENÚ

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        self.setFixedSize(600, 500)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout = QVBoxLayout()
        widget_central.setLayout(layout)

        titulo = QLabel("Gato en Python")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        layout.addWidget(titulo)

        # Botón PvP
        btn_pvp = QPushButton("2 Jugadores")
        btn_pvp.setFont(QFont("Arial", 14))
        btn_pvp.clicked.connect(lambda: self.abrir_juego("PvP"))
        layout.addWidget(btn_pvp)

        # Botón IA
        btn_pvia = QPushButton("Contra la IA (Ella inicia)")
        btn_pvia.setFont(QFont("Arial", 14))
        btn_pvia.clicked.connect(lambda: self.abrir_juego("PvIA"))
        layout.addWidget(btn_pvia)

    def abrir_juego(self, modo):
        self.juego = InterfazGato(modo, self)
        self.juego.show()
        self.close()

# VENTANA DEL JUEGO

class InterfazGato(QMainWindow):

    def __init__(self, modo, ventana_menu):
        super().__init__()
        self.logica = LogicaGato()
        self.modo = modo
        self.ventana_menu = ventana_menu
        self.botones = []
        
        # CONFIGURACIÓN DE TURNOS
        if self.modo == "PvIA":
            # Si jugamos contra la IA, la IA es "X" (Empieza) y nosotros "O"
            self.simbolo_ia = "X"
            self.simbolo_humano = "O"
        else:
            # En PvP no hay IA, pero por defecto el humano clicando es el turno actual
            self.simbolo_ia = None 
            self.simbolo_humano = "X" # Irrelevante en PvP, se alterna

        self.inicializar_ui()

        # Si la IA empieza (es X), disparamos su primer movimiento automáticamente
        if self.modo == "PvIA" and self.simbolo_ia == "X":
            self.etiqueta_estado.setText("La IA está pensando...")
            QTimer.singleShot(700, self.movimiento_ia)

    def inicializar_ui(self):
        texto = "Juego: vs Jugador" if self.modo == "PvP" else "Juego: vs IA (Tú eres O)"
        self.setWindowTitle(texto)
        self.setFixedSize(350, 480)

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        self.etiqueta_estado = QLabel(f"Turno de: X")
        self.etiqueta_estado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_estado.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        layout_principal.addWidget(self.etiqueta_estado)

        layout_tablero = QGridLayout()
        layout_principal.addLayout(layout_tablero)

        for i in range(9):
            boton = QPushButton("")
            boton.setFixedSize(90, 90)
            boton.setFont(QFont("Arial", 28, QFont.Weight.Bold))
            boton.clicked.connect(lambda _, idx=i: self.manejar_clic_humano(idx))
            layout_tablero.addWidget(boton, i // 3, i % 3)
            self.botones.append(boton)

        boton_volver = QPushButton("Volver al Menú")
        boton_volver.clicked.connect(self.volver_al_menu)
        layout_principal.addWidget(boton_volver)

    def manejar_clic_humano(self, indice):
        # 1. Validaciones para el modo PvIA
        if self.modo == "PvIA":
            # Si no es turno del humano (es turno de la IA), no hacemos nada
            if self.logica.turno_actual != self.simbolo_humano:
                return

        # 2. Intento de movimiento
        jugador_actual = self.logica.turno_actual
        if self.logica.realizar_movimiento(indice, jugador_actual):
            self.actualizar_tablero_visual(indice)
            
            if self.logica.juego_terminado:
                self.mostrar_mensaje_final()
            else:
                self.etiqueta_estado.setText(f"Turno de: {self.logica.turno_actual}")
                
                # Si es PvIA, ahora le toca a la computadora
                if self.modo == "PvIA":
                    self.etiqueta_estado.setText("La IA está pensando...")
                    # Delay para que parezca que piensa
                    QTimer.singleShot(700, self.movimiento_ia)

    def movimiento_ia(self):
        # Le pasamos a la lógica qué símbolo usa la IA
        idx = self.logica.obtener_movimiento_ia(self.simbolo_ia)
        
        if idx is not None:
            self.logica.realizar_movimiento(idx, self.simbolo_ia)
            self.actualizar_tablero_visual(idx)
            
            if self.logica.juego_terminado:
                self.mostrar_mensaje_final()
            else:
                self.etiqueta_estado.setText(f"Turno de: {self.logica.turno_actual}")

    def actualizar_tablero_visual(self, indice):
        boton = self.botones[indice]
        simbolo = self.logica.tablero[indice]
        boton.setText(simbolo)
        color = "#007BFF" if simbolo == "X" else "#FF5733"
        boton.setStyleSheet(f"color: {color}; border: 1px solid #ccc;")

    def mostrar_mensaje_final(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Fin del Juego")
        
        if self.logica.ganador == "Empate":
            msg.setText("¡Es un Empate!")
        else:
            if self.modo == "PvIA":
                ganador = "la IA" if self.logica.ganador == self.simbolo_ia else "Tú"
                msg.setText(f"¡Ha ganado {ganador}!")
            else:
                msg.setText(f"¡Ha ganado el jugador {self.logica.ganador}!")
        
        msg.exec()
        self.volver_al_menu()

    def volver_al_menu(self):
        self.close()
        self.ventana_menu.show()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    menu = MenuPrincipal()
    menu.show()
    sys.exit(app.exec())