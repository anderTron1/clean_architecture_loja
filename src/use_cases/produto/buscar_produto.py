from src.domain.entities.produto import Produto
from src.use_cases.produto.dtos import ProdutoOutputDTO

from src.domain.exceptions.produto_exceptions import ProdutoNaoEncontradoException

class BuscarProdutoUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo
    
    def execute(self, id: int) -> ProdutoOutputDTO:
        produto = self.produto_repo.buscar(id)

        if not produto:
            raise ProdutoNaoEncontradoException("Produto não encontrado")


        return ProdutoOutputDTO(
            id=produto.id,
            nome=produto.nome,
            preco=produto.preco
        )