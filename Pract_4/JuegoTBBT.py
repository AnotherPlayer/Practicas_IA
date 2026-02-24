import tkinter as tk
import random

# Reglas: cada llave vence a los valores en su lista
RULES = {
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Humano"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Humano", "Papel"],
    "Humano": ["Tijera", "Piedra"] # Humano reemplaza a Spock
}

def play(user):
    cpu = random.choice(list(RULES.keys()))
    if user == cpu:
        res = f"Empate: ambos elegisteis {user}"
    else:
        # Si la elección de la CPU está en la lista de lo que el usuario vence: Gana Usuario
        res = f"¡Ganaste! {user} vence a {cpu}" if cpu in RULES[user] else f"Perdiste: {cpu} vence a {user}"
    lbl.config(text=res)

# Interfaz Gráfica
root = tk.Tk()
root.title("Piedra, Papel, Tijera, Lagarto, Humano")
lbl = tk.Label(root, text="Selecciona tu jugada", font=('Arial', 12))
lbl.pack(pady=10)

# Generación de botones en una línea para ahorrar espacio
for opt in RULES.keys():
    tk.Button(root, text=opt, command=lambda o=opt: play(o)).pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()