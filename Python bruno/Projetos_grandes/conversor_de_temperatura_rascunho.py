from tkinter import *
from tkinter import messagebox


def recebi_cel():
    return True
    
def recebi_kelv():
    return True

def recebi_far():
    return True

def interpre_cel(recebi_cel, recebi_kelv, recebi_far):
    if recebi_cel == True:
        messagebox.showwarning("Erro", "Por favor, selecione apenas uma temperatura por vez.")
    else:
        if recebi_kelv == True:
            fim_kelv = entrada_temp.get() + 273.15
            resultado_cel["text"] = fim_kelv
        elif recebi_far == True:
            fim_faren = entrada_temp.get() *1.8 + 32
            resultado_cel["text"] = fim_faren
        

aba = Tk()
aba.title("Conversor de temperatura")

#textos da aba
de = Label(aba, text="De")
de.grid(column=0, row=0, padx= 10, pady= 10)

para = Label(aba, text="Para")
para.grid(column=2, row=0, padx= 10, pady= 10)

#botões iniciais
botao_ini_cel = Button(aba, text="Celsius", command=recebi_cel)
botao_ini_cel.grid(column=0, row=1, padx= 10, pady= 10)

botao_inic_kelv = Button(aba, text="Kelvin", command=recebi_kelv)
botao_inic_kelv.grid(column=0, row=2, padx= 10, pady= 10)

botao_inic_far = Button(aba, text="Fahrenheit", command=recebi_far)
botao_inic_far.grid(column=0, row=3, padx= 10, pady= 10)


# botões finais
botao_cel = Button(aba, text="Celsius", command=interpre_cel)
botao_cel.grid(column=2, row=1, padx= 10, pady= 10)

botao_kelv = Button(aba, text="Kelvin", command=recebi_kelv)
botao_kelv.grid(column=2, row=2, padx= 10, pady= 10)

botao_far = Button(aba, text="Fahrenheit", command=recebi_far)
botao_far.grid(column=2, row=3, padx= 10, pady= 10)

# a entrada da temperatura

entrada_temp = Entry(aba, width=15)
entrada_temp.grid(column=1, row=1, padx= 10, pady= 10)


#os resultados da conversão de cada temperatura
resultado_cel = Label(aba, text="")
resultado_cel.grid(column=1, row=4, padx= 10, pady= 10)

resultado_kelv = Label(aba, text="")
resultado_kelv.grid(column=2, row=4, padx= 10, pady= 10)

resultado_far = Label(aba, text="")
resultado_far.grid(column=3, row=4, padx= 10, pady= 10)

#botao para calcular
#botao_calcular = Button(aba, text="Calcular", command=)
#botao_far.grid(column=2, row=3, padx= 10, pady= 10)


aba.mainloop()