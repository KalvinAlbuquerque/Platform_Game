class AutoPlayer():
    
    def __init__(self):

        self.autoPlayerMode = False
        self.move_Right = False
        self.move_Left = False
        self.jump  = False
        
        self.lista = []
        self.direita = 1
        self.esquerda = 2
        self._pular_direita = 3
        self._pular_esquerda = 4
        
        self.isBlock = False
        self.isEnemy = False
        self.isLava = False 
        self.isHole = False
        
    def andar_direita(self):
        self.lista.append(self.direita)
    
    def andar_esquerda(self):
        self.lista.append(self.esquerda)

    def pular_direita(self):
        self.lista.append(self._pular_direita)
    
    def pular_esquerda(self):
        self.lista.append(self._pular_esquerda)
        
    def tem_buraco_na_frente(self):
        if self.isHole:
            return True
        else:
            return False  
    
    def tem_lava_na_frente(self):
        if self.isLava:
            return True
        else:
            return False  
        
    def tem_inimigo_na_frente(self):
        if self.isEnemy:
            return True
        else:
            return False    
            
    def tem_bloco_na_frente(self):
        if self.isBlock:
            print('Tem bloco aqui')
            return True
        else:
            return False    
         
    def resetMoves(self):
        self.move_Right = False
        self.move_Left = False
        self.jump  = False
            
    #daqui pra cima se mexer vai quebrar o jogo =(

    def lerMovimentos(self):
        
        # programe aqui =)
        
        
        
        return self.lista # não apague essa linha!


        
        
