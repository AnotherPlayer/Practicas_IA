import tkinter as tk
from tkinter import messagebox


# 1. Espacio de Busqueda (EL GRAFO)

class Nodo:
    def __init__(self, id_nodo, nombre, tiene_gema=False, tipo_gema=""):
        self.id = id_nodo
        self.nombre = nombre
        self.izquierda = None
        self.derecha = None
        self.padre = None
        self.portal = None
        self.tiene_gema = tiene_gema
        self.tipo_gema = tipo_gema
        self.gema_recolectada = False

def construir_laberinto():
    nodos = {
        'A': Nodo('A', 'Inicio'),
        'B': Nodo('B', 'Casilla B', tiene_gema=True, tipo_gema='Zafiro de la Paciencia Infinita'),
        'C': Nodo('C', 'Casilla C', tiene_gema=True, tipo_gema='Diamante de la Perseverancia'),
        'D': Nodo('D', 'Casilla D'),
        'E': Nodo('E', 'Casilla E', tiene_gema=True, tipo_gema="Esmeralda del 'Casi lo Logras'"),
        'F': Nodo('F', 'Casilla F'),
        'G': Nodo('G', 'Casilla G', tiene_gema=True, tipo_gema="Amatista del '¿Por que sigo jugando?'"),
        'H': Nodo('H', 'Casilla H'),
        'I': Nodo('I', 'Casilla I'),
        'J': Nodo('J', 'Casilla J'),
        'K': Nodo('K', 'Casilla K', tiene_gema=True, tipo_gema='Rubi del Esfuerzo Inutil'),
        'L': Nodo('L', 'Casilla L'),
        'M': Nodo('M', 'Casilla M'),
        'N': Nodo('N', 'Casilla N'),
        'O': Nodo('O', 'Casilla O')
    }

    conexiones = {
        'A': ('B', 'C'), 'B': ('D', 'E'), 'C': ('F', 'G'),
        'D': ('H', 'I'), 'E': ('J', 'K'), 'F': ('L', 'M'),
        'G': ('N', 'O')
    }

    for padre, (izq, der) in conexiones.items():
        nodos[padre].izquierda = nodos[izq]
        nodos[padre].derecha = nodos[der]
        nodos[izq].padre = nodos[padre]
        nodos[der].padre = nodos[padre]

    # Correccion de Portales (Aristas Unidireccionales)
    nodos['H'].portal = nodos['O']
    nodos['N'].portal = nodos['A']
    # El nodo 'O' ya no tiene portal, por lo que te permitira pelear con el S.A.T.

    return nodos['A']


# 2. Mmotor e Interfaz Gráfica

class InterfazLaberinto:
    def __init__(self, ventana_principal):
        self.ventana = ventana_principal
        self.ventana.title("El Laberinto del Pasante")
        self.ventana.geometry("750x550")
        self.ventana.configure(bg="#1e1e1e")
        
        # Variables de estado del Agente
        self.nodo_actual = construir_laberinto()
        self.turnos = 0
        self.inventario = []
        self.mapa_obtenido = False
        self.jefe_golpes = 0
        
        # Elementos de la interfaz
        self.lbl_estado = tk.Label(self.ventana, text="", font=("Arial", 12, "bold"), bg="#1e1e1e", fg="#4CAF50")
        self.lbl_estado.pack(pady=10)
        
        self.texto_historia = tk.Label(self.ventana, text="", font=("Arial", 14), bg="#1e1e1e", fg="white", wraplength=650, justify="center")
        self.texto_historia.pack(pady=20)
        
        self.marco_botones = tk.Frame(self.ventana, bg="#1e1e1e")
        self.marco_botones.pack(pady=10)
        
        self.iniciar_juego()

    def limpiar_botones(self):
        for widget in self.marco_botones.winfo_children():
            widget.destroy()

    def crear_boton(self, texto, comando):
        boton = tk.Button(self.marco_botones, text=texto, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", width=40, command=comando)
        boton.pack(pady=5)

    def actualizar_estado_superior(self):
        # Contamos las gemas en el inventario
        gemas_actuales = sum(1 for item in self.inventario if "Zafiro" in item or "Diamante" in item or "Esmeralda" in item or "Amatista" in item or "Rubi" in item)
        gemas_faltantes = 5 - gemas_actuales
        
        texto_adicional = ""
        
        # Regla de Conocimiento Incompleto: El contador y el mapa solo se muestran si el agente lo tiene
        if self.mapa_obtenido:
            texto_adicional += f" | Gemas faltantes: {gemas_faltantes} | Mapa: 1"
            
        # Regla de Inventario: Mostrar la Llave Maestra cuando se haya forjado
        if "Llave Maestra" in self.inventario:
            texto_adicional += " | Llave Maestra: 1"
            
        # Actualizamos la etiqueta superior en la interfaz
        self.lbl_estado.config(text=f"Turnos: {self.turnos} | Casilla: {self.nodo_actual.id} ({self.nodo_actual.nombre}){texto_adicional}")

    def iniciar_juego(self):
        self.turnos = 0
        mensaje = "Te encuentras en un laberinto llamado Dirección Escolar.\nEres un estudiante de la ESCOM y para conseguir tu título deberás pasar la puerta de la titulación."
        self.renderizar_nodo(mensaje)

    def mover(self, direccion):
        self.turnos += 1
        if direccion == 'izq': self.nodo_actual = self.nodo_actual.izquierda
        elif direccion == 'der': self.nodo_actual = self.nodo_actual.derecha
        elif direccion == 'atras': self.nodo_actual = self.nodo_actual.padre
        
        mensaje = f"Has avanzado por los Pasillos oscuros...\n\nTe encuentras en: {self.nodo_actual.nombre}."
        
        if self.nodo_actual.portal:
            mensaje += f"\n\n¡CUIDADO! Has pisado un portal de trámites burocráticos y eres teletransportado a: {self.nodo_actual.portal.nombre}."
            self.nodo_actual = self.nodo_actual.portal
            
        self.renderizar_nodo(mensaje)

    def recolectar_gema(self):
        self.turnos += 2
        self.nodo_actual.gema_recolectada = True
        self.inventario.append(self.nodo_actual.tipo_gema)
        mensaje = f"Gastas 2 turnos excavando y recogiendo la piedra.\n\n¡Has obtenido el {self.nodo_actual.tipo_gema}!"
        self.renderizar_nodo(mensaje)

    def evento_libreria(self):
        self.limpiar_botones()
        self.turnos += 1
        self.texto_historia.config(text="Te acercas al estante de libros. Ves a Mafalda, la araña intelectual en el escritorio.\n¿Qué sección de chistes deseas leer para hacerla reír?")
        
        self.crear_boton("Sección de Humor Negro (Chiste A)", lambda: self.evaluar_chiste("¿Qué hacen 2 epilépticos en una cabina de teléfono?. - Una fiesta de espuma.", False))
        self.crear_boton("Sección Casual (Chiste B)", lambda: self.evaluar_chiste("¿Por qué los científicos no confían en los átomos? Porque lo componen todo.", False))
        self.crear_boton("Sección de Papá (Chiste C)", lambda: self.evaluar_chiste("¿Por qué los pájaros vuelan al sur? Porque caminando tardarían mucho.", True))
        self.crear_boton("Regresar", lambda: self.renderizar_nodo("Decides no molestar a Mafalda por ahora."))

    def evaluar_chiste(self, chiste, es_correcto):
        self.turnos += 2
        mensaje = f"Lees el chiste (2 turnos): '{chiste}'\n\nSe lo cuentas a Mafalda...\n"
        if es_correcto:
            self.mapa_obtenido = True
            self.inventario.append("Mapa")
            mensaje += "Mafalda se ríe a carcajadas y te entrega el Mapa del Laberinto.\n¡Ahora tienes visión de minero y puedes ver las gemas en los Casillas!"
        else:
            mensaje += "Mafalda te mira fijamente, aburrida. 'Ese chiste no da gracia', dice. No consigues nada."
        self.renderizar_nodo(mensaje)

    def leer_nota_forja(self):
        self.turnos += 1
        mensaje = "Lees la nota adherida en la maquina:\n\n'ADVERTENCIA: necesitas 5 gemas para obtener una llave\nP.D : Utilízala con sabiduria y cuidado, esta muy afilada guiño guiño.'"
        self.renderizar_nodo(mensaje)

    def evento_forja(self):
        self.limpiar_botones()
        gemas = sum(1 for item in self.inventario if "Zafiro" in item or "Diamante" in item or "Esmeralda" in item or "Amatista" in item or "Rubi" in item)
        if gemas == 5:
            self.turnos += 2
            self.inventario.append("Llave Maestra")
            mensaje = "Insertas las 5 gemas en el Sinto-Gema 3000.\nPasan 2 turnos...\n\n¡La maquina forja la LLAVE MAESTRA DE GRADUACION!"
        else:
            mensaje = f"Intentas operar la maquina, pero te faltan materiales.\nSolo tienes {gemas}/5 gemas en tu inventario."
        self.renderizar_nodo(mensaje)

    def evento_jefe(self):
        self.limpiar_botones()
        self.actualizar_estado_superior()
        
        # Como el boton solo aparece si tienes la llave, pasamos directo a la logica de combate
        self.texto_historia.config(text=f"COMBATE FINAL: S.A.T. (Supervisor de Actas y Trámites)\n\nEl monstruo te ataca con papeleo y tramites. \nGolpes dados: {self.jefe_golpes}/3")
        
        if self.jefe_golpes < 3:
            self.crear_boton("Atacar con Llave Maestra", self.atacar_jefe)
        else:
            self.finalizar_juego()

    def atacar_jefe(self):
        self.jefe_golpes += 1
        self.turnos += 1
        if self.jefe_golpes >= 3:
            self.evento_jefe() # Recarga la pantalla para mostrar la victoria
        else:
            self.texto_historia.config(text=f"¡Slash! Cortas al monstruo.\nGolpes dados: {self.jefe_golpes}/3")

    def finalizar_juego(self):
        self.limpiar_botones()
        self.actualizar_estado_superior()
        texto_final = ("Abres la puerta con la llave, obtienes tu título que está en un pedestal y ves una nota a la derecha que dice:\n\n"
                       "¡FELICIDADES! HAS COMPLETADO EL JUEGO BASE\n\n"
                       "Para descubrir qué es el 'Impuesto sobre la Renta', cómo se sobrevive a una jornada de 8 horas sin llorar y por qué tu jefe se parece tanto al monstruo que acabas de derrotar...\n\n"
                       "¡ADQUIERE EL DLC: VIDA ADULTA: 'MODO PESADILLA' por solo $11.99!")
        self.texto_historia.config(text=texto_final, fg="gold")

    def renderizar_nodo(self, mensaje_extra=""):
        self.limpiar_botones()
        self.actualizar_estado_superior()
        
        # Regla de Conocimiento: Si entra a 'O' sin llave, mostramos el rechazo de inmediato
        if self.nodo_actual.id == 'O' and "Llave Maestra" not in self.inventario:
            mensaje_extra += "\n\nSurge una criatura monstruosa de carpetas y tinta...\n'¡No puedes pasar! De seguro todavia debes el Servicio Social, no has certificado el de Ingles y ni el RFC tramitado tienes. ¡Fuera de aqui!'"

        self.texto_historia.config(text=mensaje_extra)

        # Factor de ramificacion dinamico (Movimientos basicos)
        if self.nodo_actual.izquierda:
            self.crear_boton(f"Mover a la Izquierda ({self.nodo_actual.izquierda.nombre})", lambda: self.mover('izq'))
        if self.nodo_actual.derecha:
            self.crear_boton(f"Mover a la Derecha ({self.nodo_actual.derecha.nombre})", lambda: self.mover('der'))
        if self.nodo_actual.padre:
            self.crear_boton("Retroceder (1 turno)", lambda: self.mover('atras'))

        # Eventos Especiales segun la base de conocimientos
        if self.nodo_actual.id == 'I':
            self.crear_boton("Acercarse a la Estanteria", self.evento_libreria)
            
        # Regla de Gemas: La opcion desaparece por completo si no hay mapa
        if self.nodo_actual.tiene_gema and not self.nodo_actual.gema_recolectada:
            if self.mapa_obtenido:
                self.crear_boton(f"Excavar y Tomar {self.nodo_actual.tipo_gema}", self.recolectar_gema)

        if self.nodo_actual.id == 'M':
            self.crear_boton("Leer Nota de la Maquina", self.leer_nota_forja)
            self.crear_boton("Insertar Gemas en Sinto-Gema 3000", self.evento_forja)
            
        # Regla del Jefe: Solo aparece la opcion de pelear si posee la llave
        if self.nodo_actual.id == 'O' and "Llave Maestra" in self.inventario:
            self.crear_boton("Enfrentar al Monstruo S.A.T.", self.evento_jefe)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = InterfazLaberinto(raiz)
    raiz.mainloop()