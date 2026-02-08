import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email():
    
    remetente = "brunorrr14@gmail.com"  # Substitua pelo seu e-mail
    chave = "uvaf wvtl scwo ibau"  # Substitua pela sua senha de aplicativo gerada
    destinatario = input("Digite aqui o e-mail do destinatário:\n" )  # Substitua pelo destinatário


    # Configurar o e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = input("Digite aqui o assunto:\n")
    corpo = input("Digite aqui o corpo do e-mail:\n")
    


    # Adicionar o corpo ao e-mail
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(remetente, chave)  # Use a chave de aplicativo aqui
        print("Login bem-sucedido!")
        server.sendmail(remetente, destinatario, mensagem.as_string())  # Enviar o e-mail
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
    finally:
        server.quit()

enviar_email()


#uvaf wvtl scwo ibau