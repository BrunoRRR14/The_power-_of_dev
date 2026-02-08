# Projeto de jogo da forca com niveis
from tkinter import * # layout
import tkinter as tk # layout
from tkinter import messagebox # mensagens de erro
import random # sorteio de palavras
import time # relogio e timer
from time import sleep # tempo pra tudo
from PIL import Image, ImageTk # importar imagens
import cv2 # importar video
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Texto completo e índice inicial
full_text = "Seja bem vindo ao jogo!"
current_index = 0

def novo(event):
    nome.focus_set()

def type_text(text_label):
    """Função para simular a escrita do texto."""
    global current_index
    if current_index < len(full_text):
        text_label.config(text=full_text[:current_index + 1])  # Mostra o texto até o índice atual
        current_index += 1
        text_label.after(100, lambda: type_text(text_label))


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




def cadastro():
    global nome, email, senha
    tela_de_cadastro = Toplevel(principal)
    tela_de_cadastro.title("Bem vindo!")
    largura_tela = principal.winfo_screenwidth()
    altura_tela = principal.winfo_screenheight()
    
    
    # Calcula as coordenadas para centralizar a janela
    pos_x = (largura_tela - 668) // 2
    pos_y = (altura_tela -668) // 2
    tela_de_cadastro.geometry(f"{668}x{668}+{pos_x}+{pos_y}")
    tela_de_cadastro.configure(bg="lightblue")
    
    # Label para exibir o texto
    text_label = tk.Label(tela_de_cadastro, text="", font=("Arial", 20),bg="lightblue", fg="black")
    text_label.pack(pady=20)
    
    nome = Entry(tela_de_cadastro,width =23)
    nome.pack(pady=10)
    nome.bind("<Return>", novo)
    placeholder(nome, "Seu nome aqui")
    
    email = Entry(tela_de_cadastro,width =23)
    email.pack(pady=10)
    placeholder(email, "Seu email aqui")

    senha = Entry(tela_de_cadastro,width =23)
    senha.pack(pady=10)
    placeholder(senha, "Sua senha")
    tela_de_cadastro.after(500, type_text(text_label))
    
    botao_submeter = tk.Button(tela_de_cadastro, text="Enviar", command=apurar_e_enviar)
    botao_submeter.pack(pady=5)
    
    
    
    
def apurar_e_enviar():
    name = nome.get()
    mail = email.get()
    password = senha.get()
    name = name.strip()
    itens_aceitos = 0 
    caracteres_especias =[" ","(","?","= ",". ","[","!","$","%","^","&","(",")","/"]
    cont = 0
    erros = 0
    erros_2 =0
        
    for letrinha in name:
        if letrinha == name[0]:
            if not letrinha.isupper():
                erros+= 1
        elif letrinha == " ":
            if not name[name.index(letrinha) + 1].isupper():
                erros+=1
        if letrinha.isupper() and name[name.index(letrinha) -1] != " " and not name[name.index(letrinha) - 1].isupper()  and letrinha != name[0]:
            erros_2 +=1


    if erros != 0 and erros_2 != 0:
        messagebox.showerror("Lembre-se"," Nomes próprios começam com letras maiusculas e letras maiusculas devem ser encontradas no começo das palavras, não no meio.")
        return
    elif erros != 0 or erros_2 != 0:
        if erros != 0:
            messagebox.showerror("Lembre-se","Nomes próprios começam com letras maiusculas")
            return
        else:
            if erros_2 != 0:
                messagebox.showerror("Letras maiusculas devem ser encontradas no começo das palavras, não no meio")
                return
    else:
        itens_aceitos+= 1
        
        
    if "@" not in mail or not (mail.endswith(".com") or mail.endswith(".com.br")):
        messagebox.showerror("Erro", "Estrutura do e-mail é invalida")
        return
    elif not any(provider in mail for provider in ["gmail", "hotmail", "outlook", "yahoo"]):
        messagebox.showerror("Erro", "Use um e-mail pessoal sem ligações com empresas ou universidades.")
        return
    else:
        itens_aceitos += 1

    if any(letra in password for letra in caracteres_especias):
        messagebox.showerror("Erro", "A senha não deve conter caracteres especiais.")
        return
    else:
        itens_aceitos += 1

    if itens_aceitos == 3:
        messagebox.showinfo("Sucesso", "Agora vamos para a etapa de verificação de e-mail.")
        enviar_email()
    else:
        messagebox.showerror("Erro", "Algumas informações estão erradas, tente novamente.")



def exibir_video():
    # Carregar o vídeo com OpenCV
    cap = cv2.VideoCapture(f"C:/Users/user/Downloads/Logo.mp4")
    
    # Função para exibir os quadros do vídeo
    def mostrar_quadro():
        ret, frame = cap.read()
        if ret:
            # Converter o frame para o formato RGB (Tkinter usa RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame)
            frame_tk = ImageTk.PhotoImage(frame_pil)

            # Atualizar o rótulo com o novo frame
            label_video.config(image=frame_tk)
            label_video.image = frame_tk
            principal.after(10, mostrar_quadro)  # Mostrar o próximo quadro após 10 ms
        else:
            # Fechar o vídeo após a exibição
            cap.release()
            cadastro()
            

    # Iniciar a exibição dos quadros
    mostrar_quadro()

def enviar_email():
    global codigo_confirmacao
    cod_1 = random.randint(1, 100)
    cod_2 = random.randint(1, 100)
    cod_3 = random.randint(1, 100)
    cod_4 = random.randint(1, 100)
    codigo_confirmacao = f"{cod_1}{cod_2}{cod_3}{cod_4}"
    remetente = "brunorrr14@gmail.com"  # Substitua pelo seu e-mail
    chave = "uvaf wvtl scwo ibau"  # Substitua pela sua senha de aplicativo gerada
    destinatario = email.get()  # Substitua pelo destinatário


    # Configurar o e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Email de verificação"
    corpo = f"Olá {nome.get()}\n\n\nSeja bem vindo ao jogo, antes de começarmos precisamos que digite o seguinte código para confirmar seu cadastro: {codigo_confirmacao} \n\n\nObrigado e seja bem vindo"
    


    # Adicionar o corpo ao e-mail
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remetente, chave)  # Use a chave de aplicativo aqui
        print("Login bem-sucedido!")
        server.sendmail(remetente, destinatario, mensagem.as_string())  # Enviar o e-mail
        print("E-mail enviado com sucesso!")
        confirmacao()
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
    finally:
        server.quit()
    
def confirmacao():
    global tentativa
    tela_de_confirmacao = Toplevel(principal)
    tela_de_confirmacao.title("Confirme que é você")
    largura_tela = principal.winfo_screenwidth()
    altura_tela = principal.winfo_screenheight()
    
    
    # Calcula as coordenadas para centralizar a janela
    pos_x = (largura_tela - 368) // 2
    pos_y = (altura_tela -368) // 2
    tela_de_confirmacao.geometry(f"{368}x{368}+{pos_x}+{pos_y}")
    tela_de_confirmacao.configure(bg="lightblue")
    
    # Label para exibir o texto
    texto_de_inicio_da_confirmacao = tk.Label(tela_de_confirmacao, text="Verifique seu email", font=("Arial", 20),bg="lightblue", fg="black")
    texto_de_inicio_da_confirmacao.pack(pady=20)
    
    tentativa = Entry(tela_de_confirmacao,width =23)
    tentativa.pack(pady=10)
    placeholder(tentativa, "Digite o código aqui")
    
    botao_submeter = tk.Button(tela_de_confirmacao, text="Enviar", command=finalizar)
    botao_submeter.pack(pady=5)

    
    
def finalizar():
    chave_usu = tentativa.get()
    if chave_usu == codigo_confirmacao:
        messagebox.showinfo("Finalmente","Cadastro realizado com sucesso")
        parabens()
        time.sleep(10)
        principal.destroy()
    else:
        messagebox.showerror("Erro", "Algumas informações estão erradas, tente novamente.")

def parabens():
    # Criar uma nova janela
    janela_mensagem = Toplevel(principal)
    janela_mensagem.title("Aeeeeeee")
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
    mensagem_label = Label(janela_mensagem, text="Agora você faz parte do jogoooooooo", font=("Arial", 12), bg="lightblue", fg="black")
    mensagem_label.pack(pady=10)

    # Botão para fechar a janela
    fechar_button = Button(janela_mensagem, text="Fechar", command=janela_mensagem.destroy)
    fechar_button.pack(pady=10)

    


# Criar um rótulo para exibir o vídeo
principal = tk.Tk()

label_video = tk.Label(principal)
label_video.pack()

# Obter o tamanho da tela
largura_tela = principal.winfo_screenwidth()
altura_tela = principal.winfo_screenheight()
principal.title("O Jogo")
principal.geometry(f"{largura_tela}x{altura_tela}")
principal.configure(bg="black")



principal.after(0, exibir_video)
principal.mainloop()

