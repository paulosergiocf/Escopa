
from domain.entities.cartas import Carta

class Jogador():
    def __init__(self, nome):
        self.__nome = nome
        self.__pontuacao = 0
        self.__monte: Carta = list()
        self.__escopa = 0
        self.__mao = list()
    
    def __str__(self):
        return f"{self.__nome}"
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pontuacao(self) :
        return self.__pontuacao
    
    @property
    def monte(self):
        return len(self.__monte)
    
    @property
    def escopa(self) :
        return self.__escopa
    
    @property
    def mao(self):
        return self.__mao
    
    
    def addEscopa(self):
        self.__escopa += 1
        
    def addCartaMao(self, carta: Carta):
        self.__mao.append(carta)