import subprocess


# Caminho do aplicativo que você quer abrir
caminho_app = f"C:/Program Files/Google/Chrome/Application/chrome.exe"
#caminho_app = f"C:/Program Files (x86)/Mozilla Firefox/firefox.exe"



# Abrir o aplicativo
subprocess.Popen(caminho_app)
