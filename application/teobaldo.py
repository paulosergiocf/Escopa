from application.regras import Regras
from domain.entities.Jogador import Jogador
from domain.entities.cartas import Carta

class Teobaldo(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
        
    def jogar(self):
        pass
    
    def analisarProximaJogada(self, mesa: list):
        somaMesa = Regras.somarCartas(mesa)
        
        if somaMesa < 15:
            for carta in self.mao:
                listaMesa = mesa.copy()
                listaMesa.append(carta)
                
                if Regras.somarCartas(listaMesa) == 15:
                    return ''
        