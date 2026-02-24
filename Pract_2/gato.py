import tkinter as tk
from tkinter import messagebox

HUM = "X"
PC  = "O"
VACIO = " "

lineas = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

class Gato:
    def __init__(self, root):
        self.root = root
        root.title("Gato")

        self.tab = [VACIO]*9
        self.bloqueado = False

        self.lbl = tk.Label(root, text="Tú: X   |   PC: O", font=("Arial", 14))
        self.lbl.grid(row=0, column=0, columnspan=3, pady=10)

        self.info = tk.Label(root, text="La computadora inicia", font=("Arial", 12))
        self.info.grid(row=1, column=0, columnspan=3, pady=(0,10))

        self.botones = []
        for i in range(9):
            b = tk.Button(root, text="", font=("Arial", 22), width=4, height=2,
                          command=lambda i=i: self.jugar_humano(i))
            b.grid(row=2 + i//3, column=i%3, padx=5, pady=5)
            self.botones.append(b)

        self.btn_reset = tk.Button(root, text="Reiniciar", command=self.reiniciar)
        self.btn_reset.grid(row=5, column=0, columnspan=3, pady=10)

        #LA PC EMPIEZA EN EL CENTRO
        self.root.after(200, self.inicio_pc)

    def inicio_pc(self):
        self.poner(4, PC)
        self.info.config(text="Tu turno")

    def ganador(self, j):
        for a,b,c in lineas:
            if self.tab[a] == self.tab[b] == self.tab[c] == j:
                return True
        return False

    def lleno(self):
        return VACIO not in self.tab

    def casi_gana(self, j):
        for a,b,c in lineas:
            vals = [self.tab[a], self.tab[b], self.tab[c]]
            if vals.count(j) == 2 and vals.count(VACIO) == 1:
                if self.tab[a] == VACIO: return a
                if self.tab[b] == VACIO: return b
                return c
        return None

    def mejor_mov_pc(self):
        i = self.casi_gana(PC)
        if i is not None: return i

        i = self.casi_gana(HUM)
        if i is not None: return i

        for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
            if self.tab[i] == VACIO:
                return i
        return None

    def poner(self, i, j):
        self.tab[i] = j
        self.botones[i].config(text=j, state="disabled")

    def terminar(self, msg):
        self.bloqueado = True
        self.info.config(text=msg)
        for b in self.botones:
            b.config(state="disabled")

    def jugar_humano(self, i):
        if self.bloqueado or self.tab[i] != VACIO:
            return

        self.poner(i, HUM)

        if self.ganador(HUM):
            self.terminar("Ganaste")
            messagebox.showinfo("Fin", "Ganaste.")
            return

        if self.lleno():
            self.terminar("Empate")
            messagebox.showinfo("Fin", "Empate.")
            return

        self.info.config(text="Turno de la PC...")
        self.root.after(250, self.jugar_pc)

    def jugar_pc(self):
        if self.bloqueado:
            return

        i = self.mejor_mov_pc()
        if i is None:
            self.terminar("Empate")
            messagebox.showinfo("Fin", "Empate.")
            return

        self.poner(i, PC)

        if self.ganador(PC):
            self.terminar("Ganó la PC")
            messagebox.showinfo("Fin", "Ganó la computadora.")
            return

        if self.lleno():
            self.terminar("Empate")
            messagebox.showinfo("Fin", "Empate.")
            return

        self.info.config(text="Tu turno")

    def reiniciar(self):
        self.tab = [VACIO]*9
        self.bloqueado = False
        self.info.config(text="La computadora inicia")
        for b in self.botones:
            b.config(text="", state="normal")
        self.root.after(200, self.inicio_pc)


if __name__ == "__main__":
    root = tk.Tk()
    app = Gato(root)
    root.mainloop()
