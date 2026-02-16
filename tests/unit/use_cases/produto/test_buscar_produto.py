import pytest

from src.domain.entities.produto import Produto

from src.use_cases.produto.buscar_produto import BuscarProdutoUseCase
from src.use_cases.produto.dtos import ProdutoOutputDTO

from src.domain.exceptions.produto_exceptions import ProdutoNaoEncontradoException

class FakeProduto:
    def __init__(self):
        self.produtos ={
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=240)
        }
    
    def buscar(self, id):
        resultado = self.produtos.get(id)

        return resultado

def test_buscar_produto():
    repo = FakeProduto()
    
    use_case =  BuscarProdutoUseCase(repo)
    produto = use_case.execute(id=1)
    
    assert produto.nome == "Mouse"
    assert produto.preco ==  150

def test_buscar_produto_inexistente():
    repo = FakeProduto()
    
    use_case =  BuscarProdutoUseCase(repo)

    with pytest.raises(ProdutoNaoEncontradoException):
        produto = use_case.execute(id=123123)