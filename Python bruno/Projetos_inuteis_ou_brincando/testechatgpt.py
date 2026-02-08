import tkinter as tk
import time

def atualizar_horario():
    # Obtém o horário atual no formato desejado
    horario_atual = time.strftime("%H:%M:%S")
    label_horario.config(text=horario_atual)  # Atualiza o texto do rótulo
    root.after(1000, atualizar_horario)  # Reagenda a função para ser chamada em 1 segundo

# Cria a janela principal
root = tk.Tk()
root.title("Relógio Atualizado em Tempo Real")

# Cria um rótulo para exibir o horário
label_horario = tk.Label(root, text="", font=("Helvetica", 48))
label_horario.pack(pady=20)

# Inicia a atualização do horário
atualizar_horario()

# Inicia o loop principal do tkinter
root.mainloop()
