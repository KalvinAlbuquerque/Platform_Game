import pygame

class Lava(pygame.sprite.Sprite):
    
    def __init__(self, x,y, tamanhoBloco):
        #Inicializando a classe Sprite
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando imagem e posicionando-a em uma coordenada
        image = pygame.image.load('img/lava.png')
        
        #Divido por 2, pois quero somente a metade do bloco
        self.image = pygame.transform.scale(image, (tamanhoBloco, tamanhoBloco // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
