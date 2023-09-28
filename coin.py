import pygame

class Coin(pygame.sprite.Sprite):
    
    def __init__(self, x,y, tamanhoBloco):
        #Inicializando a classe Sprite
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando imagem e posicionando-a em uma coordenada
        image = pygame.image.load('img/coin.png')
        
        #Divido por 2, pois quero somente a metade do bloco
        self.image = pygame.transform.scale(image, (tamanhoBloco // 2, tamanhoBloco // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.center = (x,y)
