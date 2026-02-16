import pytest

from src.domain.entities.produto import Produto

from src.use_cases.produto.excluir_produto import ExcluirProdutoUseCase

from src.domain.exceptions.produto_exceptions import ProdutoNaoEncontradoException

class FakeProduto:
    def __init__(self):
        self.produtos ={
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=240)
        }
    
    def buscar(self, id):
        resultado = self.produtos.get(id)
        if not resultado:
            return None

        return resultado
    
    def excluir(self, id):
        del self.produtos[id]

def test_excluir_produto():
    repo = FakeProduto()
    
    use_case =  ExcluirProdutoUseCase(repo)
    produto = use_case.execute(id=1)


def test_excluir_produto_inexistente():
    repo = FakeProduto()
    
    use_case =  ExcluirProdutoUseCase(repo)
    with pytest.raises(ProdutoNaoEncontradoException):
        produto = use_case.execute(id=12312)