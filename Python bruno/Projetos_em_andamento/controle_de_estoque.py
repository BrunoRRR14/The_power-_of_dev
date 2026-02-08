# importando tudo que precisa

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from time import sleep
import openpyxl
from openpyxl import Workbook
import time
import locale
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

def novo(event):
    preco_unitario_entry.focus_set()  # Muda o foco para o próximo campo

#criando as listas que seram usadas
dados = {
    "Produtos": [],
    "Precos_unitarios": [],
}
titulos = ["Produtos", "Precos_unitarios"]
titu = "Relatório de estoque"
# funcão pra textos no fundo de caixas de texto
def placeholder(entry, texto):
    entry.insert(0, texto)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == texto:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, texto)
            entry.config(fg="grey")
        
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# função lista de produtos
def lista_de_produtos(dicio):
     pass




# funcao do relogio
def atualizar_horario():
    # Obtém o horário atual no formato desejado
    horario_atual = time.strftime("%H:%M:%S")
    label_horario.config(text=horario_atual)  # Atualiza o texto do rótulo
    tela_de_gerenciamento.after(1000, atualizar_horario)  # Reagenda a função para ser chamada em 1 segundo

# funcao que adiciona itens
def adicionar_itens(dicio):
    produto = produto_entry.get()
    preco_unitario = preco_unitario_entry.get()
    if produto == "" or preco_unitario == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos")
    else:
        dicio["Produtos"].append(produto)
        dicio["Precos_unitarios"].append(preco_unitario)
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso")
        #produto_entry.delete(0, END)
        #preco_unitario_entry.delete(0, END)
        #sleep(1)
        #tela_de_gerenciamento.destroy()




def remover_itens(dicio):
    produto = produto_entry.get()
    if produto == "":
        messagebox.showerror("Erro", "Por favor, preencha o campo necessário")
    else:
        cont_1 = 0
        for prod in dicio["Produtos"]:  
            if produto == prod:
                i = dicio["Produtos"].index(prod)
                dicio["Produtos"].remove(prod    )
                dicio["Precos_unitarios"].pop(i)
                messagebox.showinfo("Sucesso", "Produto removido com sucesso")
                produto_entry.delete(0, END)
                #preco_unitario_entry.delete(0, END)
                sleep(1)
                cont_1+= 1
                #tela_de_gerenciamento.destroy()
            else:
                cont_1+= 0
                pass
            if cont_1 == 0:
                messagebox.showerror("Erro", "Produto nao encontrado")
                #produto_entry.delete(0, END)
                #preco_unitario_entry.delete(0, END)
                sleep(1)
                #tela_de_gerenciamento.destroy()

def ad_e_rem():
    '''Adiciona itens a lista

    Parameters:
        None

    Returns:
        None
    '''
    op_1 = opcao_add_rem.get()
    if op_1 == " ":
        messagebox.showerror("Erro", "Por favor, selecione se deseja adicionar ou remover algum item")
    elif op_1 == "Adicionar":
        adicionar_itens(dados)
    elif op_1 == "Remover":
        remover_itens(dados)
    else:
        messagebox.showerror("Erro", "Por favor, selecione se deseja adicionar ou remover algum item")
    
    
    
    
    
tela_de_gerenciamento = tk.Tk()
tela_de_gerenciamento.title("Layout de controle de estoque")
tela_de_gerenciamento.geometry("400x200")

#opção de adicionar ou remover produto
opcao_add_rem = ttk.Combobox(tela_de_gerenciamento, values=[" ","Adicionar", "Remover"], state="readonly")
opcao_add_rem.current(0)
opcao_add_rem.pack(pady=5)
#1.600.000,00

#Caixa de texto para receber o nome do produto
produto_entry = Entry(tela_de_gerenciamento, width=23)
produto_entry.pack(pady=5)
produto_entry.bind("<Return>", novo)
placeholder(produto_entry, "Nome do produto")

#Caixa de texto para receber o preco do produto
preco_unitario_entry = Entry(tela_de_gerenciamento, width=23)
preco_unitario_entry.pack(pady=5)
preco_unitario_entry.bind("<Return>", lambda event: ad_e_rem())
placeholder(preco_unitario_entry, "Precos unitários")

#Botão para submeter e os produtos e adicionar ações
botao_submeter = tk.Button(tela_de_gerenciamento, text="Enviar", command=ad_e_rem)
botao_submeter.pack(pady=5)

# data no fim da tela


tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B %Y", tempo_em_struct)
texto_2 = Label(tela_de_gerenciamento, text=tempo_formatado)
texto_2.pack(pady=15)

# Cria um rótulo para exibir o horário
label_horario = tk.Label(tela_de_gerenciamento, text="", font=("Helvetica", 12))
label_horario.pack(pady=1)

# Inicia a atualização do horário
atualizar_horario()



tela_de_gerenciamento.mainloop()

# criando grafico

# Cria um novo workbook
wb = Workbook()

# Seleciona a planilha ativa (por padrão, a primeira planilha é ativa)
ws = wb.active

# Define um título para a planilha
ws.title = titu

# Adiciona os títulos na primeira linha da planilha
ws.append(titulos)

# Determina o número de linhas a partir dos dados
# num_linhas = len(dados["Produtos"])
num_linhas = 0
for prod in dados["Produtos"]:  
    num_linhas+= 1
# Adiciona os dados nas linhas subsequentes
for i in range(num_linhas):
    linha = [dados[titulo][i] for titulo in titulos]
    ws.append(linha)

# Salva o workbook em um arquivo
wb.save("planilha_teste.xlsx")
