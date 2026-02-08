import pyautogui
from time import sleep

def escrever_asunto_e_enviar(top):
    top = top +1
    sleep(2)
    for letra_1 in assunto:
        if letra_1 == " ":
            pyautogui.press("space")
            
        else:
            pyautogui.press(letra_1)
         
    sleep(2)   
    pyautogui.moveTo(846, 384)
    pyautogui.click()
    for i in range(len(texto)):
        letra_2 = texto[i]
        if letra_2 == " ":
            if texto[i + 1] == " ":
                pyautogui.press("Enter")
            else:
                pyautogui.press("space")
        else:
            pyautogui.press(letra_2)
          
    pyautogui.hotkey("Alt","Tab")
    perg = input("Gostaria de enviar o e-mail?\n")
    perg = perg.lower()
    if "sim" in perg:
        sleep(2)
        print("Ok ;-)")
        sleep(2)
        pyautogui.hotkey("Alt","Tab")
        sleep(1)
        pyautogui.moveTo(845, 690)
        pyautogui.click()
    else:
        sleep(2)
        print("...")
        sleep(3)
        print("Então faz você |:-( ")
        pyautogui.hotkey("Alt","Tab")
        sleep(2)
        pyautogui.moveTo(1336, 9)
        pyautogui.click()






# pede o e-mail principal
email = input("Digite aqui o e-mail principal para quem deseja enviar a mensagem\n")

# pergunta se tem copia e determina 
temcopia = input("Você deseja adicionar copia ou copia oculta? \n")
temcopia = temcopia.lower()

# caso sim, pergunta o tipo de copia
if "sim" in temcopia and "copia" not in temcopia:
    tipo_copia = input("Qual tipo de copia você deseja adicionar?\n(Oculta, normal ou as duas)\n")
    tipo_copia = tipo_copia.lower()
    copia = True
   
else:
    copia = False
    
# caso não tenha não, faça:  
if "não" not in temcopia:  
    # verifica se o usuario pediu copia oculta  
    if "oculta" in tipo_copia:
        oculta = True
        email_copia_oculta = input("Digite ele aqui\n")
    
    # verifica se é copia normal
    elif "normal" in tipo_copia:
        normal = True
        email_copia_normal = input("Digite ele aqui\n")
        
    # verifica se sõ os dois tipos de copia
    elif "dois" in tipo_copia or "duas" in tipo_copia:
        dois_emails = True
        email_copia_normal_d_dois = input("Digite o de copia e-mail normal aqui\n")
        email_copia_oculta_d_dois = input("Agora o e-mail de copia oculta\n")

# caso contrario: `v(o-o)v´
else:
    pass  
        
      
assunto = input("Qual o assunto do e-mail que deseja redigir? \n")
texto = input("Agora digite o texto que deseja enviar \n(Obs.: caso querira dar enter, de 2(dois) espaços, quando finalizar a mensagem de Enter)\n")  
# troca de aba
sleep(2)
pyautogui.hotkey("Alt","Tab")

# clica no icone de e-mail
sleep(7)
pyautogui.moveTo(1161, 147)
pyautogui.click()
# espera carregar
sleep(15)

pyautogui.moveTo(97, 180)
pyautogui.click()
sleep(15)

for letra in email:
    if letra == " ":
        pass
    else:
        pyautogui.press(letra)

if copia == True:
    if "normal" in locals() and normal == True :
        pyautogui.moveTo(1240, 304)
        pyautogui.click()
        sleep(2)
        for letra_3 in email_copia_normal:
            if letra_3 == " ":
                pass
            else:
                pyautogui.press(letra_3)        
        pyautogui.moveTo(811, 389)
        pyautogui.click()
        escrever_asunto_e_enviar(1)
    elif "oculta" in locals() and oculta == True:
        pyautogui.moveTo(1259, 302)
        pyautogui.click()
        sleep(2)
        for letra_4 in email_copia_oculta:
            if letra_4 == " ":
                pass
            else:
                pyautogui.press(letra_4)
        pyautogui.moveTo(810, 385)
        pyautogui.click()
        escrever_asunto_e_enviar(1)
        
    elif "dois_emails" in locals() and dois_emails == True:
        sleep(2)
        pyautogui.moveTo(1240, 304)
        pyautogui.click()
        sleep(2)
        for letra_5 in email_copia_normal_d_dois:
            if letra_5 == " ":
                pass
            else:
                pyautogui.press(letra_5)
        sleep(2)
        pyautogui.moveTo(1261, 343)
        pyautogui.click()
        
        for letra_6 in email_copia_oculta_d_dois:
            if letra_6 == " ":
                pass
            else:
                pyautogui.press(letra_6)
        pyautogui.moveTo(808, 426)
        pyautogui.click()
        escrever_asunto_e_enviar(1)
    
else:
    pyautogui.moveTo(810, 364)
    pyautogui.click()
    escrever_asunto_e_enviar(1)
    
# rrodriguesbruno14@gmail.com
# daianerodovalho@hotmail.com