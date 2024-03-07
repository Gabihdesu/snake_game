import pygame
from pygame.locals import *
from sys import exit  # fechar janela
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.3)
music_fundo = pygame.mixer_music.load('smw_course_clear.wav')
#pygame.mixer_music.play(-1)  # -1 signifca que vai tocar repetidamente
music_colisao = pygame.mixer.Sound('smw_coin.wav')


# criar objeto tela

largura = 640
altura = 480
# posicao do objeto
x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

lista_cobra = []
comprimento_cobra = 5

fonte = pygame.font.SysFont('arial', 40, True, True)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snack game')
relogio = pygame.time.Clock()

pontos = 0
morreu = False


def aumenta_cobra(lista):
    for XeY in lista:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_cobra, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_cobra = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))

    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, False, (0, 0, 0))

    # condição para fechar o jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle

    # criar movimento nos objetos
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    # quando colidir com a maçã
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        music_colisao.play()
        comprimento_cobra += 1

    lista_cabeca = []

    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        perdeu_msg = 'Game over ! Pressione a tecla R para reiniciar o jogo'
        texto_perdeu = fonte2.render(perdeu_msg, True, (0, 0, 0) )
        rect_texto = texto_perdeu.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            rect_texto.center = (largura//2, altura//2)
            tela.blit(texto_perdeu, rect_texto) # // divisão retorn inteiro
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto, (450, 40))
    pygame.display.update()  # a cada iteração atualiza a tela do jogo



