import pygame

class Player():
    
    def __init__(self, x, y):
        
        #Definindo atributos:
        
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
            spritesDireita = pygame.transform.scale(spritesDireita, (40,80))
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
        
        #Atributos relacionados à gravidade ao pular
        self.gravidade = 0
        self.jumped = False
        
        
    #Função que atualiza o jogador e suas características conforme o input do usuário
    def update(self, tela, alturaTela, LarguraTela):
        
        deltaX = 0
        deltaY = 0 
        walk_cooldown = 10
        
        #Recebendo os inputs para movimentar o player
        tecla = pygame.key.get_pressed()
        
        if tecla[pygame.K_SPACE] and self.jumped == False:
            self.gravidade = -15
            self.jumped = True
        if tecla[pygame.K_SPACE] == False: 
            self.jumped = False
        if tecla[pygame.K_LEFT]:
            deltaX -= 5
            self.contador += 1
            self.direcao = -1
        if tecla[pygame.K_RIGHT]:
            deltaX += 5
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
        if self.gravidade > 10:
            self.gravidade =10
        deltaY += self.gravidade
        
        #Checando colisões
        
        #Atualizando as coordenadas do jogador (movimentando-o)
        self.rect.x += deltaX
        self.rect.y += deltaY
        
        #Bottom é o y da parte inferior de um objeto, nesse caso o retângulo
        if self.rect.bottom > LarguraTela:
            self.rect.bottom  = LarguraTela
            deltaY = 0
        
        #Desenhando o jogador
        #Lembre-se que blit pede a superfície/imagem que deseja printar e um retângulo ou uma tupla contendo as coordenadas (x,y) 
        tela.blit(self.imagem, self.rect)
         