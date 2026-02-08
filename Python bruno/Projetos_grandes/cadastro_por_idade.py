import time
hora_local =time.localtime()


while True:
    nome_c = input("Qual é o seu nome completo? ")
    data = input("Qual é a sua data de nascimento? \n(No seguinte formato: DD/MM/AAAA)\n")
    dia_n = data[0:2]
    mes_n = data[3:5]
    ano_n = data[6:10]

    dia = hora_local.tm_mday
    mes = hora_local.tm_mon
    ano = hora_local.tm_year

    diferenca_ano = ano - int(ano_n)
    diferenca_mes = mes - int(mes_n)
    diferenca_dia = dia - int(dia_n)


    if diferenca_ano > 130:
        print("Por favor não levante os braços, qualquer coisa te puxam pro céu. :- D")
        break
    elif diferenca_ano < 12:
        print("Calma novinho, segura seu momento.")
        break
    else:
        pass
    if int(mes_n) > 12:
        print("Mês invalido \nTe dou mais uma chance ;-)")
        continue
    if int(dia_n) <= 31 and int(dia_n) >= 1:
        pass
    else:
        print("Informe um dia válido\n")
        continue



    if  diferenca_ano < 18:
        print("Infelizmente você não tem idade para assinar o contrato")
        break
    elif diferenca_ano == 18:
        if diferenca_mes < 0:
            print("Infelizmente você não tem idade para assinar o contrato")
            break
        elif diferenca_mes == 0:
            if diferenca_dia < 0:
                print("Infelizmente você não tem idade para assinar o contrato")
                break
            elif diferenca_dia == 0:
                print("Parabéns, você faz aniversário hoje, mas aproveita, faça o seu cadastro amanhã.")
                break
            else:
                cpf = input("Digite seu CPF:\n")
                print(f"\n\n \nA partir deste contrato declaramos que {nome_c}, com o seguinte CPF:\n{cpf}\n\nNascido(a) em {data} recebe o título de:\n\n                                         THE LOVE DE MY LIFE\n\nObrigado...                                              \n")
                break
        else:
            cpf = input("Digite seu CPF: \n")
            print(f"\n\n \nA partir deste contrato declaramos que {nome_c}, com o seguinte CPF:\n{cpf}\n\nNascido(a) em {data} recebe o título de:\n\n                                         THE LOVE DE MY LIFE\n\nObrigado...                                              \n")
            break
    else:
        cpf = input("Digite seu CPF: \n")
        print(f"\n\n \nA partir deste contrato declaramos que {nome_c}, com o seguinte CPF:\n{cpf}\n\nNascido(a) em {data} recebe o título de:\n\n                                         THE LOVE DE MY LIFE\n\nObrigado...                                              \n")
        break