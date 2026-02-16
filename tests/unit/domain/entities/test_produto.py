import pytest

from src.domain.entities.produto import Produto
from src.domain.exceptions.produto_exceptions import ProdutoInvalidoException

def test_produto():
    produto = Produto(nome="Teclado", preco=120.15)

    produto.nome = "teclado gamer"
    produto.preco = 120.15

    assert produto.nome == "teclado gamer"
    assert produto.preco == 120.15

def test_produto_nome_invalido():
    produto = Produto(nome="Teclado", preco=120.15)

    with pytest.raises(ProdutoInvalidoException):
        produto.nome = None

def test_produto_preco_invalido():
    produto = Produto(nome="Teclado", preco=120.15)

    with pytest.raises(ProdutoInvalidoException):
        produto.preco = -10

def test_produto_editar():
    produto = Produto(nome="Teclado", preco=120.15)

    produto.editar(nome="Teclado Gamer", preco=120)

    assert produto.nome == "Teclado Gamer"
    assert produto.preco == 120
 