import pytest
from src.domain.entities.produto import Produto

from src.use_cases.produto.salvar_produto import SalvarProdutoUseCase
from src.use_cases.produto.dtos import CadastrarProdutoDTO, ProdutoOutputDTO

from src.use_cases.produto.editar_produto import EditarProdutoUseCase
from src.use_cases.produto.dtos import EditarProdutoDTO, ProdutoOutputDTO

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

    
    def salvar(self, produto):
        produto_edit = self.produtos.get(produto.id)
        if produto.nome is not None:
            produto_edit.nome = produto.nome
        
        if produto.preco is not None:
            produto_edit.preco = produto.preco
        return produto_edit

def test_editar_produto():
    repo = FakeProduto()
    novo_produto = Produto(id=1, nome="Monitor", preco=231.22)

    use_case = EditarProdutoUseCase(repo)
    produto = use_case.execute(novo_produto)

    assert produto.nome == "Monitor"
    assert produto.preco == 231.22

def test_editar_produto():
    repo = FakeProduto()
    novo_produto = Produto(id=234, nome="Monitor", preco=231.22)

    use_case = EditarProdutoUseCase(repo)

    with pytest.raises(ProdutoNaoEncontradoException):
        produto = use_case.execute(novo_produto)
