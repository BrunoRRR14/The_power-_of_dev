import pyautogui
from tkinter import *
import tkinter as tk
from tkinter import ttk

def rosto():

        
    x,y = pyautogui.position()
    if x > 1322 and y < 37:
        carinha.quit()  # Fecha a janela
    else:
        if x < 455:
            return ":-D"
        elif 456 < x < 910:
            return ":-)"
        elif x > 1241 and y < 100:
            return "}:-("
        else:
            return ":-/"


def atualizar_rosto():
    # Obtém o horário atual no formato desejado
    
    label_horario.config(text=rosto())  # Atualiza o texto do rótulo
    carinha.after(1000, atualizar_rosto)
    
    
carinha = tk.Tk()


largura_tela = carinha.winfo_screenwidth()
altura_tela = carinha.winfo_screenheight()
carinha.title("Sorria")
carinha.geometry(f"{largura_tela}x{altura_tela}")
carinha.configure(bg="black")

# Cria um rótulo para exibir a carinha
label_horario = tk.Label(carinha, text=":-)", font=("Helvetica", 400), bg="black", fg="white")
label_horario.pack(pady=20)

# Inicia a atualização da carinha
atualizar_rosto()

# Inicia o loop principal da interface gráfica
carinha.mainloop()