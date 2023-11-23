from domain.entities.cartas import Carta

class Mesa:
    def __init__(self):
        self.__mesa: Carta = list()
    
    @property
    def mesa(self):
        """pegar cartas da mesa"""
        return self.__mesa
    
    def addCarta(self, carta: Carta):
        """
        Args:
            carta (Carta): carta a ser adicionada na mesa
        """
        self.__mesa.append(Carta)
    
    def limparMesa(self):
        """limpar mesa"""
        self.__mesa = list()
        
        
    