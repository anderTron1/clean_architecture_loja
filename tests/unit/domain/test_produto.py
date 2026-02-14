# tests/unit/test_produto.py
import pytest
from src.domain.produto import Produto

def test_criar_produto_valido():
    produto = Produto("Mouse", 150.11)

    assert produto.nome == "Mouse"
    assert produto.preco == 150.11

def test_setter_nome_invalido():
    produto = Produto("Mouse", 10)

    with pytest.raises(Exception):
        produto.nome = ""

def test_setter_nome_valido():
    produto = Produto("Mouse", 10)
    produto.nome = "Teclado"
    assert produto.nome == "Teclado"

def test_setter_preco_invalido():
    produto = Produto("Mouse", 10)

    with pytest.raises(Exception):
        produto.preco = 0

def test_setter_preco_valido():
    produto = Produto("Mouse", 10)

    produto.preco = 15.5
    assert produto.preco == 15.5