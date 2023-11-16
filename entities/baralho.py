
from entities.cartas import Naipe, Cartas

class Baralho:
    def __init__(self):
        self.__cartas = list()
        self.inicio()
    
    @property
    def cartas(self):
        return self.__cartas
    
    def inicio(self):
        ids = [1,2,3,4,5,6,7,"j","q","k"]
        
        naipes = [
            Naipe(1, "Paus"),
            Naipe(2, "Copas"),
            Naipe(3, "Espadas"),
            Naipe(4, "Ouros")
        ]
        
        for naipe in naipes:
            for id in ids:
                self.__cartas.append(Cartas(id, naipe))
                