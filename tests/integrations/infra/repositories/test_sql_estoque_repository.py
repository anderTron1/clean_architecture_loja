import pytest

from src.infra.repositories.sql_estoque_repository import SQLEstoqueRepository
from src.infra.repositories.sql_produto_repository import SQLProdutoRepository

from src.domain.entities.estoque import Estoque
from src.domain.entities.produto import Produto

def test_sql_repository_buscar_por_produto(session):
    repo_prod = SQLProdutoRepository()
    produto = Produto(nome="Mouse", preco=150.55)
    produto_salvo = repo_prod.salvar(produto)  
    repo_est = SQLEstoqueRepository()
    repo_est.salvar(Estoque(produto=produto_salvo, produto_id=produto_salvo.id, quantidade=0))

    estoque = repo_est.buscar_por_produto(produto_salvo.id)

    #assert estoque is not None
    assert estoque.produto.id == produto_salvo.id
    assert estoque.produto.nome == produto_salvo.nome
    assert estoque.quantidade == 0
    assert estoque.produto_id == produto_salvo.id

def test_sql_repository_buscar_por_produto_inexistente(session):
    repo_est = SQLEstoqueRepository()
    estoque = repo_est.buscar_por_produto(123)

    #assert estoque is not None
    assert estoque is  None

def test_sql_estoque_adicionar(session):
    repo_prod = SQLProdutoRepository()
    produto = Produto(nome="Mouse", preco=150.55)
    produto_salvo = repo_prod.salvar(produto)  
    repo_est = SQLEstoqueRepository()
    repo_est.salvar(Estoque(produto=produto_salvo, produto_id=produto_salvo.id, quantidade=0))

    estoque = repo_est.adicionar(produto_id=produto_salvo.id, quantidade=20)

    assert estoque.produto_id == produto_salvo.id
    assert estoque.quantidade == 20


def test_sql_estoque_adicionar_produto_id_inexistente(session):
    repo_est = SQLEstoqueRepository()
    estoque = repo_est.adicionar(produto_id=1234, quantidade=20)

    assert estoque is None

def test_sql_estoque_baixar(session):
    repo_prod = SQLProdutoRepository()
    produto = Produto(nome="Mouse", preco=150.55)
    produto_salvo = repo_prod.salvar(produto)  
    repo_est = SQLEstoqueRepository()
    repo_est.salvar(Estoque(produto=produto_salvo, produto_id=produto_salvo.id, quantidade=10))

    estoque = repo_est.baixar(produto_id=produto_salvo.id, quantidade=2)

    assert estoque.produto_id == produto_salvo.id
    assert estoque.quantidade == 8

def test_sql_estoque_baixar_inexistente(session): 
    repo_est = SQLEstoqueRepository()
    estoque = repo_est.baixar(produto_id=122, quantidade=2)

    assert estoque is None