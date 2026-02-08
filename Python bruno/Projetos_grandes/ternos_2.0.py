from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def nota_fiscal():
    valor_final = 0
    nao_selecionado = 0
    
    terno_escolhido = lista_cor_ternos_prec.get()
    
    if terno_escolhido != "Nenhum":
        preco_terno = terno_escolhido[-6:-3]
        cor_terno = terno_escolhido[0:-13]
        preco_terno = int(preco_terno)
        valor_final += preco_terno
        trecho_terno = (f"\nTerno de cor: {cor_terno}, Preço: R${preco_terno}")
    else:
        trecho_terno = "\n Nenhum terno foi  selecionado"
        nao_selecionado += 1
    
    gravata_escolhida = lista_cor_gravatas_prec.get()
    
    if gravata_escolhida != "Nenhum":
        preco_gravata = gravata_escolhida[-5:-3]
        cor_gravata = gravata_escolhida[0:-12]
        preco_gravata = int(preco_gravata)
        valor_final += preco_gravata
        trecho_gravata = (f" \nGravata de cor: {cor_gravata}, Preco: R${preco_gravata}")
    else:
        trecho_gravata = "\nNenhuma gravata foi selecionada"
        nao_selecionado += 1
        
    calca_escolhida = lista_cor_calcas_prec.get()
    
    if calca_escolhida != "Nenhum":
        preco_calca = calca_escolhida[-6:-3]
        cor_calca = calca_escolhida[0:-13]
        preco_calca = int(preco_calca)
        valor_final += preco_calca
        trecho_calca = (f"\nCalça de cor: {cor_calca}, Preco: R${preco_calca}")
    else:
        trecho_calca = "\nNenhuma calça foi selecionada"
        nao_selecionado += 1
        
    camisa_social_escolhida = lista_cor_camisas_sociais_prec.get()
    
    if camisa_social_escolhida != "Nenhum":
        preco_camisa_social = camisa_social_escolhida[-6:-3]
        cor_camisa_social = camisa_social_escolhida[0:-13]
        preco_camisa_social = int(preco_camisa_social)
        valor_final += preco_camisa_social
        trecho_camisa_s = (f"\nCamisa social de cor: {cor_camisa_social}, Preco: R${preco_camisa_social}")
    else:
        trecho_camisa_s = "\nNenhuma camisa social foi selecionada"
        nao_selecionado += 1
        
    if nao_selecionado == 4:
        messagebox.showerror("Erro", "Nenhum item foi selecionado.")
        
    else:
        messagebox.showinfo("Seleção finalizada",f"{trecho_terno} {trecho_gravata} {trecho_calca} {trecho_camisa_s} \n\nTotal: R${valor_final}")
    
    










# Criando e configurando a aba
ropa_gala = Tk()
ropa_gala.title("Roupa de Gala    ")
ropa_gala.geometry("450x250")

# Criando e configurando a seleção de ternos
titulo_terno = Label(ropa_gala, text= "Cor do terno:")
titulo_terno.pack()
 
lista_cor_ternos_prec = ttk.Combobox(ropa_gala, values=["Preto --> R$350,00", "Cinza --> R$270,00", "Marçala --> R$430,00", "Azul --> R$290,00", "Branco --> R$500,00", "Amarelo --> R$800,00", "Nenhum"], state="readonly")
lista_cor_ternos_prec.current(1)
lista_cor_ternos_prec.config(width=30)
lista_cor_ternos_prec.pack()


# Criando e configurando a seleção de gravatas 
titulo_gravata = Label(ropa_gala, text= "Cor da gravata:")
titulo_gravata.pack()

lista_cor_gravatas_prec = ttk.Combobox(ropa_gala, values=["Preta --> R$50,00", "Cinza --> R$70,00", "Marçala --> R$30,00", "Azul --> R$90,00", "Branca --> R$50,00", "Listrada cinza e preta --> R$80,00","Listrada preta e azul --> R$90,00","Dourada --> R$99,00", "Nenhum"], state="readonly")
lista_cor_gravatas_prec.current(1)
lista_cor_gravatas_prec.config(width=30)
lista_cor_gravatas_prec.pack()

# Criando e configurando a seleção de calcas 
titulo_calca = Label(ropa_gala, text= "Cor da calca:")
titulo_calca.pack()

lista_cor_calcas_prec = ttk.Combobox(ropa_gala, values=["Preto --> R$175,00", "Cinza --> R$145,00", "Marçala --> R$215,00", "Azul --> R$145,00", "Branca --> R$250,00", "Amarela --> R$400,00", "Nenhum"], state="readonly")
lista_cor_calcas_prec.current(1)
lista_cor_calcas_prec.config(width=30)
lista_cor_calcas_prec.pack()

# Criando e configurando a seleção de camisa_social 
titulo_camisa_social = Label(ropa_gala, text= "Cor da camisa social:")
titulo_camisa_social.pack()

lista_cor_camisas_sociais_prec = ttk.Combobox(ropa_gala, values=["Branca listrada --> R$190,00", "Branca quadriculada --> R$145,00", "Cinza --> R$160,00", "Prata --> R$200,00", "Branca lisa --> R$100,00", "Nenhum"], state="readonly")
lista_cor_camisas_sociais_prec.current(1)
lista_cor_camisas_sociais_prec.config(width=30)
lista_cor_camisas_sociais_prec.pack()

b_enviar = Button(ropa_gala, text= "Enviar", command=nota_fiscal)
b_enviar.pack(pady=5)

ropa_gala.mainloop()


