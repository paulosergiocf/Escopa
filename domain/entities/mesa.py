from domain.entities.Jogador import Jogador
from domain.entities.cartas import Carta
from domain.entities.rodada import Rodada

class Mesa:
    def __init__(self):
        self.__mesa: Carta = list()
        self.__jogadores: Jogador = list()
        self.__rodada: Rodada = None
    
    @property
    def mesa(self):
        return self.__mesa
    
    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def rodada(self):
        return self.__rodada
    
    def iniciarRodada(self):
        self.__rodada = Rodada()
    