import pytest
from src.domain.entities.produto import Produto
from src.domain.entities.estoque import Estoque

from src.use_cases.estoque.baixar_estoque import BaixarEstoqueUseCase
from src.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoException, EstoqueInvalidoException

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
            1: Estoque(id=1, produto=produto.produtos[1], produto_id=1, quantidade=20),
            2: Estoque(id=2, produto=produto.produtos[2], produto_id=2, quantidade=20)
        }
    
    def baixar(self, produto_id, quantidade):
        resultado = next(
            (e for e in self.estoque.values() if e.produto_id == produto_id),
            None
        )

        if resultado is not None:
            estoque = Estoque(
                produto = None,
                produto_id= resultado.produto_id,
                quantidade= resultado.quantidade,
                id=resultado.id
            )
            estoque.baixar(quantidade)
            return estoque
        return resultado

def test_adicionar_estoque():
    repo = FakeEstoque()

    use_case = BaixarEstoqueUseCase(repo)
    estoque = use_case.execute(produto_id=1, quantidade=5)

def test_baixar_estoque_invalido():
    repo = FakeEstoque()

    use_case = BaixarEstoqueUseCase(repo)
    with pytest.raises(EstoqueNaoEncontradoException):
        estoque = use_case.execute(produto_id=123, quantidade=10)

def test_baixar_estoque_invalido_da_entitade_estoque():
    repo = FakeEstoque()

    use_case = BaixarEstoqueUseCase(repo)
    with pytest.raises(EstoqueInvalidoException):
        estoque = use_case.execute(produto_id=1, quantidade=-10)