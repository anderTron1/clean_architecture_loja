import pytest

from src.domain.produto import Produto
from src.use_cases.produto.excluir_produto import ExcluirProdutoUseCase
from src.domain.exceptions import ProdutoNaoEncontradoException

class FakeProduto:
    def __init__(self):
        self.produtos = {
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=250.00),
        }
    
    def excluir(self, produto_id):
        fakeProduto = self.produtos.get(produto_id)

        if not fakeProduto:
            raise ProdutoNaoEncontradoException("Produto não encontrado!")

        del self.produtos[produto_id]

def test_excluir_produto_existente():
    repo = FakeProduto()

    use_case = ExcluirProdutoUseCase(repo)
    use_case.execute(1)

    assert 1 not in repo.produtos

def test_excluir_produto_inexistente():
    repo = FakeProduto()

    use_case = ExcluirProdutoUseCase(repo)
    with pytest.raises(ProdutoNaoEncontradoException):
        use_case.execute(9999)