import pytest
from src.infra.repositories.sql_produto_repository import SQLProdutoRepository
from src.domain.produto import Produto

from src.domain.exceptions import ProdutoNaoEncontradoException, ProdutoInvalidoException

from src.infra.models.produto_sql import ProdutoSQL
from src.infra.db import db

def test_sql_repository_salvar(session):
    repo = SQLProdutoRepository()

    produto = Produto(nome="Mouse", preco=150)
    resultado = repo.salvar(produto)

    assert resultado.id is not None

def test_sql_repository_editar(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo  = repo.salvar(novo_produto)

    produto = Produto(id=produto_salvo.id, nome="Mouse Gamer", preco=122)
    resultado = repo.editar(produto)

    assert resultado.id == produto_salvo.id
    assert resultado.nome == "Mouse Gamer"
    assert resultado.preco == 122

def test_sql_repository_editar_inexistente(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo = repo.salvar(novo_produto)

    produto = Produto(id=1233, nome="Mouse Gamer", preco=299)

    with pytest.raises(ProdutoNaoEncontradoException):
        repo.editar(produto) 

def test_sql_repository_editar_sem_alteracoes(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo = repo.salvar(novo_produto)

    produto = Produto(id=1, nome="", preco=None)

    with pytest.raises(ProdutoInvalidoException):
        repo.editar(produto)

def test_sql_repository_excluir_existente(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo = repo.salvar(novo_produto)

    repo.excluir(produto_salvo.id)

    produto = db.session.get(ProdutoSQL, produto_salvo.id)

    assert produto is None 

def test_sql_repository_excluir_inexistente(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo = repo.salvar(novo_produto)

    with pytest.raises(ProdutoNaoEncontradoException):
        repo.excluir(2)

def test_sql_repository_buscar(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo = repo.salvar(novo_produto)

    produto = repo.buscar(novo_produto.id)

    assert produto.id == novo_produto.id
    assert produto.nome == "Mouse"
    assert produto.preco == 150

def test_sql_repository_buscar_inexistente(session):
    repo = SQLProdutoRepository()

    novo_produto = Produto(nome="Mouse", preco=150)
    produto_salvo = repo.salvar(novo_produto)

    with pytest.raises(ProdutoNaoEncontradoException):
        produto = repo.buscar(234)

def test_sql_repository_listar(session):
    repo = SQLProdutoRepository()

    repo.salvar(Produto(nome="Mouse", preco=150))
    repo.salvar(Produto(nome="Teclado", preco=250))

    produtos = repo.listar()

    assert len(produtos) == 2