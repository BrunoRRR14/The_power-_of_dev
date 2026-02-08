from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
import time
from time import sleep
from PIL import Image, ImageTk
import pygame
import threading


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




def type_text():
    """Função para simular a escrita do texto."""
    global current_index
    if current_index < len(full_text):
        text_label.config(text=full_text[:current_index + 1])  # Mostra o texto até o índice atual
        current_index += 1
        jogo.after(100, type_text)  # Chama a função novamente após 100ms

def ganhou_parabem():
    # Criar uma nova janela
    janela_mensagem = Toplevel(jogo)
    tocar_som_acerto()
    janela_mensagem.title("Parabens, acertou")
    janela_mensagem.geometry("400x500")
    janela_mensagem.configure(bg="lightblue")

    # Carregar a imagem
    image = Image.open(f"C:/Users/user/OneDrive/Área de Trabalho/CódigosBruno/jogo_forca1.0/perdeu.png")  # Substitua pelo caminho da sua imagem
    #image = image.resize((100, 100))  # Redimensiona a imagem (opcional)
    photo = ImageTk.PhotoImage(image)

    # Label para exibir a imagem
    image_label = Label(janela_mensagem, image=photo, bg="lightblue")
    image_label.image = photo  # Manter uma referência da imagem
    image_label.pack(pady=20)

    # Label para exibir a mensagem
    mensagem_label = Label(janela_mensagem, text="Ganhouuuu Parabens", font=("Arial", 12), bg="lightblue", fg="black")
    mensagem_label.pack(pady=10)
    
    

    # Botão para fechar a janela
    fechar_button = Button(janela_mensagem, text="Fechar", command=janela_mensagem.destroy)
    fechar_button.pack(pady=10)


def perdeu():
    # Criar uma nova janela
    tocar_som_erro()
    janela_perdeu = Toplevel(jogo)
    janela_perdeu.title("Parabens, você errou!")
    janela_perdeu.geometry("400x400")
    janela_perdeu.configure(bg="lightblue")

    # Carregar a imagem
    image = Image.open(f"C:/Users/user/OneDrive/Área de Trabalho/CódigosBruno/jogo_forca1.0/perdeu.jpg")  # Substitua pelo caminho da sua imagem
    #image = image.resize((100, 100))  # Redimensiona a imagem (opcional)
    photo = ImageTk.PhotoImage(image)

    # Label para exibir a imagem
    image_label = Label(janela_perdeu, image=photo, bg="lightblue")
    image_label.image = photo  # Manter uma referência da imagem
    image_label.pack(pady=20)

    # Label para exibir a mensagem
    mensagem_label = Label(janela_perdeu, text="Erouuuu!", font=("Arial", 12), bg="lightblue", fg="black")
    mensagem_label.pack(pady=10)

    # Botão para fechar a janela
    fechar_button = Button(janela_perdeu, text="Fechar", command=janela_perdeu.destroy)
    fechar_button.pack(pady=10)
    

    
    
    
    
def apurar_letra(event=None):
    global texto, tentativas
    letra = entrada_letra.get().lower()
    if letra in palavra and letra not in letras_testadas:
        # Substitui as ocorrências da letra na posição correta
        for i in range(len(palavra)):
            if palavra[i] == letra:
                texto = texto[:i] + letra + texto[i+1:]  # Substitui a posição da letra na palavra oculta
                entrada_letra.delete(0, tk.END)
        funcao_simples(texto)
        
    else:
        entrada_letra.delete(0, tk.END)
        if letra in letras_testadas:
            messagebox.showerror("Opa...", "Já tentou essa letra")
        else:
            messagebox.showerror("Errou", "Hahahaha")
            tentativas+= 1
            
    if "_" not in texto:
        ganhou_parabem()
        
    if letra in letras_testadas:
        pass
    else:
        letras_testadas.insert(-1, letra)  
    funcao_simples_2(letras_testadas)
    cont_tentativas(tentativas)
        
        
def funcao_simples(frase_atual):
    texto = (frase_atual)
    texto_final["text"] = texto
    
def funcao_simples_2(frase_2):
    texto = frase_2  # Corrigindo o nome da variável
    texto_final_2["text"] = texto
    
    
def cont_tentativas(tentei):
    if tentei >= len(palavra):
        perdeu()
    testo = f"Erros restantes: {len(palavra) - tentei}"  # Corrigindo o texto para mostrar a quantidade correta
    texto_t["text"] = testo
        
    
    
letras_testadas =[]
palavras = ["terremoto","significado","militar","atletismo","cercado","horas","sucesso","dobrado","verruga","lesma","professor", "celular","calcular","faca","loja", "escola", "tapete","geladeira", "bala", "teclado", "palavra", "pessoa", "palito", "marca","camiseta", "pesquisa", "cidade", "baleia", "contexto"]

palavra = random.choice(palavras)
 
quant_l = len(palavra)


jogo = tk.Tk()
jogo.title("jogo da forca")


jogo.configure(bg="lightblue")  # Define a cor de fundo da janela


# Obter a largura e altura da tela
screen_width = jogo.winfo_screenwidth()
screen_height = jogo.winfo_screenheight()

# Configurar a janela "jogo" para ocupar a metade esquerda da tela
jogo.geometry(f"{screen_width}x{screen_height}+0+0")

# Certifique-se de que ambas as janelas sejam exibidas corretamente
jogo.deiconify()
# tentativas :-)
tentativas = 0

# Texto completo e índice inicial
full_text = "Que comecem os jogos!"
current_index = 0

# Inicializa a palavra oculta com underscores
texto = "_" * len(palavra)

# Label para exibir o texto
text_label = tk.Label(jogo, text="", font=("Arial", 20),bg="lightblue", fg="black")
text_label.pack(pady=20)

# Carregar a imagem
image = Image.open(f"C:/Users/user/OneDrive/Área de Trabalho/CódigosBruno/jogo_forca1.0/capa.jpg")  # Substitua pelo caminho da sua imagem
image = image.resize((200, 200))  # Redimensiona a imagem (opcional)
photo = ImageTk.PhotoImage(image)

# Label para exibir a imagem
image_label = tk.Label(jogo, image=photo, bg="lightblue")
image_label.pack(pady=20)  # Espaçamento entre a imagem e os outros elementos


# Label de texto da letra
letra = Label(jogo, text= f"Adivinhe a palavra de {quant_l} letras", font=(16),bg="lightblue", fg="black")
letra.pack(pady=10)


# Label de texto da letra
letra = Label(jogo, text= "Digite a letra:", font=(8),bg="lightblue", fg="black")
letra.pack(pady=10)

# Entrada da letra
entrada_letra= Entry(jogo, width=5)
entrada_letra.pack(pady=5)


# Botão pra enviar a letra
botao_submeter = tk.Button(jogo, text="Enviar", command=apurar_letra)
botao_submeter.pack(pady=5)

# Associa o Enter à função 'enviar'
entrada_letra.bind("<Return>", apurar_letra)

# O texto que mostra a situação da palavra
texto_final = Label(jogo, text="", font= (120),bg="lightblue", fg="black")
texto_final.pack(pady=20)

# o texto que mostra as letras que ja foram
texto_final_2 = Label(jogo, text="", font= (120),bg="lightblue", fg="black")
texto_final_2.pack(pady=20)

# o testo que mostra a quantidade de tentativas
texto_t = Label(jogo, text="", font= (120),bg="lightblue", fg="black")
texto_t.pack(pady=20)

# Inicia a animação
jogo.after(500, type_text)  # Aguarda 500ms antes de iniciar


jogo.mainloop()

print(palavra)