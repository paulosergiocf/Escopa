
from application.baralho import Baralho
from domain.entities import Jogador
import random

class Rodada():
    def __init__(self):
        self.__baralho = Baralho()
        self.__carteador: Jogador = None
        self.__baralho.embaralhar()
                
    
    @property
    def baralho(self):
        return self.__baralho
    
    @property
    def carteador(self):
        return self.carteador
    
    def quemCarteia(self, anterior: Jogador, jogadores: list):
        qntJogadores = len(jogadores)
        if anterior == None:
            self.quemCarteia = random.shuffle(jogadores)
        
        else:
            indice = jogadores.index(anterior)
            if qntJogadores < jogadores.index(jogador):
                jogador = jogadores[indice+1]
                
            elif qntJogadores == jogadores.index(jogador):
                jogador = jogadores[indice-1]
    
        return self.__carteador
    
    