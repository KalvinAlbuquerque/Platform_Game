#Importando bibliotecas
import pygame
from pygame.locals import * 
import pickle
import os
from os import path

from enemy import Enemy
from lava import Lava
from gate import Gate


class World():
    
    #Construtor
    def __init__(self, tamanhoBloco, tela):
        
        #Definindo atributos
        self.tamanhoBloco = tamanhoBloco
        
        #Definindo Game Over
        self.game_over = 0
        
        #Definindo variável de controle de fases
        self.level = 1
        self.max_Levels = self.count_files()
        
        #Definindo atributos para controlar o menu
        self.menu = True
        
        #Definindo um grupo  -> semelhante a uma lista no pygame
        #É útil, pois um jogo lida com várias quantidades de inimigos, por exemplo. Ter um grupo faz com que você possa modificar todos de vez
        self.enemy_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        self.gate_group = pygame.sprite.Group()
        
        #Posição de inicio do player
        self.posicaoInicialPlayerX = 40
        self.posicaoInicialPlayerY = tela.get_height() - 130

        #Carregando o mundo
        self.loadingWorld(tamanhoBloco= self.tamanhoBloco, tela=tela)
        
        self.count_files()
    

        
    #Função para desenhar/printar os blocos na tela
    def draw(self, tela):
     
        for bloco in self.listaBlocos:
            tela.blit(bloco[0], bloco[1])

    #Função para carregar o mundo
    def loadingWorld(self, tamanhoBloco, tela):
        
        #Carregando nova fase
        #Lendo arquivo de fases e carregando-as para a memória
        #open(Arquivo que irei ler, r = read, b = binary)
        self.matrizMundo = []
        self.listaBlocos = []
        if path.exists(f'levels/level{self.level}_data'):
            pickle_in = open(f'levels/level{self.level}_data', 'rb')
            self.matrizMundo = pickle.load(pickle_in)
            print(self.matrizMundo)
        else: 
            print('Fase não existe!')
        
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
                    enemy = Enemy(contadorColunas * self.tamanhoBloco, (contadorLinhas * self.tamanhoBloco) + self.tamanhoBloco*0.3)
                    self.enemy_group.add(enemy)
                    
                if bloco == 6:
                    lava =  Lava(contadorColunas * self.tamanhoBloco, (contadorLinhas * self.tamanhoBloco) + (tamanhoBloco//2), self.tamanhoBloco)
                    self.lava_group.add(lava)
                
                if bloco == 8:
                    gate =  Gate(contadorColunas * self.tamanhoBloco, contadorLinhas * self.tamanhoBloco - (self.tamanhoBloco //2), self.tamanhoBloco)
                    self.gate_group.add(gate)    
                                    
                contadorColunas = contadorColunas +1
            contadorLinhas = contadorLinhas +1
    
    def count_files(self):

        #Caminho do diretório de onde irei contar os arquivos
        diretorio = 'levels'
        
        #Aqui estou listando todos os arquivos que há no diretório
        arquivos = os.listdir(diretorio)
        
        #Filtrando todos os arquivos que começam com "level"
        #Aqui estou usando uma lista de compreensão [elementoQueDesejoIncluirNaLista for iterator in range if condição]
        arquivosFiltrados = [arquivoFiltrado for arquivoFiltrado in arquivos if arquivoFiltrado.startswith("level")]
        
        #Contando quantos arquivos há no diretório
        quantidade_de_arquivos = len(arquivosFiltrados)
        
        #-1, pois até o presente momento o arquivo level_editor.py está no diretório 'levels'
        return quantidade_de_arquivos -1