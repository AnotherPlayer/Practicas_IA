# 🧠 Algoritmo Minimax: La Lógica "Invencible" del Gato

Este documento explica cómo funciona la Inteligencia Artificial (IA) implementada en el juego del Gato (Tic-Tac-Toe). El algoritmo utilizado se llama **Minimax**.

---

## 1. El Concepto Fundamental
Para entender Minimax, imagina al **Doctor Strange** en *Infinity War*. Él no adivina; él mira millones de futuros posibles para encontrar el único camino donde ganan.

Minimax hace exactamente eso:
1.  **Simula** todas las jugadas posibles desde el estado actual del tablero.
2.  **Simula** todas las respuestas posibles de tu oponente.
3.  **Simula** tus respuestas a esas respuestas...
4.  Continúa así hasta que el juego termina (victoria, derrota o empate).

Esto genera un **Árbol de Decisiones** completo.

---

## 2. Los Roles: MAX y MIN
El algoritmo asume que hay dos jugadores con objetivos opuestos:

### 🤖 El Jugador MAX (La IA)
* Su objetivo es **Maximizar** la puntuación.
* Quiere obtener el número más alto posible (ganar).

### 👤 El Jugador MIN (El Humano)
* La IA asume que el humano es perfecto y quiere ganar.
* Por lo tanto, el humano quiere **Minimizar** la puntuación de la IA.
* Quiere obtener el número más bajo posible (hacer perder a la IA).

---

## 3. Sistema de Puntuación
Cuando la simulación llega al final de una partida (un "nodo hoja" del árbol), se asigna una puntuación:

| Resultado | Puntos | Significado para la IA |
| :--- | :---: | :--- |
| **Gana la IA** | **+10** | ¡El mejor escenario! (MAX) |
| **Empate** | **0** | Neutral. Mejor que perder. |
| **Gana Humano** | **-10** | ¡El peor escenario! (MIN) |

---

## 4. El Flujo de Decisión (Paso a Paso)

Supongamos que es el turno de la IA y tiene dos casillas disponibles (**A** y **B**).

### Paso 1: Simulación de la Opción A
1.  La IA coloca su ficha en **A** imaginariamente.
2.  Ahora es el turno del Humano (**MIN**).
3.  El algoritmo ve que el Humano tiene una jugada ganadora inmediata.
4.  Como el Humano es inteligente, elegirá ganar.
5.  **Resultado de la rama A: -10** (La IA pierde).

### Paso 2: Simulación de la Opción B
1.  La IA coloca su ficha en **B** imaginariamente.
2.  Ahora es el turno del Humano (**MIN**).
3.  El algoritmo ve que el Humano *no* puede ganar, y el juego terminará en empate.
4.  **Resultado de la rama B: 0** (Empate).

### Paso 3: La Elección (Backpropagation)
La IA compara los futuros posibles:
* Camino A = -10
* Camino B = 0

> **Decisión:** Como la IA es **MAX** (busca el valor más alto), elige el **Camino B**. Prefiere empatar (0) antes que perder (-10).

---

## 5. Diagrama Visual del Árbol

```text
                     [Estado Actual]
                       (Turno IA)
                     /            \
             [Opción A]          [Opción B]
            (Simulación)        (Simulación)
                 |                   |
           [Turno Humano]      [Turno Humano]
           (Juega Perfecto)    (Juega Perfecto)
                 |                   |
           [GANA HUMANO]         [EMPATE]
           (Valor: -10)         (Valor: 0)

      -----------------------------------------
      DECISIÓN FINAL:
      La IA compara (-10 vs 0) y elige 0.
      --> La IA juega la Opción B.