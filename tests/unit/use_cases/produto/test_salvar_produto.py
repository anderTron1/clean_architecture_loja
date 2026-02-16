from src.domain.entities.produto import Produto
from src.domain.entities.estoque import Estoque

from src.use_cases.produto.salvar_produto import SalvarProdutoUseCase
from src.use_cases.produto.dtos import CadastrarProdutoDTO, ProdutoOutputDTO

class FakeProduto:
    def __init__(self):
        self.produtos ={
            1: Produto(id=1, nome="Mouse", preco=150),
            2: Produto(id=2, nome="Teclado", preco=240)
        }
    
    def salvar(self, produto):
        produto.id = 3
        self.produtos[3] = produto
        return self.produtos[3]

class FakeEstoque:
    def __init__(self):
        self.estoque = {}
    
    def salvar(self, estoque):
        self.estoque[1] = Estoque(
            produto=estoque.produto,
            produto_id=estoque.produto_id,
            quantidade=estoque.quantidade
        )
        return self.estoque[1]
def test_salvar_produto():
    repo_prod = FakeProduto()
    repo_est = FakeEstoque()

    novo_produto = Produto(nome="Monitor", preco=231.22)

    use_case = SalvarProdutoUseCase(repo_prod, repo_est)
    produto = use_case.execute(novo_produto)

    assert produto.nome == "Monitor"
    assert produto.preco == 231.22