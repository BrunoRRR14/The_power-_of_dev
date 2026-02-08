#tudo que tem que importar
import webbrowser as wb
from time import sleep
import pyautogui


lista_de_celulares = ["A55 5G", "Poco X6 Pro", "Poco X6 5G", "S23 FE", "S23","S23 Plus", "Poco F6 Pro","S24","S24 Ultra"]
frase = " tudo celular"
sleep(2)

for celular in lista_de_celulares:
    sleep(7)
    wb.open('https://www.google.com')
    
    sleep(7)
    for letra in celular:
        if letra == " ":
            pyautogui.press("space")
        else:
            pyautogui.press(letra)
    for letro in frase:
        if letro == " ":
            pyautogui.press("space")
        else:
            pyautogui.press(letro)
            
    #move o mouse pra clicar no estou com sorte (te manda pro primeiro link)
    sleep(3)
    pyautogui.moveTo(1076, 435)
    sleep(1)
    pyautogui.click
    sleep(1)
    pyautogui.moveTo(599, 404)
    sleep(1)
    pyautogui.click()
    sleep(1)
print("Programa finalizado")
