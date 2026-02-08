# configurações iniciais 
import pygame as pg
import random

pg.init()
pg.display.set_caption("Jogo snake Python")
larg, altu = 800, 600
tela = pg.display.set_mode((larg, altu))
relogio = pg.time.Clock()


# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0 ,0)
verde = (0, 255, 0)


# parametros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0, larg - tamanho_quadrado) / float(tamanho_quadrado))  * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altu - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pg.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])
    
    
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pg.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])
    
    
def  desenhar_pontuacao(pontuacao):
    fonte = pg.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1,1])

def selecionar_velocidade(tecla):
    if tecla == pg.K_DOWN or tecla == pg.K_s:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        
    elif tecla == pg.K_UP or tecla == pg.K_w:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        
        
    elif tecla == pg.K_RIGHT or tecla == pg.K_d:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0    
    
    elif tecla == pg.K_LEFT or tecla == pg.K_a:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    
    
    return velocidade_x, velocidade_y
    
    
def rodar_jogo():
    fim_jogo = False
    
    X = larg / 2
    Y = altu / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_cobra = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
    
    
    while not fim_jogo:
        tela.fill(preta)
        
        
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                fim_jogo = True
            elif evento.type == pg.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        # desenha_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
    
        
        # atuaslizar a posicao da cobra
        if X < 0 or X >= larg or Y < 0 or Y >= larg:
            fim_jogo = True
        
        
        X += velocidade_x
        Y += velocidade_y
        
        # desenhar_cobra 
        pixels.append([X, Y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        
        # se a cobrinha bateu no proprio corpo 
        for pixel in pixels[:-1]:
            if pixel == [X ,Y]:
                fim_jogo = True
        
        desenhar_cobra(tamanho_quadrado, pixels)
        
        # desenhar_pontos
        desenhar_pontuacao(tamanho_cobra - 1)
        
        
        # atualizacao tela
        pg.display.update()
        
        # criar uma nova comida
        if X == comida_x and Y == comida_y:
            tamanho_cobra += 1 
            comida_x, comida_y = gerar_comida()
        
        
        relogio.tick(velocidade_jogo)
        
        

# criar loop infinito

# desenhar objetos do jogo na tela
# pontuação
# cobrinha
# comida



# criar a lógica de terminar o jogo
# o que acontece:
# cobra bateu na parede
# cobra bateu na própria cobra


# pegar interações do usuário
# fechou a tela
# apertou as teclas do teclado pra mover a cobra

rodar_jogo()