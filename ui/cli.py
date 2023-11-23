import os
from application.baralho import Baralho
from application.jogo import Jogo
from application.organizarMesa import OrganizarMesa
from application.teobaldo import Teobaldo
from domain.entities.Jogador import Jogador
from domain.entities.mesa import Mesa
from time import sleep as esperar
from application.regras import Regras
from ui.CoresTerminal import CoresTerminal
from ui.Textos import Textos
    
class TermUI(CoresTerminal):
    def __init__(self):
        super().__init__()
        self.menu_list = ['iniciar', 'pontuações','sair']
    
    def menu(self):
        """
        Menu da aplicação
        """
        self.limparTela()
        self.tituloPrincipal()
        self.desenharLinha(self.BRANCO, '-', tamanho=20)
        
        for item in self.menu_list:
            print(f'{item}')
        try:
            resposta_menu = input(self.CIANO+"> ").strip().lower()
            
            while resposta_menu not in self.menu_list:
                print(self.VERMELHO+"escolha uma opção válida")
                resposta_menu = input(self.CIANO+"> ").strip().lower()
        except KeyboardInterrupt as erro:
            self.sair()
            
        if resposta_menu == 'iniciar':
            self.iniciar()
        elif resposta_menu == 'pontuação':
            self.pontuacao()
        else:
            self.sair()
        
    def tituloPrincipal(self):
        print(self.AZUL+Textos.ESCOPA+self.RESET)

    def iniciar(self):
        self.limparTela() 
           
        jogo = Jogo()
        teo = Teobaldo(nome='Teobaldo')
        jogador2 = Jogador(nome=self.criarJogador())
        jogo.adicionarJogador(teo)
        jogo.adicionarJogador(jogador2)

        mesa = Mesa()
        baralho = Baralho()
        baralho.embaralhar()
        JogadorDaRodada = None
        JogadorDaRodada = Regras.quemCarteia(anterior=JogadorDaRodada, jogadores=jogo.jogadores)
        vira, escopas = Regras.tombar(baralho=baralho)
        
        teo.addCartaMao(baralho.comprar())
        teo.addCartaMao(baralho.comprar())
        teo.addCartaMao(baralho.comprar())
        
        jogador2.addCartaMao(baralho.comprar())
        jogador2.addCartaMao(baralho.comprar())
        jogador2.addCartaMao(baralho.comprar())
        
        if escopas != None:
            for escopa in range(0,escopas):
                JogadorDaRodada.addEscopa()
                mesa.limparMesa()
                vira = None

        self.display(jogo.jogadores ,vira)
        
    def display(self, jogadores: list, mesa: list):
        self.exibirJogador(jogadores[0])
        self.mesa(mesa)
        self.exibirJogador(jogadores[1])
    
    def exibirJogador(self, jogador: Jogador, mensagem="..."):
        """
        Mostrar jogador
        """
        cartas = str()
        for carta in jogador.mao:
            cartas += f" {self.FUNDO_VERMELHO}|{carta.id}{Textos.NAIPES_SOMBOLOS[carta.naipe.nome]}|{self.RESET}"
        
        avatar = f"""
{self.AMARELO}-----------------------------------------------
{self.AMARELO}───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄─── {self.MAGENTA}Jogador: {self.CIANO}{jogador}
{self.AMARELO}───█▒▒░░░░░░░░░▒▒█─── {self.MAGENTA}Pontos: {self.CIANO}{jogador.pontuacao}{self.MAGENTA}
{self.AMARELO}────█░░█░░░░░█░░█──── {self.MAGENTA}_________________________
{self.AMARELO}─▄▄──█░░░▀█▀░░░█──▄▄─ {self.MAGENTA}Monte: {self.CIANO}{jogador.monte}{self.MAGENTA}
{self.AMARELO}█░░█─▀▄░░░░░░░▄▀─█░░█ {self.MAGENTA}Escopa: {self.CIANO}{jogador.escopa}{self.MAGENTA}

{self.AMARELO} Mão: {cartas}
{self.AMARELO}-----------------------------------------------
"""
        print(avatar)    
    def exibirCarta(self, cartas: list):
        
        mesaArrumada = OrganizarMesa()
        resultado = mesaArrumada.gerar(cartas)
        for linhas in resultado:
            for linha in linhas.values():
                print('\n\n')
                for carta in linha:
                    
                    naipe = carta.naipe.nome
                   
                    
                    if naipe[0] in "CO":
                        print(f"\t{self.FUNDO_VERMELHO}|{carta.id}{Textos.NAIPES_SOMBOLOS[naipe]}|{self.RESET}", end="")
                    else:
                        print(f"\t{self.FUNDO_CIANO}|{carta.id}{Textos.NAIPES_SOMBOLOS[naipe]}|{self.RESET}", end="")     
      
                print('\n\n\n')
    def pontuacao(self):
        pass
    
    def criarJogador(self):
        try:
            self.desenharLinha(self.CIANO, '*', 40)
            print("""
            ─▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄
            █░░░█░░░░░░░░░░▄▄░██░█
            █░▀▀█▀▀░▄▀░▄▀░░▀▀░▄▄░█
            █░░░▀░░░▄▄▄▄▄░░██░▀▀░█
            ─▀▄▄▄▄▄▀─────▀▄▄▄▄▄▄▀
                
                """)
            nomeJogador = input(self.AZUL+"digite seu nome. Ex:'felisberto'> ").strip().lower()
            
            while len(nomeJogador) < 3 or len(nomeJogador) > 12:
                print(self.VERMELHO+"o nome deve ter mais de 3 caracteres e menos que 12")
                nomeJogador = input(self.AZUL+"> ").strip().lower()
                
            self.desenharLinha(self.CIANO, '*', 40)
            self.limparTela() 
            return nomeJogador
        except KeyboardInterrupt as erro:
            self.sair()
    
    # --------- COMPONENTES VISUAIS-----------
    def limparTela(self):
        """Limpar terminal"""
        os.system("clear")
        
    def sair(self):
        """Fechar o jogo"""
        self.limparTela()
        self.desenharLinha(self.MAGENTA,'-',20)
        print("saindo...")
        self.desenharLinha(self.MAGENTA,'-',20)
        esperar(2)
        self.limparTela()
        quit()
                
    def desenharLinha(self,  cor: str, simbolo: str='-', tamanho: int=20):
        """_summary_
        Args:
            cor (str): passar cor unicode
            simbolo (str, optional): simbolo para desenhar linha. Defaults to '-'.
            tamanho (int, optional): tamanho da multiplicação do simbolo. Defaults to 20.
        """
        print(cor+'', end='')
        print(simbolo * tamanho, end='')
        print(''+self.RESET)
    
    def mesa(self, vira: list):
        """
        Mostrar mesa
        """
        self.desenharLinha(self.VERDE,'=',50)
        if vira != None:    
            self.exibirCarta(vira)
        else:
            print("\n\n\n")
        self.desenharLinha(self.VERDE,'=',50)

        
    
        
    