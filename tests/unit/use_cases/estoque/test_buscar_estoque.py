import pytest
from src.domain.entities.produto import Produto
from src.domain.entities.estoque import Estoque

from src.use_cases.estoque.buscar_estoque import BuscarEstoqueUseCase

from src.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoException
class FakeProduto:
    def __init__(self):
        self.produtos ={
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=240)
        }
    
class FakeEstoque:
    def __init__(self):
        produto = FakeProduto()
        self.estoque = {
            1: Estoque(id=1, produto=produto.produtos[1], produto_id=1, quantidade=2),
            2: Estoque(id=2, produto=produto.produtos[2], produto_id=2, quantidade=20)
        }
    
    def buscar_por_produto(self, produto_id):
        resultado = next(
            (e for e in self.estoque.values() if e.produto_id == produto_id),
            None
        )
        return resultado

def test_buscar_estoque():
    repo = FakeEstoque()

    use_case = BuscarEstoqueUseCase(repo)
    estoque = use_case.execute(produto_id=1)

    assert estoque.id == 1
    assert estoque.quantidade == 2
    assert estoque.produto.id == 1

def test_buscar_estoque_invalido():
    repo = FakeEstoque()

    use_case = BuscarEstoqueUseCase(repo)
    with pytest.raises(EstoqueNaoEncontradoException):
        use_case.execute(produto_id=12121)