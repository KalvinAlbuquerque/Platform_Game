import pygame
from world import World

import pickle
from os import path

class Player():
    
    #Construtor
    def __init__(self, x, y, world: World):
        
        #Atributo que controla o autoplayer
        self.world = world
        
        self.reset(x,y)
        
    #Função que reseta todas as variáveis e atributos da classe player
    #É chamada no construtor para facilitar quando ocorrer um game over e o usuário desejar reiniciar o jogo
    def reset(self, x,y):
        #Definindo atributos:
        
  
        self.game_over = 0
        #Atributos relacionados às sprites
        self.spritesDireita = []
        self.spritesEsquerda = []
        self.spriteID = 0
        self.contador = 0
        # '-1' -> esquerda/// '1' -> direita
        self.direcao = 0 
        
        #Carregando as imagens do jogador e redimensionando-as
        for num in range(1,5):
            spritesDireita = pygame.image.load(f'img/guy{num}.png')
            spritesDireita = pygame.transform.scale(spritesDireita, (self.world.tamanhoBloco * 0.8, self.world.tamanhoBloco *2 * 0.8))
            self.spritesDireita.append(spritesDireita)
            
            #A função flip possibilita inverter as imagens. Então se as sprites estavam se movimentando para a direita, agora ela irá se movimenta para esquerda
            #Flip(superfície, alterarMovimento em x, alterar movimento em Y)
            spritesEsquerda = pygame.transform.flip(spritesDireita, True, False)
            self.spritesEsquerda.append(spritesEsquerda)
            
        #Redimensionando o atributo imagem e definindo suas coordenadas 
        self.imagem = self.spritesDireita[self.spriteID]
        self.rect = self.imagem.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alturaJogador = self.imagem.get_height()
        self.larguraJogador = self.imagem.get_width()
        
        #Atributos relacionados à gravidade ao pular
        self.gravidade = 0
        self.jumped = False
        self.in_air = True
        
        #Atributos relacionados à morte do jogador:
        self.deadImage = pygame.image.load('img/ghost.png')
        
        self.autoPlayerMode = True
        
        self.isBlock = False
        self.isEnemy = False
        self.isHole = False
        self.isLava = False
        
        self.DIREITA = False
        self.ESQUERDA = False
        self.JUMP = False
        
    #Função que atualiza o jogador e suas características conforme o input do usuário
    def update(self, tela):
        if self.world.game_over == 0:
            
            deltaX = 0
            deltaY = 0 
            walk_cooldown = 10
            
            #Controlando se o jogador irá se mover no modo automático ou pelas setas
            if self.autoPlayerMode == False:
                #Recebendo os inputs para movimentar o player
                tecla = pygame.key.get_pressed()
                
                if tecla[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                    self.gravidade = -self.world.tamanhoBloco * 0.4
                    self.jumped = True
                if tecla[pygame.K_SPACE] == False: 
                    self.jumped = False
                if tecla[pygame.K_LEFT]:
                    deltaX -= self.world.tamanhoBloco * 0.1
                    self.contador += 1
                    self.direcao = -1
                if tecla[pygame.K_RIGHT]:
                    deltaX += self.world.tamanhoBloco * 0.1
                    self.contador += 1
                    self.direcao = 1
                
                #Caso o usuário pare de apertar K_RIGHT ou K_LEFT, a sprite do jogador irá voltar para a padrão, para que ele não fique em uma sprite aleatória
                if tecla[pygame.K_RIGHT] == False and tecla[pygame.K_LEFT] == False:
                    self.contador = 0
                    self.spriteID = 0 
                    if self.direcao == 1:
                        self.imagem = self.spritesDireita[self.spriteID]
                    if self.direcao == -1:
                        self.imagem = self.spritesEsquerda[self.spriteID]
            else:
                #Controlando movimentos com o autoPlayerMode
                if self.DIREITA:
                    deltaX += self.world.tamanhoBloco * 0.1
                    self.contador += 1
                    self.direcao = 1

                if self.ESQUERDA:
                    deltaX -= self.world.tamanhoBloco * 0.1
                    self.contador += 1
                    self.direcao = -1

                if  self.JUMP and self.jumped == False and self.in_air == False:
                    self.gravidade = -self.world.tamanhoBloco * 0.4
                    self.jumped = True
                elif self.JUMP == False:
                    self.jumped = False

            #Desenhando as animações do jogador
            if self.contador > walk_cooldown:
                self.contador = 0 
                self.spriteID += 1
                
                if self.spriteID >= len(self.spritesDireita):
                    self.spriteID = 0
                    
                #Definindo sprites conforme movimentos para esquerda ou direita
                if self.direcao == 1:
                    self.imagem = self.spritesDireita[self.spriteID]
                if self.direcao == -1:
                    self.imagem = self.spritesEsquerda[self.spriteID]

                
            
            #Simulando gravidade ao pular
            self.gravidade += 1
            if self.gravidade > self.world.tamanhoBloco*0.2:
                self.gravidade = self.world.tamanhoBloco*0.2
            deltaY += self.gravidade
            
            
            #Checando colisões (antes delas acontecerem)
            self.in_air = True
            for bloco in self.world.listaBlocos:
                
                #Checando colisão no eixo x
                #Se ele colidiu com algo no eixo x, basta impedi-lo de seguir adiante
                if bloco[1].colliderect(self.rect.x + deltaX, self.rect.y, self.larguraJogador, self.alturaJogador):
                    # self.autoPlayer.isStuck = True

                    deltaX = 0 
                #else:
                #    self.autoPlayer.isStuck = False
                #Checando colisão no eixo y 
                if bloco[1].colliderect(self.rect.x, self.rect.y + deltaY, self.larguraJogador, self.alturaJogador):
                    
                    #Checando se ele está embaixo de algum bloco ( se ele está pulando)
                    #Se a gravidade for negativa quer dizer que ele está subindo(pulando
                    #Caso ele se mova mais do que deveria e "bata" com a cabeça em um bloco, estou calculando a distância entre a cabeça do jogador e a parte
                    #de baixo do bloco com o qual ele irá colidir. Desta forma, o jogador irá se mover somente até essa parte de baixo do bloco.
                    if self.gravidade < 0:
                        deltaY = bloco[1].bottom - self.rect.top
                        self.gravidade = 0
                        
                    #De mesmo modo, estou checando se ele está acima de algum bloco. 
                    elif self.gravidade >= 0:
                        deltaY = bloco[1].top - self.rect.bottom
                        self.gravidade = 0
                        #Se o jogador colidiu com a parte de cima de um bloco, ele não está flutuando
                        self.in_air = False
            
            #Checando Game Over (Colisão com inimigos ou lava)
            #spritecollide(sprite1, sprite2, Se a sprite deve sumir após a colisão)
            if pygame.sprite.spritecollide(self, self.world.enemy_group, False):
                self.world.game_over = -1
                
            if pygame.sprite.spritecollide(self, self.world.lava_group, False):
                self.world.game_over = -1
                        
            #Atualizando as coordenadas do jogador (movimentando-o)
            self.rect.x += deltaX
            self.rect.y += deltaY
            
            #Checando colisão com portão de saída da fase
            if pygame.sprite.spritecollide(self, self.world.gate_group, False):
                self.world.game_over = 1 
        
        elif self.world.game_over == -1: 
            self.imagem = self.deadImage
            self.rect.y -= self.world.tamanhoBloco * 0.1
            
        #Desenhando o jogador
        #Lembre-se que blit pede a superfície/imagem que deseja printar e um retângulo ou uma tupla contendo as coordenadas (x,y) 
        tela.blit(self.imagem, self.rect)

        #Verificando colisões para o modo AutoPlayer
 
        #print('Tem bloco na frente')
        self.temBlocoNaFrente()
                
        self.temInimigoNaFrente()
        #print('TEM INIMIGO NA FRENTE')

        self.temLavaNaFrente()
        #print('TEM LAVA NA FRENTE')

        self.temBuracoNaFrente()
        #print('TEM BURACO NA FRENTE')

          
    #Deveria ficar na classe World, mas criaria dependência circular  
    #Função para resetarLevel
    def reset_Level(self, tela):
        
        self.reset(x=self.world.posicaoInicialPlayerX, y=self.world.posicaoInicialPlayerY)
        self.world.lava_group.empty()
        self.world.gate_group.empty()
        self.world.enemy_group.empty()
        self.world.loadingWorld(tamanhoBloco=self.world.tamanhoBloco, tela=tela)
        #Carregando nova fase
        #Lendo arquivo de fases e carregando-as para a memória
        #open(Arquivo que irei ler, r = read, b = binary)
        if path.exists(f'levels/level{self.world.level}_data'):
            pickle_in = open(f'levels/level{self.world.level}_data', 'rb')
            self.world.matrizMundo = pickle.load(pickle_in)
        else: 
            print('Fase não existe!')
            
    
    def temBlocoNaFrente(self):
        
        posPlayerX = round(self.rect.x / self.world.tamanhoBloco)
        posPlayerY = round(self.rect.y / self.world.tamanhoBloco)
        
        y = posPlayerY + 1
        x = posPlayerX + self.direcao

        blocoNaFrente = self.world.matrizMundo[y][x] 

        if blocoNaFrente == 1 or blocoNaFrente == 2:
            return True
        else:
            return False
                
    def temBuracoNaFrente(self):
          
        posPlayerX = round(self.rect.x / self.world.tamanhoBloco)
        posPlayerY = round(self.rect.y / self.world.tamanhoBloco)
        
        y = posPlayerY + 2
        x = posPlayerX + self.direcao

        buraco = self.world.matrizMundo[y][x] 

        if buraco == 0 and self.in_air == False:
            return True
        else:
            return False
        
    def temLavaNaFrente(self):
          
        posPlayerX = round(self.rect.x / self.world.tamanhoBloco)
        posPlayerY = round(self.rect.y / self.world.tamanhoBloco)
        
        y = posPlayerY + 2
        x = posPlayerX + self.direcao

        buraco = self.world.matrizMundo[y][x] 

        if buraco == 6:
            return True
        else:
            return False
        
    def temInimigoNaFrente(self):
            
        posPlayerX = round(self.rect.x / self.world.tamanhoBloco)
        posPlayerY = round(self.rect.y / self.world.tamanhoBloco)
        
        y = posPlayerY + 1
        x = posPlayerX + self.direcao

        blocoNaFrente = self.world.matrizMundo[y][x] 

        if blocoNaFrente == 3:
            return True
        else:
            return False
        