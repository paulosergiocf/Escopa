
from domain.entities.mesa import Mesa
from domain.entities.Jogador import Jogador


class Jogo:
    def __init__(self):
        self.jogadores = list()
        self.mesa = Mesa()
        self.estado = False
    
    
    def adicionarJogador(self, jogador: Jogador):
        self.jogadores.append(jogador)
    
    def game(self):
        pass
    
        
    def fim_de_jogo(self):
        for jogador in self.jogadores:
            if jogador.pontuacao >= 15:
                self.estado = False
                