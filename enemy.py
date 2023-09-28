import pygame

#A classe enemy herda da classe Sprite
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x,y, tamanhoBloco):
        #Inicializando a classe Sprite
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando imagem e posicionando-a em uma coordenada
        self.image = pygame.image.load('img/blob.png')
        self.tamanhoBloco = tamanhoBloco
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movimentoEmX = 1
        self.contadorMovimento = 0
        
    def update(self):
        
        self.rect.x += self.movimentoEmX
        self.contadorMovimento += 1
    
        #Invertendo o sentido do movimento do inimigo, quando ele atinge determinado limite
        if abs(self.contadorMovimento) > self.tamanhoBloco//2:
            self.movimentoEmX *= -1
            self.contadorMovimento *= -1