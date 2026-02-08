import tkinter as tk
import random

# ---------------- CONFIGURAÇÕES ---------------- #

PALAVRAS = {
    3: ["Natal", "Papai Noel", "Rena", "Elfo", "Estrela", "Galinha", "Coiote", "Baiano" , "Rei", "Árvore", "Furadeira", "Presente", "Árvore de Natal", "Sino", "Neve", "Japão", "Teclado", "Livro", "Lula" , "Fogo", "Gorro", "Trenó", "Tubarão", "Padre", "Ovo", "Dente"],
    4: ["Presente", "Árvore de Natal", "Sino", "Neve", "Japão", "Teclado", "Livro", "Lula" , "Fogo", "Gorro", "Trenó", "Tubarão", "Padre", "Ovo", "Dente"],
    5: ["Ceia", "Luzinhas", "Estrela", "Gorro", "Trenó", "Tubarão", "Padre", "Ovo", "Dente",  "Sino", "Neve", "Japão", "Teclado", "Livro", "Lula" , "Fogo"]
}

# ---------------- APLICAÇÃO ---------------- #

class JogoImpostor:
    def __init__(self, root):
        self.root = root
        self.root.title("🎄 Impostor de Natal 🎄")
        self.root.geometry("400x300")

        self.jogadores = 0
        self.palavras_sorteadas = []
        self.jogador_atual = 0

        self.tela_inicio()

    # -------- TELAS -------- #

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_inicio(self):
        self.limpar_tela()

        tk.Label(self.root, text="🎅 Impostor de Natal 🎅", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text="Quantos jogadores?", font=("Arial", 12)).pack(pady=10)

        for qtd in [3, 4, 5]:
            tk.Button(
                self.root,
                text=f"{qtd} Jogadores",
                width=20,
                command=lambda q=qtd: self.iniciar_jogo(q)
            ).pack(pady=5)

    def iniciar_jogo(self, qtd):
        self.jogadores = qtd
        palavras = PALAVRAS[qtd].copy()

        impostor = random.randint(0, qtd - 1)
        palavra_base = random.choice(palavras)

        self.palavras_sorteadas = []
        for i in range(qtd):
            if i == impostor:
                self.palavras_sorteadas.append("IMPOSTOR")
            else:
                self.palavras_sorteadas.append(palavra_base)

        random.shuffle(self.palavras_sorteadas)
        self.jogador_atual = 0

        self.tela_jogador()

    def tela_jogador(self):
        self.limpar_tela()

        tk.Label(
            self.root,
            text=f"Jogador {self.jogador_atual + 1}",
            font=("Arial", 16)
        ).pack(pady=20)

        self.label_palavra = tk.Label(self.root, text="❓", font=("Arial", 20))
        self.label_palavra.pack(pady=20)

        tk.Button(
            self.root,
            text="Ver Palavra",
            width=20,
            command=self.mostrar_palavra
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Esconder e Passar",
            width=20,
            command=self.proximo_jogador
        ).pack(pady=5)

    # -------- AÇÕES -------- #

    def mostrar_palavra(self):
        self.label_palavra.config(
            text=self.palavras_sorteadas[self.jogador_atual]
        )

    def proximo_jogador(self):
        self.jogador_atual += 1

        if self.jogador_atual < self.jogadores:
            self.tela_jogador()
        else:
            self.tela_fim()

    def tela_fim(self):
        self.limpar_tela()

        tk.Label(
            self.root,
            text="🎉 Todos receberam suas palavras!",
            font=("Arial", 14)
        ).pack(pady=30)

        tk.Label(
            self.root,
            text="Agora conversem e descubram o impostor 👀",
            font=("Arial", 11)
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Jogar Novamente",
            command=self.tela_inicio
        ).pack(pady=20)

# ---------------- EXECUÇÃO ---------------- #

root = tk.Tk()
app = JogoImpostor(root)
root.mainloop()
