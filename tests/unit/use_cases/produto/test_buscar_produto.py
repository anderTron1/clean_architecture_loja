import pytest

from src.use_cases.produto.buscar_produto import BuscarProdutoUseCase
from src.domain.produto import Produto

class FakeProdutoRepo:
    def __init__(self):
        self.produtos = {
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=250.00),
        }
    
    def buscar(self, produto_id):
        return self.produtos.get(produto_id)

def test_buscar_produto_existente():
    repo = FakeProdutoRepo()
    use_case = BuscarProdutoUseCase(repo)

    resultados = use_case.execute(1)

    assert resultados.id == 1
    assert resultados.nome == "Mouse"
    assert resultados.preco == 150