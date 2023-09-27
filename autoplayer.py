class AutoPlayer():
    
    def __init__(self):

        self.autoPlayerMode = False
        self.move_Right = False
        self.move_Left = False
        self.jump  = False
        
        self.listaMovimentos = []
        self.direita = (1,False)
        self.esquerda = (2,False)
        self._pular_direita = (3,False)
        self._pular_esquerda = (4,False)
        
        self.listaVerificacoes = []
        self.verificarBloco = (5,False)
        self.isEnemy = False
        self.isLava = False 
        self.isHole = False
        self.isBlock = False
        
    #Funções para movimentar o jogador automaticamente
    def andar_direita(self):
        self.listaMovimentos.append(self.direita)
    
    def andar_esquerda(self):
        self.listaMovimentos.append(self.esquerda)

    def pular_direita(self):
        self.listaMovimentos.append(self._pular_direita)
    
    def pular_esquerda(self):
        self.listaMovimentos.append(self._pular_esquerda)
        
    #Funções para verificar a colisão com elementos dentro do jogo
    def tem_bloco_na_frente(self):
        self.listaMovimentos.append(self.verificarBloco)
        
        if self.isHole:
            return True
        else:
            return False
            
 
         
    def resetMoves(self):
        self.move_Right = False
        self.move_Left = False
        self.jump  = False
        
    def lerMovimentos(self):
        
        boneco = AutoPlayer()

        boneco.andar_direita()
        boneco.andar_direita()
        
        if boneco.tem_bloco_na_frente():
            boneco.pular_direita()

        print(boneco.listaMovimentos)
        
        return boneco.listaMovimentos


        
        
