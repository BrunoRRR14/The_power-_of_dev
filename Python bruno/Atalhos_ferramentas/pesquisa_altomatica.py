#tudo que tem que importar
import webbrowser as wb
from time import sleep
import pyautogui
import pyperclip

#pede o que tu quer pesquisar
frase = input("Digite: \n")
sleep(5)

#abre o navegador
wb.open('https://www.google.com')
sleep(10)

#digita o que você digitou no navegador
#for letra in frase:
#    if letra == " ":
#        pyautogui.press("space")
#    else:
#        pyautogui.press(letra)
pyperclip.copy(frase)
pyautogui.hotkey("ctrl","V")

pyautogui.press("Enter")
sleep(4)
#move o mouse pra clicar no estou com sorte (te manda pro primeiro link)

#    if 2 < 1:
#        sleep(3)
#        pyautogui.moveTo(1076, 435)
#        sleep(1)
#        pyautogui.click()
#        sleep(2)
#        pyautogui.moveTo(806, 402)
#        sleep(1)
#        pyautogui.click()


pyautogui.hotkey("Alt","Tab")
# fecha a aba só de sacanagem
#pyautogui.moveTo(354, 13)
#sleep(2)
#pyautogui.click()


#e por fim, terminamos de rodar
print("Pronto!")


