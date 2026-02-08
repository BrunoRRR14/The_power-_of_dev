import time
import locale
from time import sleep
import webbrowser as wb

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()
print(time.strftime("%d  de %B de %Y", tempo_em_struct))
print(time.strftime("%H:%M:%S", tempo_em_struct))

sleep(10)

tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)
print(tempo_formatado)


sleep(10)

#wb.open('https://www.google.com')
#sleep(10)
print("Pronto")