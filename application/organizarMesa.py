
class OrganizarMesa():
    def __init__(self):
        self.organizacao= list()
        self.diagramacao = dict()
        self.contador = 1
        self.linha = 1

    def gerar(self, lista):
        for objeto in lista:
            if self.contador == 1:
                self.diagramacao[f"linha{self.linha}"] = [objeto]
                self.contador +=1
            elif self.contador == 2:
                self.diagramacao[f"linha{self.linha}"].append(objeto)
                self.contador +=1
            elif self.contador == 3:
                self.diagramacao[f"linha{self.linha}"].append(objeto)
                self.linha += 1
                self.contador = 1 

        self.organizacao.append(self.diagramacao)

        return self.organizacao