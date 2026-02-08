from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def novo(event):
    email.focus_set()  # Muda o foco para o próximo campo

def interprete():
    nome_aqui = nome.get()
    usando_aqui = combo_origem.get()
    usar_email = email.get()

    # Inicializando condições
    cond_1 = cond_2 = cond_3 = False

    # Verifica se o nome foi preenchido
    if not nome_aqui.strip():
        messagebox.showerror("Erro", "Campo nome não foi preenchido.")
    else:
        cond_1 = True

    # Verifica se o gênero é válido
    if usando_aqui in ["Masculino", "Feminino", "Outro"]:
        cond_2 = True
    else:
        messagebox.showerror("Erro", "Gênero não identificado.")

    # Verifica se o email é válido
    if "@" in usar_email and usar_email[0] not in ["@", "."] and "mail.com" in usar_email:
        if not any(letra.isupper() for letra in usar_email):  # Checa se tem letra maiúscula
            cond_3 = True
        else:
            messagebox.showerror("Erro", "Email tem letras maiúsculas.")
    else:
        messagebox.showerror("Erro", "Email inválido.")

    # Verifica se todas as condições foram atendidas
    if cond_1 and cond_2 and cond_3:
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

cadastro = Tk()
cadastro.title("Tela de cadastro")

# Campos do formulário
nome = Entry(cadastro, width=30)
nome.grid(column=1, row=0, padx=10, pady=10)
nome.bind("<Return>", novo)  # Move para o próximo campo ao pressionar Enter

email = Entry(cadastro, width=30)
email.grid(column=1, row=1, padx=10, pady=10)
email.bind("<Return>", lambda event: interprete())  # Chama a função sem erro

combo_origem = ttk.Combobox(cadastro, values=["Masculino", "Feminino", "Outro"], state="readonly")
combo_origem.current(0)
combo_origem.grid(column=1, row=2, padx=10, pady=10)

# Botão para enviar
botao_d_enviar = Button(cadastro, text="Enviar", command=interprete)
botao_d_enviar.grid(column=1, row=3, padx=10, pady=10)

# Labels
Label(cadastro, text="Nome:").grid(column=0, row=0, padx=10, pady=10)
Label(cadastro, text="E-mail:").grid(column=0, row=1, padx=10, pady=10)
Label(cadastro, text="Gênero:").grid(column=0, row=2, padx=10, pady=10)

cadastro.mainloop()
