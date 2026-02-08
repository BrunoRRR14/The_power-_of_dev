from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import pygame
import threading


# Variáveis globais
tabuada = ""
tabuadas = []
tabuadas_q_foram = []
text_var = None  # Será inicializada depois

def tocar_som_acerto():
    def tocar():
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/user/Downloads/duo.mp3")  # Caminho do seu som
        pygame.mixer.music.play()
    threading.Thread(target=tocar).start()

def tocar_som_erro():
    def reproduzir():
        pygame.mixer.init()
        random_number = random.randint(1, 2)
        if random_number == 1:
            pygame.mixer.music.load("C:/Users/user/Downloads/errou_2.mp3")  # Caminho do seu som
        else:
            pygame.mixer.music.load("C:/Users/user/Downloads/errou.mp3")  # Caminho do seu som
        pygame.mixer.music.play()
    threading.Thread(target=reproduzir).start()



def ganhou_parabem():
    # Criar uma nova janela
    janela_mensagem = Toplevel(jogo)
    janela_mensagem.title("Parabéns, acertou!")
    janela_mensagem.geometry("400x500")
    janela_mensagem.configure(bg="lightblue")

    # Carregar a imagem
    image = Image.open("C:/Users/user/OneDrive/Área de Trabalho/CódigosBruno/jogo_forca1.0/perdeu.png")  # Substitua por imagem de vitória, se quiser
    photo = ImageTk.PhotoImage(image)

    # Label para exibir a imagem
    image_label = Label(janela_mensagem, image=photo, bg="lightblue")
    image_label.image = photo
    image_label.pack(pady=20)

    # Mensagem de parabéns
    mensagem_label = Label(janela_mensagem, text="Ganhouuuu Parabéns!", font=("Arial", 12), bg="lightblue", fg="black")
    mensagem_label.pack(pady=10)

    # Botão para fechar a janela
    fechar_button = Button(janela_mensagem, text="Fechar", command=janela_mensagem.destroy)
    fechar_button.pack(pady=10)

def apurar(event=None):
    global tabuada, tabuadas_q_foram
    numero = entrada_letra.get()
    calculo = tabuada.replace("x", "*")
    resultado = eval(calculo)
    
    if numero.isdigit() and int(numero) == resultado:
        tocar_som_acerto()
        ganhou_parabem()
        tabuadas_q_foram.append(tabuada)
        entrada_letra.delete(0, END)
        cerebro()
    else:
        messagebox.showerror("Errou", f"O resultado não é {numero}")
        entrada_letra.delete(0, END)
        tocar_som_erro()

def cerebro(event=None):
    global tabuada, tabuadas, text_var

    if not tabuadas:  # Carrega apenas uma vez
        tabuadas = [f"{i} x {j}" for i in range(1, 11) for j in range(1, 11)]
        random.shuffle(tabuadas)

    if tabuadas:
        tabuada = tabuadas.pop()
        text_var.set(tabuada)
    else:
        text_var.set("Você terminou todas as tabuadas!")
        messagebox.showinfo("Fim de jogo", "Parabéns! Você completou todas as tabuadas.")

# Criando janela principal
jogo = tk.Tk()
jogo.title("Jogo das Tabuadas")
jogo.configure(bg="lightblue")

# Ocupa a tela inteira
screen_width = jogo.winfo_screenwidth()
screen_height = jogo.winfo_screenheight()
jogo.geometry(f"{screen_width}x{screen_height}+0+0")

# Variável de texto para exibir a tabuada
text_var = tk.StringVar()
text_var.set("Carregando...")

# Label da tabuada
label_tabuada = tk.Label(jogo, textvariable=text_var, font=("Arial", 20), bg="lightblue", fg="black")
label_tabuada.pack(pady=160)

# Campo de entrada da resposta
entrada_letra = tk.Entry(jogo, width=5, font=("Arial", 16))
entrada_letra.pack(pady=10)
entrada_letra.bind("<Return>", apurar)

# Botão de envio
botao_submeter = tk.Button(jogo, text="Enviar", font=("Arial", 12), command=apurar)
botao_submeter.pack(pady=5)

# Começar automaticamente a primeira tabuada após iniciar
jogo.after(500, cerebro)

# Iniciar loop principal
jogo.mainloop()
