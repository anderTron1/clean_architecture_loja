import pytest

from src.use_cases.produto.buscar_produto import BuscarProdutoUseCase
from src.domain.produto import Produto

from src.domain.exceptions import ProdutoNaoEncontradoException, ProdutoInvalidoException

class FakeProdutoRepo:
    def __init__(self):
        self.produtos = {
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=250.00),
        }
    
    def editar(self, produto):
        fakeProduto = self.produtos.get(produto.id)
        
        if not fakeProduto:
            raise ProdutoNaoEncontradoException("Produto não encontrado!")

        campos = ["nome", "preco"]

        alterou = False
        for campo in campos:
            valor = getattr(produto, campo)
            if valor is not None and valor != "":
                setattr(fakeProduto, campo, valor)
                alterou = True
        if not alterou:
            raise ProdutoInvalidoException("Nenhum campo foi atualizado")

        return Produto(id=fakeProduto.id, nome=fakeProduto.nome, preco=fakeProduto.preco)
        
def test_editar_produto_existente():
    repo = FakeProdutoRepo()

    produto = Produto(id=1, nome="Mouse Gamer", preco=188)

    resultados = repo.editar(produto)

    assert resultados.id == 1
    assert resultados.nome == "Mouse Gamer"
    assert resultados.preco == 188

def test_editar_produto_inexistente():
    repo = FakeProdutoRepo()
    produto = Produto(id=123, nome="Mouse", preco=150)

    with pytest.raises(ProdutoNaoEncontradoException):
        repo.editar(produto)

def test_editar_produto_sem_alteracoes():
    repo = FakeProdutoRepo()

    produto = Produto(id=1, nome="", preco=None)

    with pytest.raises(ProdutoInvalidoException):
        repo.editar(produto)