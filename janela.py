import pygame

#Importando funções do módulo locals
from pygame.locals import * 

#Importando função exit do módulo sys -> para fechar a janela no "x"
from sys import exit

#Inicializando a classe
pygame.init()

#Instanciando a janela (Recebe largura e altura)
largura = 1024
altura = 680
tela = pygame.display.set_mode((largura, altura))

#Looping principal do jogo - é infinito, pois o jogo deve continuar até que o usuário deseje sair
while True:
    #Como é um sistema interativo, sempre verifico se o usuário está dando input em algo
    for event in pygame.event.get():
        #Para que o botão de fechar o jogo funcione, devo criar esse evento dentro das interações do sistema
        if event.type == QUIT:
            pygame.quit()
            exit()
        #Aqui estou atualizando a tela a cada interação que ocorrer
        pygame.display.update()

