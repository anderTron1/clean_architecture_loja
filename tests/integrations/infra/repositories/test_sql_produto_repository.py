
import pytest 

from src.infra.repositories.sql_produto_repository import SQLProdutoRepository

from src.domain.entities.produto import Produto

def test_sql_repository_salvar(session):
    repo = SQLProdutoRepository()
    produto = Produto(nome="Mouse", preco=150.55)
    resultado = repo.salvar(produto)

    assert resultado.id is not None

def test_sql_repository_buscar(session):
    repo = SQLProdutoRepository()
    produto = Produto(nome="Mouse", preco=150.55)
    resultado = repo.salvar(produto)

    buscar_produto = repo.buscar(id=resultado.id)

    assert resultado.nome == "Mouse"
    assert resultado.preco == 150.55

def test_sql_repository_buscar_inexistente(session):
    repo = SQLProdutoRepository()
    buscar_produto = repo.buscar(id=12)

    assert buscar_produto is None

def test_sql_repository_excluir(session):
    repo = SQLProdutoRepository()
    produto = Produto(nome="Mouse", preco=150.55)
    resultado = repo.salvar(produto)

    repo.excluir(resultado.id)

def test_sql_repository_excluir_inexistente(session):
    repo = SQLProdutoRepository()
    result = repo.excluir(123123)

    assert result is None

def test_sql_repository_listar(session):
    repo = SQLProdutoRepository()
    resultado = repo.salvar(Produto(nome="Mouse", preco=150.55))
    resultado = repo.salvar(Produto(nome="Teclado", preco=250.55))

    resultado = repo.listar()

    assert len(resultado) == 2
    assert resultado[0].nome == "Mouse"
    assert resultado[1].nome == "Teclado"

def test_sql_repository_listar(session):
    repo = SQLProdutoRepository()
    resultado = repo.listar()

    assert resultado == []