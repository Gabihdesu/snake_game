import pygame
from pygame.locals import *
from sys import exit  # fechar janela
from random import randint


class SnakeGame():
    def __init__(self):
        pygame.init()
        # criar objeto tela
        pygame.display.set_caption('Snack game')
        self.largura = 640
        self.altura = 480
        # posicao do objeto
        self.x_cobra = int(self.largura/2)
        self.y_cobra = int(self.altura/2)

        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0

        self.x_maca = randint(40, 600)
        self.y_maca = randint(50, 430)

        self.lista_cobra = []
        self.comprimento_cobra = 5

        self.fonte = pygame.font.SysFont('arial', 40, True, True)
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        self.relogio = pygame.time.Clock()

        self.pontos = 0
        self.morreu = False
        self.Jogo()

    def aumenta_cobra(self, lista):
        for XeY in lista:
            #XeY = [x, y]
            #XeY[0] = x
            #XeY[1] = y
            pygame.draw.rect(self.tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

    def reiniciar_jogo(self):
        self.pontos = 0
        self.comprimento_cobra = 5
        self.x_cobra = int(self.largura / 2)
        self.y_cobra = int(self.altura / 2)
        self.lista_cobra = []
        self.lista_cabeca = []
        self.x_maca = randint(40, 600)
        self.y_maca = randint(50, 430)
        self.morreu = False

    def Jogo(self):
        pygame.mixer.music.set_volume(0.3)
        self.music_fundo = pygame.mixer.music.load('smw_course_clear.wav')  # Fix this line
        pygame.mixer.music.play(-1)  # -1 signifies that it will play repeatedly
        self.music_colisao = pygame.mixer.Sound('smw_coin.wav')

        while True:
            self.relogio.tick(30)
            self.tela.fill((255, 255, 255))

            mensagem = f'Pontos: {self.pontos}'
            texto = self.fonte.render(mensagem, False, (0, 0, 0))

            # condição para fechar o jogo
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if self.x_controle == self.velocidade:
                            pass
                        else:
                            self.x_controle = -self.velocidade
                            self.y_controle = 0
                    if event.key == K_d:
                        if self.x_controle == -self.velocidade:
                            pass
                        else:
                            self.x_controle = self.velocidade
                            self.y_controle = 0
                    if event.key == K_w:
                        if self.y_controle == self.velocidade:
                            pass
                        else:
                            self.y_controle = -self.velocidade
                            self.x_controle = 0
                    if event.key == K_s:
                        if self.y_controle == -self.velocidade:
                            pass
                        else:
                            self.y_controle = self.velocidade
                            self.x_controle = 0

            self.x_cobra += self.x_controle
            self.y_cobra += self.y_controle

            # criar movimento nos objetos
            cobra = pygame.draw.rect(self.tela, (0, 255, 0), (self.x_cobra, self.y_cobra, 20, 20))
            maca = pygame.draw.rect(self.tela, (255, 0, 0), (self.x_maca, self.y_maca, 20, 20))

            # quando colidir com a maçã
            if cobra.colliderect(maca):
                self.x_maca = randint(40, 600)
                self.y_maca = randint(50, 430)
                self.pontos += 1
                self.music_colisao.play()
                self.comprimento_cobra += 1

            lista_cabeca = []

            lista_cabeca.append(self.x_cobra)
            lista_cabeca.append(self.y_cobra)
            self.lista_cobra.append(lista_cabeca)

            if self.lista_cobra.count(lista_cabeca) > 1:
                fonte2 = pygame.font.SysFont('arial', 20, True, True)
                perdeu_msg = 'Game over ! Pressione a tecla R para reiniciar o jogo'
                texto_perdeu = fonte2.render(perdeu_msg, True, (0, 0, 0) )
                rect_texto = texto_perdeu.get_rect()

                self.morreu = True
                while self.morreu:
                    self.tela.fill((255,255,255))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                self.reiniciar_jogo()
                    rect_texto.center = (self.largura//2, self.altura//2)
                    self.tela.blit(texto_perdeu, rect_texto) # // divisão retorn inteiro
                    pygame.display.update()

            if self.x_cobra > self.largura:
                self.x_cobra = 0
            if self.x_cobra < 0:
                self.x_cobra = self.largura
            if self.y_cobra < 0:
                self.y_cobra = self.altura
            if self.y_cobra > self.altura:
                self.y_cobra = 0

            if len(self.lista_cobra) > self.comprimento_cobra:
                del self.lista_cobra[0]

            self.aumenta_cobra(self.lista_cobra)

            self.tela.blit(texto, (450, 40))
            pygame.display.update()  # a cada iteração atualiza a tela do jogo


if __name__ == '__main__':
    SnakeGame()
