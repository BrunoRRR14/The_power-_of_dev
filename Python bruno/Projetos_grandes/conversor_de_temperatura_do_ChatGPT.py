import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para realizar a conversão
def converter_temperatura():
    try:
        temp = float(entrada_temp.get())
        unidade_origem = combo_origem.get()
        unidade_destino = combo_destino.get()

        # Converter a temperatura para Celsius como intermediário
        if unidade_origem == "Celsius":
            temp_celsius = temp
        elif unidade_origem == "Fahrenheit":
            temp_celsius = (temp - 32) * 5/9
        elif unidade_origem == "Kelvin":
            temp_celsius = temp - 273.15
        else:
            messagebox.showerror("Erro", "Unidade de origem inválida.")
            return

        # Converter de Celsius para a unidade de destino
        if unidade_destino == "Celsius":
            resultado = temp_celsius
        elif unidade_destino == "Fahrenheit":
            resultado = (temp_celsius * 9/5) + 32
        elif unidade_destino == "Kelvin":
            resultado = temp_celsius + 273.15
        else:
            messagebox.showerror("Erro", "Unidade de destino inválida.")
            return

        # Exibir o resultado
        label_resultado.config(text=f"Resultado: {resultado:.2f} °{unidade_destino[0]}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor de Temperaturas")
janela.geometry("500x300")
janela.resizable(False, False)

# Label e campo de entrada para a temperatura
label_temp = ttk.Label(janela, text="Temperatura:")
label_temp.pack(pady=10)

entrada_temp = ttk.Entry(janela)
entrada_temp.pack()

# Combobox para unidade de origem
label_origem = ttk.Label(janela, text="De:")
label_origem.pack(pady=5)

combo_origem = ttk.Combobox(janela, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_origem.current(0)
combo_origem.pack()

# Combobox para unidade de destino
label_destino = ttk.Label(janela, text="Para:")
label_destino.pack(pady=5)

combo_destino = ttk.Combobox(janela, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_destino.current(1)
combo_destino.pack()

# Botão para converter
botao_converter = ttk.Button(janela, text="Converter", command=converter_temperatura)
botao_converter.pack(pady=10)

# Label para exibir o resultado
label_resultado = ttk.Label(janela, text="Resultado: ")
label_resultado.pack(pady=5)

# Iniciar o loop principal da interface
janela.mainloop()
