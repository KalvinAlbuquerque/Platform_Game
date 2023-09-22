#Importando bibliotecas externas
import pygame
from pygame.locals import * 
from sys import exit

#Importando bibliotecas locais
from world import World
from player import Player
from screen import Screen
from button import Button

#Inicializando as classes necessárias 
pygame.init()

screen = Screen(alturaTela=1000,larguraTela=1000)
player = Player(x=100, y=screen.tela.get_height() - 130)
world = World(tamanhoBloco=50)

#Criando botões
restart_button = pygame.image.load('img/restart_btn.png')
restart_button = Button((screen.tela.get_width()//2)-50 , (screen.tela.get_height()//2) +100, restart_button)


#Sysfont(Formato da fonte, tamanho do texto, negrito ou não, itálico ou não)
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = 0 
  

#Looping principal do jogo 
while True:

    screen.update()
    screen.draw_grid(world.tamanhoBloco)
    screen.define_clock(fps=500)
    
    world.draw(screen.tela)
    world.enemy_group.draw(screen.tela)
    world.enemy_group.update()
    world.lava_group.draw(screen.tela)
    
    player.update(screen.tela, world)
    
    #Verificando qualquer entrada(evento) para manter a interatividade do programa
    for event in pygame.event.get():

        #Habilitando o botão "xis" para encerrar o programa
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Verificando ocorreu game over para printar opções    
    if world.game_over == -1:
        
        #Se o usuário clicou no botão de restart a instância do player é resetada para o início do jogo
        if restart_button.draw(screen.tela):
            
            #Apenas para deixar claro: aqui reseto o player
            player.reset(x=100, y=screen.tela.get_height() - 130)
            #Aqui restarto o jogo
            world.game_over = 0
               
    #Atualizando a tela a cada nova interação
    pygame.display.update()
    



