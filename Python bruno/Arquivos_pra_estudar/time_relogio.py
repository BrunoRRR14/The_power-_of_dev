import time
import locale
locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B %Y, %H:%M", tempo_em_struct)
print(tempo_formatado)

