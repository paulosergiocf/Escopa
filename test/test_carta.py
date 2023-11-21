import pytest
from domain.entities.cartas import Carta
from domain.entities.cartas import Naipe

# Testes para a classe Naipe
def test_naipe_criacao():
    naipe = Naipe(id=1, nome="Copas")
    assert naipe.id == 1
    assert naipe.nome == "Copas"

def test_naipe_str():
    naipe = Naipe(id=1, nome="Copas")
    assert str(naipe) == "Copas"

# Testes para a classe Carta
def test_carta_criacao():
    naipe = Naipe(id=1, nome="Copas")
    carta = Carta(id=2, naipe=naipe)
    assert carta.id == 2
    assert carta.naipe == naipe

def test_carta_str():
    naipe = Naipe(id=1, nome="Copas")
    carta = Carta(id=2, naipe=naipe)
    assert str(carta) == "2 | Copas"
