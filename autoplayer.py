from world import World

class AutoPlayer():
    
    def __init__(self, world: World):

        self.autoPlayerMode = False
        self.move_Right = False
        self.move_Left = False
        self.jump  = False

        self.matriz = world.matrizMundo
        self.simPosPlayerX = 0
        self.simPosPlayerY = 17

        self.lista = []
        self.direita = 1
        self.esquerda = 2
        self._pular_direita = 3
        self._pular_esquerda = 4
        
        self.isBlock = False
        self.isEnemy = False
        self.isLava = False 
        self.isHole = False
        
    def resetSimPos(self):
        self.simPosPlayerX = 0
        self.simPosPlayerY = 17

    def andar_direita(self):
        self.lista.append(self.direita)
        self.simPosPlayerX = self.simPosPlayerX + 1
    
    def andar_esquerda(self):
        self.lista.append(self.esquerda)
        self.simPosPlayerX = self.simPosPlayerX - 1

    def pular_direita(self):
        self.lista.append(self._pular_direita)
        self.simPosPlayerX = self.simPosPlayerX + 1
    
    def pular_esquerda(self):
        self.lista.append(self._pular_esquerda)
        
    def tem_buraco_na_frente(self):
        y = self.simPosPlayerY + 1
        x = self.simPosPlayerX + self.direcao

        blocoNaFrente = self.world.matrizMundo[y][x] 

        if blocoNaFrente == 1 or blocoNaFrente == 2:
            self.autoPlayer.isBlock = True
        else:
            self.autoPlayer.isBlock = False
    
    def tem_lava_na_frente(self):
        y = self.simPosPlayerY + 2
        x = self.simPosPlayerX + self.direcao

        buraco = self.world.matrizMundo[y][x] 

        if buraco == 0 and self.in_air == False:
            self.autoPlayer.isHole = True
        else:
            self.autoPlayer.isHole = False
        
    def tem_inimigo_na_frente(self):
        y = self.simPosPlayerY + 2
        x = self.simPosPlayerX + self.direcao

        buraco = self.world.matrizMundo[y][x] 

        if buraco == 6:
            self.autoPlayer.isLava = True
        else:
            self.autoPlayer.isLava = False
            
    def tem_bloco_na_frente(self):
        y = self.simPosPlayerY + 1
        x = self.simPosPlayerX + self.direcao

        blocoNaFrente = self.world.matrizMundo[y][x] 

        if blocoNaFrente == 3:
            self.autoPlayer.isEnemy = True
        else:
            self.autoPlayer.isEnemy = False
        
         
    def resetMoves(self):
        self.move_Right = False
        self.move_Left = False
        self.jump  = False
            
    #daqui pra cima se mexer vai quebrar o jogo =(

    def lerMovimentos(self):
        
        # programe aqui =)
        
        
        
        return self.lista # não apague essa linha!


        
        
