import pygame

class Screen():

    #Construtor
    def __init__ (self, larguraTela, alturaTela):
        
        #Definindo atributos
        #Instanciando a tela do jogo
        self.tela = pygame.display.set_mode((larguraTela, alturaTela), pygame.RESIZABLE) 
        pygame.display.set_caption('Game')
        
    def update(self):
        
        #Carregando imagens
        imagemSol = pygame.image.load('img/sun.png')
        imagemCeu = pygame.image.load('img/sky.png')
        
        #Desenhando imagens
        self.tela.blit(imagemCeu,(0,0))
        self.tela.blit(imagemSol, (100,100))
    
    #Função para desenhar grades na tela. Útil para visualizar a janela repartida em retângulos
    def draw_grid(self, tamanhoBloco):
        
        for line in range(0, 20):
            
            pygame.draw.line(self.tela, (255, 255, 255), (0, line * tamanhoBloco), (self.tela.get_width(), line * tamanhoBloco))
            pygame.draw.line(self.tela, (255, 255, 255), (line * tamanhoBloco, 0), (line * tamanhoBloco, self.tela.get_height()))
        
    #Função que limite a taxa de frames por segundo
    def define_clock(self, fps):
        clock = pygame.time.Clock()
        clock.tick(fps)
        