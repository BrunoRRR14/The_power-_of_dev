import tkinter as tk
from tkinter import messagebox

# Função para processar o cadastro
def cadastrar():
    email = email_entry.get()
    cpf = cpf_entry.get()
    
    # Validação simples dos campos
    if not email or not cpf:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    else:
        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Cadastro realizado com sucesso!\nE-mail: {email}\nCPF: {cpf}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Cadastro")

# Configurando o layout
tk.Label(janela, text="E-mail:").grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(janela, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="CPF:").grid(row=1, column=0, padx=10, pady=10)
cpf_entry = tk.Entry(janela, width=30)
cpf_entry.grid(row=1, column=1, padx=10, pady=10)

# Botão de cadastro
cadastrar_button = tk.Button(janela, text="Cadastrar", command=cadastrar)
cadastrar_button.grid(row=2, column=1, padx=10, pady=10)

# Inicia o loop principal
janela.mainloop()
