import pyautogui
import webbrowser as wb
from time import sleep

wb.open('https://www.google.com')
sleep(7)
x,y = pyautogui.position()
print(x,y)
print("Beleza")