#Importando bibliotecas externas
import pygame
from pygame.locals import * 
from sys import exit
import math

#Importando bibliotecas locais
from world import World
from player import Player
from screen import Screen
from button import Button
           
    
class Jogo():
    
    def __init__(self):
        self.DIREITA = False
        self.ESQUERDA = False
        self.JUMP = False
        
        self.max_pixels = 12
        self.pixel_atual = 0
        
        self.executing = True
        
        pygame.init()

        self.alturaTela = 680
        self.larguraTela = 680
        self.quantidadeBlocos = 400
        self.tamanhoBloco = math.sqrt((self.alturaTela * self.larguraTela)/self.quantidadeBlocos)

        self.screen = Screen(alturaTela=self.alturaTela,larguraTela=self.larguraTela)
        self.world = World(tamanhoBloco=self.tamanhoBloco, tela=self.screen.tela)
        self.player = Player(x=self.world.posicaoInicialPlayerX, y=self.world.posicaoInicialPlayerY, world=self.world)

        #Variáveis para controlar movimento do autoPlayerMode


        #Criando botões 
        
        #Botão de restart
        self.restart_button = pygame.image.load('img/restart_btn.png')
        self.restart_button = Button((self.screen.tela.get_width()//2), (self.screen.tela.get_height()//2), self.restart_button)

        #Botão de start 
        self.start_button = pygame.image.load('img/start_btn.png')
        self.start_button = Button((self.screen.tela.get_width()//2) - (self.world.tamanhoBloco * 9), (self.screen.tela.get_height()//2), self.start_button)

        #Botão de exit
        self.exit_button = pygame.image.load('img/exit_btn.png')
        self.exit_button = Button((self.screen.tela.get_width()//2) + (self.world.tamanhoBloco* 2) , (self.screen.tela.get_height()//2) , self.exit_button)

        #Botões autoPlayerMode
        self.autoPlayerMode_button_OFF = pygame.image.load('img/autoPlayerModeOFF.png')
        self.autoPlayerMode_button_OFF = Button((self.screen.tela.get_width() - (self.world.tamanhoBloco * 3)), (self.screen.tela.get_height()//10) - (self.world.tamanhoBloco * 2), self.autoPlayerMode_button_OFF)

        self.autoPlayerMode_button_ON = pygame.image.load('img/autoPlayerModeON.png')
        self.autoPlayerMode_button_ON = Button((self.screen.tela.get_width() - (self.world.tamanhoBloco * 3)), (self.screen.tela.get_height()//10) - (self.world.tamanhoBloco * 2), self.autoPlayerMode_button_ON)
        
        #Botão de visualizar a grade do jogo
        self.grid_ON = pygame.image.load('img/comGrade.png')
        self.grid_ON = Button(0 + self.tamanhoBloco * 1 * 0.3, (self.screen.tela.get_height()//10) - (self.world.tamanhoBloco * 2), self.grid_ON)
        
        self.grid_OFF = pygame.image.load('img/semGrade.png')
        self.grid_OFF = Button(0 + self.tamanhoBloco * 1 * 0.3, (self.screen.tela.get_height()//10) - (self.world.tamanhoBloco * 2), self.grid_OFF)


    def andar_para_direita(self):
        while(self.pixel_atual is not self.max_pixels):
            self.player.DIREITA = True
            self.update()
            self.pixel_atual += 1
        
        self.pixel_atual = 0
        self.reset_movs()
    
    def andar_para_esquerda(self):
        while(self.pixel_atual is not self.max_pixels):
            self.player.ESQUERDA = True
            self.update()
            self.pixel_atual += 1
        
        self.pixel_atual = 0
        self.reset_movs()
    
    def pular_para_direita(self):
        while(self.pixel_atual is not self.max_pixels):
            self.player.DIREITA = True
            self.player.JUMP = True
            self.update()
            self.pixel_atual += 1
        
        self.pixel_atual = 0
        self.reset_movs()
            
    def pular_para_esquerda(self):
        while(self.pixel_atual is not self.max_pixels):
            self.player.ESQUERDA = True
            self.player.JUMP = True
            self.update()
            self.pixel_atual += 1
        
        self.pixel_atual = 0
        self.reset_movs()
    
    def esperar(self):
        while(self.pixel_atual is not self.max_pixels):
            self.update()
            self.pixel_atual += 1
        
        self.pixel_atual = 0
        self.reset_movs()
    
    def reset_movs(self):
        self.player.DIREITA = False
        self.player.ESQUERDA = False
        self.player.JUMP = False

    def comandos(self):
        ...
        
        
        #Programe aqui! 

#Inicializando as classes necessárias 

#Lista para controlar a ordem dos movimentos quando o autoPlayerMode estiver ativo

    def update(self):
        
        
            jogo.screen.update()
            jogo.screen.define_clock(fps=100)
            
            #Desenhando e atualizando recursos de mundo
            self.world.draw(self.screen.tela)
            self.world.enemy_group.draw(self.screen.tela)
            self.world.enemy_group.update()
            self.world.lava_group.draw(self.screen.tela)
            self.world.gate_group.draw(self.screen.tela)
            self.world.coin_group.draw(self.screen.tela)
            self.player.update(self.screen.tela)
            
            if self.world.menu == False:
                self.world.draw_text('SCORE: ' + str(self.world.score), self.world.fonte_score, self.world.cor_score, self.world.tamanhoBloco * 18, 10, self.screen.tela)
                self.world.draw_text('LEVEL: ' + str(self.world.level), self.world.fonte_score, self.world.cor_score, self.tamanhoBloco * 18, 30, self.screen.tela)
                    
            #Desenhando grade, pode comentar caso não queira que apareça
            if jogo.screen.visualizarGrade == True:
                jogo.screen.draw_grid(jogo.world.tamanhoBloco)
    
            #Verificando ocorreu game over 
            #Se game over == 0 jogo continua
            #Game over == 1, mudança de fase
            #Game over = -1, fim de jogo  
            if self.world.game_over == -1:
                
                #Se o usuário clicou no botão de restart a instância do player é resetada para o início do jogo
                if self.restart_button.draw(self.screen.tela):
                    
                    #Apenas para deixar claro: aqui reseto o player
                    self.player.reset(x=self.world.posicaoInicialPlayerX, y=self.world.posicaoInicialPlayerY)
                    #Aqui restarto o jogo
                    self.world.game_over = 0
                
            if self.world.game_over == 1:
                #Se o player passou de fase, então reseto o jogo e passo a fase
                self.world.level += 1
                
                #Verificando se o level que estou passando existe
                if self.world.level <= self.world.max_Levels:
                    #Resetando self.world
                    self.player.reset_Level(self.screen.tela)
                    self.world.game_over = 0
                    
            #Desenhando botão de habilitar e desabilitar grade
            if jogo.screen.visualizarGrade == False:
                if jogo.grid_OFF.draw(jogo.screen.tela):
                    jogo.screen.visualizarGrade = True
                
            if jogo.screen.visualizarGrade == True:
                if jogo.grid_ON.draw(jogo.screen.tela):
                    jogo.screen.visualizarGrade = False
                    
            if self.world.level == self.world.max_Levels+1:
                self.world.menu = True 
            if jogo.world.menu == True:
                if jogo.start_button.draw(jogo.screen.tela):
                    jogo.world.menu = False
                    jogo.world.level = 0
                if jogo.exit_button.draw(jogo.screen.tela):
                    exit()

            
            #Verificando qualquer entrada(evento) para manter a interatividade do programa
            for event in pygame.event.get():

                #Habilitando o botão "xis" para encerrar o programa
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            
            #Atualizando a tela a cada nova interação
            pygame.display.update()


jogo = Jogo()



#Looping principal do jogo 
while jogo.world.menu:
    
    jogo.screen.update()
    jogo.screen.define_clock(fps=100)
    
    #Printando menu de início
    if jogo.world.menu == True:
        if jogo.start_button.draw(jogo.screen.tela):
            jogo.world.menu = False
            break
        if jogo.exit_button.draw(jogo.screen.tela):
            exit()
    
        #Habilitando e desabilitando autoPlayerMode
        if jogo.player.autoPlayerMode == False:
            if jogo.autoPlayerMode_button_OFF.draw(jogo.screen.tela):
                jogo.player.autoPlayerMode = True                
                
        if jogo.player.autoPlayerMode == True:
            if jogo.autoPlayerMode_button_ON.draw(jogo.screen.tela):
                jogo.player.autoPlayerMode = False
                
        #Verificando qualquer entrada(evento) para manter a interatividade do programa
        for event in pygame.event.get():

            #Habilitando o botão "xis" para encerrar o programa
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        #Atualizando a tela a cada nova interação
        pygame.display.update()
 
jogo.comandos()

while True:
    jogo.update()
        


 