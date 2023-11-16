
class Naipe:
    def __init__(self, id: int, nome):
        self.__id = id
        self.__nome = nome
        
    def __str__(self):
        return f"{self.__nome}"
        
        
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
    
class Cartas:
    def __init__(self, id, naipe: Naipe):
        self.__id = id
        self.__naipe = naipe
        
    def __str__(self):
        return f"{self.__id} | {self.__naipe}"
        
    @property
    def id(self):
        return self.__id
    @property
    def naipe(self):
        return self.__naipe
