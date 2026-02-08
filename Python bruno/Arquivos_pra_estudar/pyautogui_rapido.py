import pyautogui
from pyautogui import  *


pyautogui.alert('Mensagem de alerta!')
resposta = pyautogui.prompt('Digite algo:')  # Entrada de texto do usuário
confirmar = pyautogui.confirm('Confirma a ação?', buttons=['Sim', 'Não'])

 