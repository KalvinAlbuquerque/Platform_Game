#Importando bibliotecas externas
import pygame
from pygame.locals import * 
from sys import exit

#Importando bibliotecas locais
from world import World
from player import Player
from screen import Screen

#Inicializando as classes necessárias 
pygame.init()
screen = Screen(alturaTela=1000,larguraTela=1000)
player = Player(x=100, y=screen.tela.get_height() - 130)
world = World(tamanhoBloco=50)

#Sysfont(Formato da fonte, tamanho do texto, negrito ou não, itálico ou não)
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0 
  

#Looping principal do jogo 
while True:

    screen.update()
    screen.draw_grid(world.tamanhoBloco)
    screen.define_clock(fps=500)
    
    world.draw(screen.tela)
    player.update(screen.tela, screen.tela.get_height(), screen.tela.get_width())
    
    #Verificando qualquer entrada(evento) para manter a interatividade do programa
    for event in pygame.event.get():

        #Habilitando o botão "xis" para encerrar o programa
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Atualizando a tela a cada nova interação
    pygame.display.update()


