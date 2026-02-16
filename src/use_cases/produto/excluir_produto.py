from src.domain.entities.produto import Produto
from src.domain.exceptions.produto_exceptions import ProdutoNaoEncontradoException

class ExcluirProdutoUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo

    def execute(self, id: int) -> None:
        produto = self.produto_repo.buscar(id)
        
        if not produto:
            raise ProdutoNaoEncontradoException("Produto não encontrado")
        
        self.produto_repo.excluir(produto.id)