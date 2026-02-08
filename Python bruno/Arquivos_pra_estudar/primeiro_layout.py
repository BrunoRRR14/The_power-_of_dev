from tkinter import *

def funcao_simples():
    texto = ("Top d+, você clicou :- D")
    texto_final["text"] = texto







#cria a janela crua
janela = Tk()

#titulo da janela
janela.title("Minha primeira janela")

#tamanho da janela
janela.geometry("250x160")
#cria o texto
texto_1 = Label(janela, text="Eai, beleza? Clica ai")
#coloca o texto em um lugar especifico
texto_1.grid(column=0, row=0, padx= 10, pady= 10)

#cria um botão e passa: em que janela vai aparecer; o texto dele; o comondo que executa um a funçao sem parenteses pra não executar ela
botao = Button(janela, text="Aquii", command=funcao_simples)
botao.grid(column=0, row=1, padx= 10, pady= 10)
#outro texto
texto_2 = Label(janela, text="Clica aqui em baixo e descubra ao porquê")
texto_2.grid(column=0, row=2, padx= 10, pady= 10)


#cria um texto que aparece a partir da função que depende do botão
texto_final = Label(janela, text="")
texto_final.grid(column=0, row=3, padx= 10, pady= 10)

#mantem a janela
janela.mainloop()