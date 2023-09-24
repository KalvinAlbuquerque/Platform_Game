class AutoPlayer():
    
    def __init__(self):

        self.autoPlayerMode = False
        self.move_Right = False
        self.move_Left = False
        self.move_Right_Pixels = 0
        self.jump  = False
        self.lista = []
        self.direita = 1
        self.esquerda = 2
        self._pular_direita = 3
        self._pular_esquerda = 4

    def andar_direita(self):
        self.lista.append(self.direita)
    
    def andar_esquerda(self):
        self.lista.append(self.esquerda)

    def pular_direita(self):
        self.lista.append(self._pular_direita)
    
    def pular_esquerda(self):
        self.lista.append(self._pular_esquerda)
         
    def resetMoves(self):
        self.move_Right = False
        self.move_Left = False
        self.jump  = False

    #daqui pra cima se mexer vai quebrar o jogo =(

    def lerMovimentos(self):
        
        # programe aqui =)

        for i in range(0, 2):
            self.andar_direita()

        for i in range(0, 8):
            self.pular_direita()
        
        for i in range(0, 2):
            self.andar_direita()

        for i in range(0, 3):
            self.andar_esquerda()

        

        return self.lista # não apague essa linha!


        
        
