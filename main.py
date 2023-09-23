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
#TO DO: ver onde as imagens de fundo e dos botões irão ficar, ficar em screen não faz sentido e ficar metade/metade também não faz sentido

#Botão de restart
restart_button = pygame.image.load('img/restart_btn.png')
restart_button = Button((screen.tela.get_width()//2), (screen.tela.get_height()//2), restart_button)

#Botão de start 
start_button = pygame.image.load('img/start_btn.png')
start_button = Button((screen.tela.get_width()//2) - (world.tamanhoBloco * 8), (screen.tela.get_height()//2), start_button)

#Botão de exit
exit_button = pygame.image.load('img/exit_btn.png')
exit_button = Button((screen.tela.get_width()//2) + (world.tamanhoBloco* 3) , (screen.tela.get_height()//2) , exit_button)

#Botões autoPlayerMode
autoPlayerMode_button_OFF = pygame.image.load('img/autoPlayerModeOFF.png')
autoPlayerMode_button_OFF = Button((screen.tela.get_width() - (world.tamanhoBloco * 3)), (screen.tela.get_height()//10) - (world.tamanhoBloco * 2), autoPlayerMode_button_OFF)

autoPlayerMode_button_ON = pygame.image.load('img/autoPlayerModeON.png')
autoPlayerMode_button_ON = Button((screen.tela.get_width() - (world.tamanhoBloco * 3)), (screen.tela.get_height()//10) - (world.tamanhoBloco * 2), autoPlayerMode_button_ON)




#Sysfont(Formato da fonte, tamanho do texto, negrito ou não, itálico ou não)
fonte = pygame.font.SysFont('arial', 40, True, True)
pontos = False 
  
#Andar_para_Direita()
#Andar_para_Direita()
#pular()
#Looping principal do jogo 
while True:

    
    screen.update()
    screen.draw_grid(world.tamanhoBloco)
    screen.define_clock(fps=500)
    
    
    #Printando menu de início
    if world.menu == True:
        if start_button.draw(screen.tela):
            world.menu = False
        if exit_button.draw(screen.tela):
            exit()
            
    else:
        
        #Habilitando e desabilitando autoPlayerMode
        if player.autoPlayer.autoPlayerMode == False:
            if autoPlayerMode_button_OFF.draw(screen.tela):
                player.autoPlayer.autoPlayerMode = True
                
        if player.autoPlayer.autoPlayerMode == True:
            if autoPlayerMode_button_ON.draw(screen.tela):
                player.autoPlayer.autoPlayerMode = False
                
        #Desenhando e atualizando recursos de mundo
        world.draw(screen.tela)
        world.enemy_group.draw(screen.tela)
        world.enemy_group.update()
        world.lava_group.draw(screen.tela)
        
        player.update(screen.tela, world)
        
        if pontos == False:
            player.autoPlayer.andar_Para_Direita()
            pontos = True
        
        #Verificando ocorreu game over para printar opções    
        if world.game_over == -1:
            
            #Se o usuário clicou no botão de restart a instância do player é resetada para o início do jogo
            if restart_button.draw(screen.tela):
                
                #Apenas para deixar claro: aqui reseto o player
                player.reset(x=100, y=screen.tela.get_height() - 130)
                #Aqui restarto o jogo
                world.game_over = 0
        
    #Verificando qualquer entrada(evento) para manter a interatividade do programa
    for event in pygame.event.get():

        #Habilitando o botão "xis" para encerrar o programa
        if event.type == QUIT:
            pygame.quit()
            exit()
            
               
    #Atualizando a tela a cada nova interação
    pygame.display.update()
    



