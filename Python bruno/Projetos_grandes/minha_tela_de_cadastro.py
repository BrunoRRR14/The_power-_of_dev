from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def novo(event):
    email.focus_set()  # Muda o foco para o próximo campo






def interprete():
    
    contador = 0
    nome_aqui = nome.get()
    if not nome_aqui:
        messagebox.showerror("Erro", "Campo nome não foi preenchido.")
    else:
        cond_1 = True
    
    usando_aqui = combo_origem.get()
    #if usando_aqui != "Feminino" and usando_aqui != "Outro" and usando_aqui != "Masculino":
        #messagebox.showerror("Erro", "Genero não identificado.")
    #else:
    cond_2 = True
        
    usar_email = email.get()
    
    
    if "@" in usar_email:
        if "@" != usar_email[0] and "." != usar_email[0]:
            if "mail.com" in usar_email:
                for letra in usar_email:
                    if letra.isupper() == True:
                        messagebox.showerror("Erro", "Email tem letras maiusculas.")
                        contador+= 1
                    else:
                        contador = contador
                    if contador == 0:
                        cond_3 = True
                    else:
                        cond_3 = False
                        
            else:
                messagebox.showerror("Erro", "Email invalido.")
        else:
            messagebox.showerror("Erro", "Email invalido.")
    else:
        messagebox.showerror("Erro", "Email invalido.")

    try:
        if cond_1 == True and cond_2 == True and cond_3 == True:
            messagebox.showinfo("Cadastro bem sucedido          .")
            
    except:
        messagebox.showerror("Erro", "Tente novamente.")



cadastro = Tk()
cadastro.title("Tela de cadastro")

combo_origem = ttk.Combobox(cadastro, values=["Masculino", "Feminino", "Gay", "Lesbica", "Trans", "Transformer", "Robo", "Equilatero", "Cateto oposto", "Cateto adjacente", "Hipotenusa", "Medusa", "Perseu", "Hercolis", "Brocolis", "Binario", "Não binário", "Centenário", "Fúria da noite", "Marca-página" , "Michael Jackson", "Honda Civic", "Fiat Uno", "Fiat Uno com ESCADA", "Darth Vaider","Estrela da morte", "Bola de futbol da copa de 14", "Bola de futbol da copa de 18", "Bola de futbol da copa de 22",  "Bola de boliche", "Harry Potter", "Sonserina", "Lufa-Lufa", "Grifinória","Corvinal", "Animal","Panela ant_aderente", "S24 Ultra" ,"S25 Ultra", "J7 prime", "Argentino", "Teletubs", "Briofita", "Pteridofta", "Gimnosperma", "Angiosperma", "Celenterado", "Acelomado", "Ablacito", "Diblácito", "Triblácito", "Galinha da angola", "Tuk-Tuk", 'Vaso de planta' ,"Outro"], state="readonly")
combo_origem.current(0)
combo_origem.pack()
combo_origem.config(width=25)
combo_origem.grid(column=1, row=2, padx= 10, pady= 10)


botao_d_enviar = Button(cadastro, text="Enviar", command=interprete)
botao_d_enviar.grid(column=1, row=3, padx= 10, pady= 10)

email = Entry(cadastro, width=30)
email.grid(column=1, row=1, padx= 10, pady= 10)

email.bind("<Return>", interprete)

texto_email = Label(cadastro, text= "E-mail:")
texto_email.grid(column=0, row=1, padx= 10, pady= 10)

nome = Entry(cadastro, width=30)
nome.grid(column=1, row=0, padx= 10, pady= 10)

nome.bind("<Return>", novo)

texto_nome = Label(cadastro, text= "Nome:")
texto_nome.grid(column=0, row=0, padx= 10, pady= 10)

texto_genero = Label(cadastro, text= "Genero:")
texto_genero.grid(column=0, row=2, padx= 10, pady= 10)

cadastro.mainloop()
