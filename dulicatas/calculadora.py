equacao_completa = " "
caracteres_calculator = ["+", "*", "/", ",","=", "%", "^", "."]
while True:
    tecla = input("")
    try:
        if int(tecla) / 1 == int(tecla):
            equacao_completa = f"{equacao_completa} {tecla}"
    except:
        if tecla in caracteres_calculator:
            equacao_completa = f"{equacao_completa}{tecla}"
        else:
            print("A tela digitada não corresponde a nenhuma do nosso banco de dados")
            break
        
    finally:
        if tecla != "=":
            continue
        else:
            break
equacao_completa = equacao_completa.replace(",", ".")
equacao_completa = equacao_completa.replace("^", "**")
equacao_completa = equacao_completa.replace(" ", "")
print(equacao_completa)
        