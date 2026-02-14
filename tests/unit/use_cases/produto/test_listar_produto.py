import pytest

from src.domain.produto import Produto
from src.use_cases.produto.listar_produto import ListarProdutosUseCase

class FakeProduto:
    def __init__(self):
        self.produtos = {
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=250.00) 
        }

    def listar(self):
        return list(self.produtos.values())

def test_listar_produtos_existentes():
    repo = FakeProduto()

    use_case = ListarProdutosUseCase(repo)
    resultado = use_case.execute()

    assert len(resultado.produtos) == 2
    assert resultado.produtos[0].nome == "Mouse"
    assert resultado.produtos[1].nome == "Teclado"