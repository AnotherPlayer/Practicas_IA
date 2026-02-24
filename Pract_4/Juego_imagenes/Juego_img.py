import tkinter as tk
import random
import os

# 1. Base de conocimiento (Representación basada en reglas)
RULES = {
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Humano"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Humano", "Papel"],
    "Humano": ["Tijera", "Piedra"]
}

# 2. Memoria del agente (Estado interno)
scores = {"user": 0, "bot": 0, "ties": 0}

# 3. Función de decisión (Actuador del agente)
def play(user):
    cpu = random.choice(list(RULES.keys()))
    
    if user == cpu:
        res = f"Empate: ambos eligieron {user}"
        scores["ties"] += 1
    elif cpu in RULES[user]:
        res = f"Ganaste. {user} vence a {cpu}"
        scores["user"] += 1
    else:
        res = f"Perdiste. {cpu} vence a {user}"
        scores["bot"] += 1

    # Actualizar la interfaz
    lbl_result.config(text=res)
    lbl_score.config(text=f"Usuario: {scores['user']}  |  Máquina: {scores['bot']}  |  Empates: {scores['ties']}")

# --- 4. Entorno de Trabajo (Interfaz Gráfica) ---
root = tk.Tk()
root.title("Edición Sheldon: Piedra, Papel, Tijera, Lagarto, Humano")
root.geometry("800x600") # Tamaño de ventana ajustado
root.configure(bg="#2b2b2b")

# Título
tk.Label(root, text="¡Haz tu jugada!", font=('Courier New', 20, 'bold'), bg="#2b2b2b", fg="#f39c12").pack(pady=20)

# Contenedor de botones
frame_buttons = tk.Frame(root, bg="#2b2b2b")
frame_buttons.pack(pady=10)

# Manejo de rutas y memoria de imágenes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images = {} 

# Creación de botones dinámicos
for opt in RULES.keys():
    try:
        # Cargar imagen
        img_path = os.path.join(BASE_DIR, f"{opt.lower()}.png")
        img = tk.PhotoImage(file=img_path)
        
        # PREPROCESAMIENTO: Reducir la imagen para que encaje en la UI
        img = img.subsample(4, 4) 
        
        images[opt] = img 
        
        # Asignar imagen y texto al botón (compound=tk.TOP pone la imagen arriba)
        btn = tk.Button(frame_buttons, text=opt, image=img, compound=tk.TOP,
                        command=lambda o=opt: play(o), bg="#2b2b2b", fg="#f39c12", 
                        font=('Courier New', 12, 'bold'), activebackground="#e74c3c", 
                        borderwidth=0, cursor="hand2", pady=5)
    except tk.TclError:
        # Plan B en caso de error de lectura de archivo
        btn = tk.Button(frame_buttons, text=opt, font=('Courier New', 12, 'bold'), 
                        command=lambda o=opt: play(o), bg="#f39c12", fg="#2b2b2b", width=8, height=2)
    
    btn.pack(side=tk.LEFT, padx=10)

# Etiquetas de Resultados y Marcador
lbl_result = tk.Label(root, text="Esperando tu movimiento...", font=('Courier New', 14), bg="#2b2b2b", fg="white")
lbl_result.pack(pady=30)

lbl_score = tk.Label(root, text="Usuario: 0  |  Máquina: 0  |  Empates: 0", font=('Courier New', 16, 'bold'), bg="#2b2b2b", fg="#3498db")
lbl_score.pack(pady=10)

root.mainloop()