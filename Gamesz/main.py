import pygame
from pygame.locals import *
from sys import exit  # fechar janela
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.3)
music_fundo = pygame.mixer_music.load('smw_course_clear.wav')
pygame.mixer_music.play(-1)  # -1 signifca que vai tocar repetidamente
music_colisao = pygame.mixer.Sound('smw_coin.wav')


# criar objeto tela

largura = 640
altura = 480
# posicao do objeto
x = 300
y = int(altura/2)
x_azul = randint(40, 600)
y_azul = randint(50, 430)
fonte = pygame.font.SysFont('gabriola', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Fogo e Água')
relogio = pygame.time.Clock()
pontos = 0

while True:
    relogio.tick(20)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, False, (255, 255, 255))
    # desenhar na tela
    # a tela do pygame segue coordenadas do plano cartesiano porém
    # o eixo y ele começa do 0 para baixo a partir do canto superio esquero
    # o eixo x começa no canto superior esquero e cresce para direita
    # as cores são passadas em rgb

    #pygame.draw.circle(tela, (0,0,255), (300, 260), 40)
    #pygame.draw.line(tela, (255,255,0), (390, 0), (390,600), 5 )

    # criar movimento nos objetos
    rect_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    rect_azul = pygame.draw.rect(tela, (0,0,255),(x_azul, y_azul, 40, 50))

    if rect_vermelho.colliderect(rect_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1
        music_colisao.play()

    if y >= altura:
        y = 0
    y = y + 5


    # condição para fechar o jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    # se pressionar e segurar a tecla a
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    tela.blit(texto, (450, 40))
    pygame.display.update()  # a cada iteração atualiza a tela do jogo



