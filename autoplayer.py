class AutoPlayer():
    
    def __init__(self,autoPlayerMode):

        self.autoPlayerMode = autoPlayerMode
        self.move_Right = False
        self.move_Left = False
        self.move_Right_Pixels = 0
        self.jump  = False
        
    def andar_Para_Direita(self):
        self.move_Right = True
        pixels = 50
        return pixels  
    
    def andar_Para_Esquerda(self):
        self.move_Left = True
        pixels = 50

        return pixels        
        
    def resetMoves(self):
        self.move_Right = False
        self.move_Left = False
        self.jump  = False
        
