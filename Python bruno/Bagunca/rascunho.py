import tkinter as tk
from PIL import Image, ImageTk
import cv2
import time

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
            root.after(10, mostrar_quadro)  # Mostrar o próximo quadro após 10 ms
        else:
            # Fechar o vídeo após a exibição
            cap.release()
            root.quit()

    # Iniciar a exibição dos quadros
    mostrar_quadro()

# Criar a janela principal
root = tk.Tk()
root.title("Exibição de Vídeo")

# Definir o tamanho da janela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
root.geometry(f"{largura_tela}x{altura_tela}")
root.configure(bg="black")
# Criar um rótulo para exibir o vídeo
label_video = tk.Label(root)
label_video.pack()
 
#  Exibir o vídeo
root.after(0, exibir_video)

# Fechar a janela automaticamente após 3 segundos
root.after(3000, root.destroy)

# Iniciar o loop principal
root.mainloop()
