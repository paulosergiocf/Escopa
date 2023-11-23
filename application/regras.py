from application.baralho import Baralho
from domain.entities.Jogador import Jogador
import random

class Regras():
    def quemCarteia( anterior: Jogador, jogadores: list):
        qntJogadores = len(jogadores)
        
        if anterior == None:
            return random.choice(jogadores)
        
        else:
            indice = jogadores.index(anterior)
            if qntJogadores < jogadores.index(anterior):
                return jogadores[indice+1]
                
            elif qntJogadores == jogadores.index(anterior):
                return jogadores[indice-1]
    
    def podePegar(cartas: list):
        soma = Regras.somarCartas(cartas)
        if soma == 15:
            return True
    
    def cartear(baralho: Baralho):
        mao = list()
        for indice in range(0,3):
            mao.append(baralho.comprar())
        return mao
    
    def somarCartas(cartas: list):
        """_summary_

        Args:
            cartas (list): lista de Cartas

        Returns:
            int: retorna a soma de todas as cartas da lista.
        """
        soma = 0
        if len(cartas) == 0:
            return soma
        
        for carta in cartas:
            if carta.id == 'K':
                soma += 10
            elif carta.id =='J':
                soma += 9
            elif carta.id == 'Q':
                soma += 8
            else:
                soma += carta.id
        
        return soma
    
    def tombar(baralho: Baralho):
        vira = list()
        
        for indice in range(0,4):
            vira.append(baralho.comprar())
        
        calcularVira = vira.copy()
        
        soma = Regras.somarCartas(calcularVira)
            
        if soma == 15:
            return vira, 1
        elif soma == 30:
            return vira, 2
        return vira, None