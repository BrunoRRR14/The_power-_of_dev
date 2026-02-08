from selenium import webdriver
import time

# abrir navegador
navegador = webdriver.Chrome()

# acessar site
navegador.get("https://www.google.com")

# colocar em tela cheia 
navegador.maximize_window()


# selecionar elemento NA TELA
area_restrita = navegador.find_element("class name", "gb_Z")

# clicar em um elemento
area_restrita.click()


time.sleep(10)

print("Bora bora")
