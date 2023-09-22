#Importando bibliotecas
import pygame
from pygame.locals import * 
from sys import exit

from enemy import Enemy
from lava import Lava


class World():
    
    #Construtor
    def __init__(self, tamanhoBloco):
        
        #Definindo Game Over
        self.game_over = 0
        
        #Definindo atributos para controlar o menu
        self.menu = True
        
        #Definindo um grupo  -> semelhante a uma lista no pygame
        #É útil, pois um jogo lida com várias quantidades de inimigos, por exemplo. Ter um grupo faz com que você possa modificar todos de vez
        self.enemy_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        
        #Definindo atributos
        self.listaBlocos = []
        self.tamanhoBloco = tamanhoBloco
        
        #Definindo a matriz que irá ser convertida em blocos
        self.matrizMundo = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0], 
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0], 
        [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0], 
        [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        
        #Carregando imagens
        chaoImagem = pygame.image.load('img/dirt.png')
        gramaImagem = pygame.image.load('img/grass.png')
        
        contadorLinhas = 0
        for linha in self.matrizMundo:
            contadorColunas = 0
            for bloco in linha:
                if bloco == 1:
                    
                    #Vou ler uma matriz com 0, 1 e 2 se for um, eu vou redimensionar a imagem chãoImg para o tamanho do bloco
                    #Scale(altura, largura -> (x,y)) 
                    imagemRedimensionada = pygame.transform.scale(chaoImagem, (self.tamanhoBloco, self.tamanhoBloco))
                    
                    #Associando a imagem redimensionada a um retângulo -> fica mais fácil trabalhar com retângulos  
                    retanguloImagem = imagemRedimensionada.get_rect()          
                    
                    #Reposicionando os blocos conforme a matriz 
                    retanguloImagem.x = contadorColunas * self.tamanhoBloco
                    retanguloImagem.y = contadorLinhas * self.tamanhoBloco
                    
                    #Agora o bloco possui a imagem redimensioanda do chão e o retângulo associado a ela
                    bloco = (imagemRedimensionada, retanguloImagem)
                    
                    #Adicionando o bloco à lista
                    self.listaBlocos.append(bloco)
                
                if bloco == 2:
                    
                    imagemRedimensionada = pygame.transform.scale(gramaImagem, (self.tamanhoBloco, self.tamanhoBloco))
                    
                    retanguloImagem = imagemRedimensionada.get_rect()

                    #Reposicionando os blocos conforme a matriz 
                    retanguloImagem.x = contadorColunas * self.tamanhoBloco
                    retanguloImagem.y = contadorLinhas * self.tamanhoBloco
                    
                    #Agora o bloco possui a imagem redimensioanda do chão e o retângulo associado a ela
                    bloco = (imagemRedimensionada, retanguloImagem)
                    
                    #Adicionando o bloco à lista
                    self.listaBlocos.append(bloco)
                
                if bloco == 3:
                    enemy = Enemy(contadorColunas * self.tamanhoBloco, (contadorLinhas * self.tamanhoBloco) +15)
                    self.enemy_group.add(enemy)
                    
                if bloco == 6:
                    lava =  Lava(contadorColunas * self.tamanhoBloco, (contadorLinhas * self.tamanhoBloco) + (tamanhoBloco//2), self.tamanhoBloco)
                    self.lava_group.add(lava)
                    
                contadorColunas = contadorColunas +1
            contadorLinhas = contadorLinhas +1
    
    #Função para desenhar/printar os blocos na tela
    def draw(self, tela):
     
        for bloco in self.listaBlocos:
            tela.blit(bloco[0], bloco[1])

                    
                    
                    
                    
                    
        