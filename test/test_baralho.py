import pytest
from application.baralho import Baralho
from domain.entities.cartas import Carta, Naipe

def test_iniciar_baralho():
    baralho = Baralho()
    assert len(baralho.cartas) == 40
    assert baralho.qntCartas == 40

def test_embaralhar_baralho():
    baralho = Baralho()
    cartas_antes = baralho.cartas.copy()

    baralho.embaralhar()

    assert cartas_antes != baralho.cartas

def test_comprar_carta():
    baralho = Baralho()
    cartas_antes = baralho.cartas.copy()
    qnt_cartas_antes = baralho.qntCartas

    carta_comprada = baralho.comprar()

    assert carta_comprada in cartas_antes
    assert baralho.qntCartas == qnt_cartas_antes - 1

def test_comprar_carta_de_baralho_vazio():
    baralho = Baralho()

    # Esvazia o baralho
    while baralho.qntCartas > 0:
        baralho.comprar()

    carta_comprada = baralho.comprar()

    assert carta_comprada == []
    assert baralho.qntCartas == 0

def test_verificar_situacao_baralho():
    baralho = Baralho()

    assert baralho.qntCartas == 40
    assert baralho._Baralho__situacao is True

    # Esvazia o baralho
    while baralho.qntCartas > 0:
        baralho.comprar()

    assert baralho.qntCartas == 0
    assert baralho._Baralho__situacao is False