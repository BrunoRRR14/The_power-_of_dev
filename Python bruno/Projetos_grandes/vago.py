import tkinter as tk

def enviar(event=None):
    resposta = entry.get()
    print("Resposta enviada:", resposta)
    entry.delete(0, tk.END)  # Limpa o campo de texto

# Janela principal
root = tk.Tk()
root.title("Enviar com Enter")

# Caixa de entrada
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Botão de envio (opcional)
botao = tk.Button(root, text="Enviar", command=enviar)
botao.pack(pady=10)

# Associa o Enter à função 'enviar'
entry.bind("<Return>", enviar)

root.mainloop()
