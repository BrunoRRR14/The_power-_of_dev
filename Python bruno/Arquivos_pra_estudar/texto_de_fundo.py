# todo esse código serve pra colocar aquele texto de fundona caixa de texto. Tudo isso só pra uma coisa tão simples. Não vou decorar

import tkinter as tk

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

# Janela principal
root = tk.Tk()
root.title("Exemplo com Placeholder")

# Caixa de entrada com placeholder
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
placeholder(entry, "Digite algo aqui...")

root.mainloop()
