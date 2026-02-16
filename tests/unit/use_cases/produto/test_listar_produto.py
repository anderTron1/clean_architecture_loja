import pytest

from src.domain.entities.produto import Produto

from src.use_cases.produto.listar_produto import ListarProdutosUseCases

class FakeProduto:
    def __init__(self):
        self.produtos ={
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=240)
        }
    
    def listar(self):
        return list(self.produtos.values())

def test_listar_produtos():
    repo = FakeProduto()

    use_case = ListarProdutosUseCases(repo)
    resultados = use_case.execute()

    assert len(resultados) == 2
    assert resultados[0].nome == "Mouse"
    assert resultados[1].nome == "Teclado"