import pygame

class Button():
    
    #Construtor
    def __init__(self, x,y, imagem):
        
        #Defininfo atributos do botão e reposicionando-o
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.clicked = False
        
    #Método para desenhar/printar o botão
    def draw(self,tela):
        
        action = False
        #Checando a posição do cursor do mouse
        mousePosition = pygame.mouse.get_pos()
        
        #Checando cliques
        if self.rect.collidepoint(mousePosition):
            
            # 0 -> botão esquerdo, 1 -> botão direito
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                action = True
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False
                
        tela.blit(self.imagem, self.rect)
        
        return action