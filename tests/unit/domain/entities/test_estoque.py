import pytest

from src.domain.entities.estoque import Estoque
from src.domain.exceptions.estoque_exceptions import EstoqueInvalidoException

class FakeProduto:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

def test_quantidade_inicial():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    assert e.quantidade == 10

def test_nao_permite_alterar_quantidade_direta():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    with pytest.raises(EstoqueInvalidoException) as exc:
        e.quantidade = 5

def test_adicionar_quantidade_valida():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    e.adicionar(5)
    assert e.quantidade == 15

def test_adicionar_quantidade_invalida():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    with pytest.raises(EstoqueInvalidoException) as exc:
        e.adicionar(0)

def test_baixar_quantidade_valida():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    e.baixar(4)
    assert e.quantidade == 6

def test_baixar_quantidade_invalida_maior_que_estoque():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    with pytest.raises(EstoqueInvalidoException) as exc:
        e.baixar(20)

def test_baixar_quantidade_invalida_zero():
    p = FakeProduto("Mouse", 1)
    e = Estoque(produto=p, produto_id=p.id, quantidade=10)

    with pytest.raises(EstoqueInvalidoException) as exc:
        e.baixar(0)