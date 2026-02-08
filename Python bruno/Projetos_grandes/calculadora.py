equacao_completa = ""
caracteres_calculator = ["+", "*", "/", ",", "%", "^", "."]
while True:
    tecla = input("")
    try:
        if int(tecla) / 1 == int(tecla):
            equacao_completa = f"{equacao_completa} {tecla}"
    except:
        if tecla in caracteres_calculator:
            equacao_completa = f"{equacao_completa}{tecla}"
        elif tecla == "=":
            break
        else:
            print("A tela digitada não corresponde a nenhuma do nosso banco de dados")
            break
        
equacao_completa =  equacao_completa.replace(" ", "")
resultado = eval(f"{equacao_completa}")
print(resultado)
        