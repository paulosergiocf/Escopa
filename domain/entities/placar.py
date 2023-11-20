
class PlacarRodada:
    def __init__(self):
        self.__escopa = 0
        self.__belo = 0
        self.__primeira = 0
        self.__ouro = 0
        self.__carta = 0        
        
    @property
    def escopa(self):
        return self.__escopa

    @property
    def belos(self):
        return self.__belo

    @property
    def carta(self):
        return self.__carta

    @property
    def primeira(self):
        return self.__primeira

    @property
    def ouro(self):
        return self.__ouro
    
    @property
    def cartas(self):
        return self.__cartas
    
    def adicionarEscopa(self):
        self.__escopa += 1
        
    def adicionarBelo(self):
        self.__belo += 1
        
    def adicionarPrimeira(self):
        self.__primeira += 1
        
    def adicionarCarta(self):
        self.__carta += 1
        
    def adicionarOuro(self):
        self.__ouro += 1
        
    def limparPlacar(self):
        self.__escopa = 0
        self.__belo = 0
        self.__primeira = 0
        self.__ouro = 0
        self.__carta = 0
