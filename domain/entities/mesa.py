from jogador import Jogador

class Mesa:
    def __init__(self):
        self.__mesa = list()
        self.__jogadores: Jogador = list()
    
    @property
    def mesa(self):
        return self.__mesa
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    