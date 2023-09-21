import pygame

class Player():
    
    def __init__(self, x, y):
        
        #Definindo atributos:
        #Carregando a imagem do jogador
        imagem = pygame.image.load('img/guy1.png')
        
        #Redimensionando o atributo imagem e definindo suas coordenadas 
        self.imagem =  pygame.transform.scale(imagem, (40,80))
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravidade = 0
        self.jumped = False
    
    def update(self, tela, alturaTela, LarguraTela):
        
        deltaX = 0
        deltaY = 0 
        
        #Recebendo os inputs para movimentar o player
        tecla = pygame.key.get_pressed()
        
        if tecla[pygame.K_SPACE] and self.jumped == False:
            self.gravidade = -15
            self.jumped = True
        if tecla[pygame.K_SPACE] == False: 
            self.jumped = False
        if tecla[pygame.K_LEFT]:
            deltaX -= 5
        if tecla[pygame.K_RIGHT]:
            deltaX += 5
        
        self.gravidade += 1
        if self.gravidade > 10:
            self.gravidade =10
        deltaY += self.gravidade
        #Checando colisões
        
        #Atualizando as coordenadas do jogador (movimentando-o)
        self.rect.x += deltaX
        self.rect.y += deltaY
        
        #Bottom é o y da parte inferior de um objeto, nesse caso o retângulo
        if self.rect.bottom > LarguraTela:
            self.rect.bottom  = LarguraTela
            deltaY = 0
        
        #Desenhando o jogador
        #Lembre-se que blit pede a superfície/imagem que deseja printar e um retângulo ou uma tupla contendo as coordenadas (x,y) 
        tela.blit(self.imagem, self.rect)
         