import os
from application.jogo import Jogo
from application.organizarMesa import OrganizarMesa
from application.teobaldo import Teobaldo
from domain.entities.Jogador import Jogador
from domain.entities.mesa import Mesa
from time import sleep as esperar

class CoresTerminal:
    RESET = '\033[0m'
    NEGRITO = '\033[1m'
    ITALICO = '\033[3m'
    SUBLINHADO = '\033[4m'
    INVERSO = '\033[7m'

    PRETO = '\033[30m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'

    FUNDO_PRETO = '\033[40m'
    FUNDO_VERMELHO = '\033[41m'
    FUNDO_VERDE = '\033[42m'
    FUNDO_AMARELO = '\033[43m'
    FUNDO_AZUL = '\033[44m'
    FUNDO_MAGENTA = '\033[45m'
    FUNDO_CIANO = '\033[46m'
    FUNDO_BRANCO = '\033[47m'
    
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
        
        resposta_menu = input(self.CIANO+"> ").strip().lower()
        
        while resposta_menu not in self.menu_list:
            print(self.VERMELHO+"escolha uma opção válida")
            resposta_menu = input(self.CIANO+"> ").strip().lower()
            
        if resposta_menu == 'iniciar':
            self.iniciar()
        elif resposta_menu == 'pontuação':
            self.pontuacao()
        else:
            self.sair()
        
    def tituloPrincipal(self):
        print(self.AZUL+"""
    ╔╗╔╗╔╗╔╗╔╗╔╗
    ╠─╚╗║─║║╠╝╠║
    ╚╝╚╝╚╝╚╝╩─╩╩
        """+self.RESET)

    def iniciar(self):
        self.limparTela()    
        jogo = Jogo()
        jogo.adicionarJogador(Teobaldo(nome='Teobaldo'))
        jogo.adicionarJogador(Jogador(nome=self.criarJogador()))
        jogo.mesa.iniciarRodada()
        jogo.mesa.rodada.quemCarteia(anterior=None, jogadores=jogo.jogadores)
        
        self.exibirJogador(jogo.jogadores[0])
        self.mesa(jogo.mesa)
        self.exibirJogador(jogo.jogadores[1])
    
    def exibirJogador(self, jogador: Jogador, mensagem="..."):
        """
        Mostrar jogador
        """
        avatar = f"""
{self.AMARELO}-----------------------------------------------
{self.AMARELO}───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄─── {self.MAGENTA}Jogador: {self.CIANO}{jogador}
{self.AMARELO}───█▒▒░░░░░░░░░▒▒█─── {self.MAGENTA}Pontos: {self.CIANO}{jogador.pontuacao}{self.MAGENTA}
{self.AMARELO}────█░░█░░░░░█░░█──── {self.MAGENTA}_________________________
{self.AMARELO}─▄▄──█░░░▀█▀░░░█──▄▄─ {self.MAGENTA}Monte: {self.CIANO}{jogador.monte}{self.MAGENTA}
{self.AMARELO}█░░█─▀▄░░░░░░░▄▀─█░░█ {self.MAGENTA}Escopa: {self.CIANO}{jogador.escopa}{self.MAGENTA}
{self.AMARELO}-----------------------------------------------
"""
        print(avatar)
        print(f"{self.MAGENTA}Mensagem:{self.CIANO} {mensagem}{self.RESET}")
        self.desenharLinha(self.MAGENTA,'*',40)
    
    def exibirCarta(self, cartas: list):
        
        mesaArrumada = OrganizarMesa()
        resultado = mesaArrumada.gerar(cartas)
        for linhas in resultado:
            for linha in linhas.values():
                print()
                for carta in linha:
                    
                    naipe = carta.naipe.nome
                    naipe = naipe.upper()
                    
                    if naipe[0] in "CO":
                        print(f"\t{self.FUNDO_VERMELHO}|{carta.id}{naipe[0]}|{self.RESET}", end="")
                    else:
                        print(f"\t{self.FUNDO_CIANO}|{carta.id}{naipe[0]}|{self.RESET}", end="")     
      
        print()
    def pontuacao(self):
        pass
    
    def criarJogador(self):
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
    
    # --------- COMPONENTES VISUAIS-----------
    def limparTela(self):
        """Limpar terminal"""
        os.system("clear")
        
    def sair(self):
        self.limparTela()
        print("saindo...")
        self.desenharLinha(self.MAGENTA,'*',20)
        esperar(1)
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
        
    
    
    def mesa(self, mesa: Mesa):
        """
        Mostrar mesa
        """
        self.desenharLinha(self.VERDE,'-',40)
        self.exibirCarta(mesa.rodada.baralho.cartas)
        self.desenharLinha(self.VERDE,'-',40)
    
    
        
    