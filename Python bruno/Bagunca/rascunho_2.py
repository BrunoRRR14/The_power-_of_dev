import random

def tres_pessoas():
  all_portuguese_words = [
      'maçã', 'banana', 'laranja', 'uva', 'kiwi', 'manga', 'pera', 'pêssego',
      'gato', 'cachorro', 'pássaro', 'peixe', 'coelho', 'hamster', 'cobra', 'tartaruga',
      'vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'preto', 'branco', 'rosa',
      'carro', 'casa', 'árvore', 'sol', 'lua', 'estrela', 'água', 'fogo', 'terra', 'céu',
      'flor', 'livro', 'caneta', 'telefone', 'computador', 'mesa', 'cadeira', 'porta', 'janela',
      'cidade', 'montanha', 'rio', 'mar', 'nuvem', 'vento', 'chuva', 'neve',
      'dia', 'noite', 'manhã', 'tarde', 'jantar', 'café', 'chá', 'suco', 'leite',
      'pão', 'bolo', 'doce', 'salgado', 'feliz', 'triste', 'grande', 'pequeno',
      'quente', 'frio', 'bom', 'mau', 'novo', 'velho', 'rápido', 'lento',
      'silêncio', 'barulho', 'música', 'filme', 'jogo', 'viagem', 'trabalho', 'escola',
      'família', 'amigo', 'amor', 'paz', 'esperança', 'saúde', 'tempo', 'dinheiro', 'felicidade'
  ]
  palavra = random.choice(all_portuguese_words)
  escolhido = random.randint(0, 2)
  palavras_1 = [palavra, palavra, palavra]
  palavras_1[escolhido] = "IMPOSTOR"
  return palavras_1

def quatro_pessoas():
  all_portuguese_words = [
      'maçã', 'banana', 'laranja', 'uva', 'kiwi', 'manga', 'pera', 'pêssego',
      'gato', 'cachorro', 'pássaro', 'peixe', 'coelho', 'hamster', 'cobra', 'tartaruga',
      'vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'preto', 'branco', 'rosa',
      'carro', 'casa', 'árvore', 'sol', 'lua', 'estrela', 'água', 'fogo', 'terra', 'céu',
      'flor', 'livro', 'caneta', 'telefone', 'computador', 'mesa', 'cadeira', 'porta', 'janela',
      'cidade', 'montanha', 'rio', 'mar', 'nuvem', 'vento', 'chuva', 'neve',
      'dia', 'noite', 'manhã', 'tarde', 'jantar', 'café', 'chá', 'suco', 'leite',
      'pão', 'bolo', 'doce', 'salgado', 'feliz', 'triste', 'grande', 'pequeno',
      'quente', 'frio', 'bom', 'mau', 'novo', 'velho', 'rápido', 'lento',
      'silêncio', 'barulho', 'música', 'filme', 'jogo', 'viagem', 'trabalho', 'escola',
      'família', 'amigo', 'amor', 'paz', 'esperança', 'saúde', 'tempo', 'dinheiro', 'felicidade'
  ]
  palavra = random.choice(all_portuguese_words)
  escolhido = random.randint(0, 3)
  palavras_2 = [palavra, palavra, palavra, palavra]
  palavras_2[escolhido] = "IMPOSTOR"
  return palavras_2

def cinco_pessoas():
  all_portuguese_words = [
      'maçã', 'banana', 'laranja', 'uva', 'kiwi', 'manga', 'pera', 'pêssego',
      'gato', 'cachorro', 'pássaro', 'peixe', 'coelho', 'hamster', 'cobra', 'tartaruga',
      'vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'preto', 'branco', 'rosa',
      'carro', 'casa', 'árvore', 'sol', 'lua', 'estrela', 'água', 'fogo', 'terra', 'céu',
      'flor', 'livro', 'caneta', 'telefone', 'computador', 'mesa', 'cadeira', 'porta', 'janela',
      'cidade', 'montanha', 'rio', 'mar', 'nuvem', 'vento', 'chuva', 'neve',
      'dia', 'noite', 'manhã', 'tarde', 'jantar', 'café', 'chá', 'suco', 'leite',
      'pão', 'bolo', 'doce', 'salgado', 'feliz', 'triste', 'grande', 'pequeno',
      'quente', 'frio', 'bom', 'mau', 'novo', 'velho', 'rápido', 'lento',
      'silêncio', 'barulho', 'música', 'filme', 'jogo', 'viagem', 'trabalho', 'escola',
      'família', 'amigo', 'amor', 'paz', 'esperança', 'saúde', 'tempo', 'dinheiro', 'felicidade'
  ]
  palavra = random.choice(all_portuguese_words)
  escolhido = random.randint(0, 4)
  palavras_3 = [palavra, palavra, palavra, palavra, palavra]
  palavras_3[escolhido] = "IMPOSTOR"
  return palavras_3

P = int(input("Quantas pessoas  vão participar da brincadeira \n"))

# @title
## principal
from ipywidgets import widgets
from IPython.display import display

if P == 3:
  my_list = ["Pessoa 1", "Pessoa 2", "Pessoa 3"]
  palavras_1 = (tres_pessoas())
elif P == 4:
  my_list = ["Pessoa 1", "Pessoa 2", "Pessoa 3", "Pessoa 4"]
  palavras_2 = (quatro_pessoas())
elif P == 5:
  my_list = ["Pessoa 1", "Pessoa 2", "Pessoa 3", "Pessoa 4", "Pessoa 5"]
  palavras_3 = (cinco_pessoas())
else:
  print("Número de pessoas inválido")



checkboxes = []

for item in my_list:
    checkbox = widgets.Checkbox(description=item, value=False, disabled=False, indent=False)
    checkboxes.append(checkbox)
    display(checkbox)

# @title
# Exemplo de como acessar os valores (você precisaria de um botão ou evento para isso)

if P == 3:
  if checkboxes[0].value == True and checkboxes[1].value == False and checkboxes[2].value == False:
    print(palavras_1[0])
  elif checkboxes[0].value == False and checkboxes[1].value == True and checkboxes[2].value == False:
    print(palavras_1[1])
  elif checkboxes[0].value == False and checkboxes[1].value == False and checkboxes[2].value == True:
    print(palavras_1[2])

elif P == 4:
  if checkboxes[0].value == True and checkboxes[1].value == False and checkboxes[2].value == False and checkboxes[3].value == False:
    print(palavras_2[0])
  elif checkboxes[0].value == False and checkboxes[1].value == True and checkboxes[2].value == False and checkboxes[3].value == False:
    print(palavras_2[1])
  elif checkboxes[0].value == False and checkboxes[1].value == False and checkboxes[2].value == True and checkboxes[3].value == False:
    print(palavras_2[2])
  elif checkboxes[0].value == False and checkboxes[1].value == False and checkboxes[2].value == False and checkboxes[3].value == True:
    print(palavras_2[3])

elif P == 5:
  if checkboxes[0].value == True and checkboxes[1].value == False and checkboxes[2].value == False and checkboxes[3].value == False and checkboxes[4].value == False:
    print(palavras_3[0])
  elif checkboxes[0].value == False and checkboxes[1].value == True and checkboxes[2].value == False and checkboxes[3].value == False and checkboxes[4].value == False:
    print(palavras_3[1])
  elif checkboxes[0].value == False and checkboxes[1].value == False and checkboxes[2].value == True and checkboxes[3].value == False and checkboxes[4].value == False:
    print(palavras_3[2])
  elif checkboxes[0].value == False and checkboxes[1].value == False and checkboxes[2].value == False and checkboxes[3].value == True and checkboxes[4].value == False:
    print(palavras_3[3])
  elif checkboxes[0].value == False and checkboxes[1].value == False and checkboxes[2].value == False and checkboxes[3].value == False and checkboxes[4].value == True:
    print(palavras_3[4])