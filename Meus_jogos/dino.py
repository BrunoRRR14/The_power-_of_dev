# configurações iniciais

import pygame as pg
import random

pg.init()
pg.display.set_caption("Jogo do Dino")
larg, altu = 800, 600
tela = pg.display.set_mode((larg, altu))
relogio = pg.time.Clock()



# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0 ,0)
verde = (0, 255, 0)
cinza = (100, 100, 100)

# parametros importates 

tamanho_dino = 40
tamanho_quadrado = 20
chao_y = altu - 50
velocidade_jogo = 15


# Dino
dino_x = 100
dino_y = chao_y - tamanho_dino
pulo = False
forca_pulo = 13
gravidade = 1
velocidade_y = 0

# Cacto
def gerar_cacto():
    cacto_x = larg
    cacto_y = chao_y - tamanho_dino
    return [cacto_x, cacto_y]

cactos = [gerar_cacto()]

# Desenhar chão
def desenhar_chao():
    pg.draw.rect(tela, cinza, [0, chao_y, larg, 10])


def gerar_cacto():
    cacto_x = round(random.randrange(0, larg - tamanho_quadrado) / float(tamanho_quadrado))  * float(tamanho_quadrado)
    cacto_y = round(random.randrange(0, altu - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return cacto_x, cacto_y
    
def desenhar_cacto(tamanho, cacto_x, cacto_y):
    pg.draw.rect(tela, verde, [cacto_x, cacto_y, tamanho, tamanho])
    
def desenhar_dino(tamanho, pixels):
    for pixel in pixels:
        pg.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontos):
    fonte = pg.font.SysFont(None, 35)
    texto = fonte.render(f"Pontos: {pontos}", True, branca)
    tela.blit(texto, [10, 10])



def selecionar_velocidade(tecla):
    if tecla == pg.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        
    elif tecla == pg.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        
        
    elif tecla == pg.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0    
    
    elif tecla == pg.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
        
    return velocidade_x, velocidade_y






def bora():
    cabo = False
    
    X = larg / 2
    Y = altu / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_dino = 1
    pixels = []
    
    cacto_x, cacto_y = gerar_cacto()
    
    while not cabo:
        tela.fill(preta)
        
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                cabo = True
                
            elif evento.type == pg.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        # desenha_cacto
        desenhar_cacto(tamanho_quadrado, cacto_x, cacto_y)
        
        
        # atuaslizar a posicao da dino
        if X < 0 or X >= larg or Y < 0 or Y >= larg:
            cabo = True
        
        
        X += velocidade_x
        Y += velocidade_y
        
        # desenhar_dino 
        pixels.append([X, Y])
        if len(pixels) > tamanho_dino:
            del pixels[0]
        
        
        # se a cobrinha bateu no proprio corpo 
        for pixel in pixels[:-1]:
            if pixel == [X ,Y]:
                cabo = True
        
        desenhar_dino(tamanho_quadrado, pixels)
        
        # desenhar_pontos
        desenhar_pontuacao(tamanho_dino - 1)
        
        
        # atualizacao tela
        pg.display.update()
        
        # criar um nova cacto
        if X == cacto_x and Y == cacto_y:
            tamanho_dino += 1 
            cacto_x, cacto_y = gerar_cacto()
        
        
        relogio.tick(velocidade_jogo)
                
                
bora()
        
