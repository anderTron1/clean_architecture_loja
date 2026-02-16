from src.domain.entities.produto import Produto

from src.use_cases.produto.salvar_produto import SalvarProdutoUseCase
from src.use_cases.produto.dtos import CadastrarProdutoDTO, ProdutoOutputDTO

class FakeProduto:
    def __init__(self):
        self.produtos ={
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=240)
        }
    
    def salvar(self, produto):
        self.produtos[3] = produto
        return self.produtos[3]

def test_salvar_produto():
    repo = FakeProduto()
    novo_produto = Produto(nome="Monitor", preco=231.22)

    use_case = SalvarProdutoUseCase(repo)
    produto = use_case.execute(novo_produto)

    assert produto.nome == "Monitor"
    assert produto.preco == 231.22