from time import sleep
import pyautogui as py

sleep(2)
testes = ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
def digite_o_teste(n):
    for letra in n:
        py.press(letra)
        sleep(2)
        n = float(input())
py.moveTo(604, 746)
py.click() #clica no chorome na barra
sleep(5)

for n in testes:
    py.moveTo(369, 89)
    py.click() #clica no run
    
    digite_o_teste(n) # digita o caso teste e envia
    py.press("Enter") 
    
    sleep(3)
    py.moveTo(275,615) # seleciona a saida do teste e copia
    py.mouseDown()
    sleep(1)
    py.moveTo(355,615)
    sleep(1)
    py.mouseUp()
    py.hotkey("Ctrl","c")
    
    sleep(2)
    py.moveTo(650, 20) # vai probloco  de notas n aguia a direita
    py.click()
    
    sleep(2)
    digite_o_teste(testes)
    py.press("Enter")
    py.hotkey("Ctrl","v") # cola todo o caso teste
    py.press("Enter")
    
    sleep(3)
    py.moveTo(403, 13) # volta pra guia do gdb online
    py.click()
    
    
    


