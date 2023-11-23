
import random
from domain.entities.cartas import Carta, Naipe

class Baralho:
    """
    Conjunto de cartas 
    metodos: 
     - iniciar: cria braranho de 40 cartas
     - embaralhar: embaralha cartas do baralho
     - comprar: remove uma carta do baralho e a retorna
     - qntCartas: retorna quantidade de cartas restantes
     
    """
    def __init__(self):
        self.__cartas: Carta = list()
        self.__situacao = False
        self.__qntCartas = 0
        self.inicio()
    
    @property
    def cartas(self):
        return self.__cartas
    
    @property
    def qntCartas(self):
        return self.__qntCartas
    
    def comprar(self):
        if self.__situacao:
            carta =  self.__cartas[0]
            self.__cartas.pop(0)
            self.verificarSituacao()
            return carta
        
        return ValueError("Sem cartas para comprar")
    
    
    def inicio(self):
        """
        Criar bartalho com todas as cartas nescessárias
        """
        ids = [1,2,3,4,5,6,7,"J","Q","K"]
        
        naipes = [
            Naipe(1, "Paus"),
            Naipe(2, "Copas"),
            Naipe(3, "Espadas"),
            Naipe(4, "Ouros")
        ]
        
        for naipe in naipes:
            for id in ids:
                self.__cartas.append(Carta(id, naipe))
                
        self.verificarSituacao()
                
    def embaralhar(self):
        """
        Ordena aleatóriamente as cartas de um baralho
        """
        random.shuffle(self.__cartas)
     
    def verificarSituacao(self):
        quantidadeCartas = len(self.__cartas)
        if quantidadeCartas == 0:     
            self.__situacao = False
        else:
            self.__situacao = True
            
        self.__qntCartas = quantidadeCartas