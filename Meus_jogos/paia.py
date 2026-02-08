import pygame as pg
import random

pg.init()
pg.display.set_caption("Jogo do Dino")

# Tela
larg, altu = 800, 400
tela = pg.display.set_mode((larg, altu))
relogio = pg.time.Clock()

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
verde = (0, 255, 0)
vermelha = (255, 0, 0)
cinza = (100, 100, 100)

# Parâmetros
tamanho_dino = 40
chao_y = altu - 50
velocidade_jogo = 10

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

# Desenhar dino
def desenhar_dino(x, y):
    pg.draw.rect(tela, branca, [x, y, tamanho_dino, tamanho_dino])

# Desenhar cactos
def desenhar_cactos(lista_cactos):
    for cacto in lista_cactos:
        pg.draw.rect(tela, verde, [cacto[0], cacto[1], tamanho_dino, tamanho_dino])

# Pontuação
def desenhar_pontuacao(pontos):
    fonte = pg.font.SysFont(None, 35)
    texto = fonte.render(f"Pontos: {pontos}", True, branca)
    tela.blit(texto, [10, 10])

# Jogo principal
def bora():
    global dino_y, pulo, velocidade_y
    rodando = True
    pontos = 0
    cactos.clear()
    cactos.append(gerar_cacto())

    while rodando:
        tela.fill(preta)
        desenhar_chao()

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_UP and not pulo:
                    pulo = True
                    velocidade_y = -forca_pulo

        # Lógica do pulo
        if pulo:
            dino_y += velocidade_y
            velocidade_y += gravidade
            if dino_y >= chao_y - tamanho_dino:
                dino_y = chao_y - tamanho_dino
                pulo = False

        # Mover cactos
        for cacto in cactos:
            cacto[0] -= velocidade_jogo
        if cactos[-1][0] < larg - 300:
            cactos.append(gerar_cacto())
        if cactos[0][0] < -tamanho_dino:
            cactos.pop(0)
            pontos += 1

        # Colisão
        for cacto in cactos:
            if (dino_x < cacto[0] + tamanho_dino and
                dino_x + tamanho_dino > cacto[0] and
                dino_y + tamanho_dino > cacto[1]):
                rodando = False

        # Desenhar tudo
        desenhar_dino(dino_x, dino_y)
        desenhar_cactos(cactos)
        desenhar_pontuacao(pontos)

        pg.display.update()
        relogio.tick(30)

bora()
pg.quit()
