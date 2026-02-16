from src.domain.entities.estoque import Estoque
from src.use_cases.estoque.dtos import EstoqueOutputDTO

from src.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoException

class BuscarEstoqueUseCase:
    def __init__(self, estoque_repo) -> None:
        self.estoque_repo = estoque_repo

    def execute(self, produto_id: int) -> EstoqueOutputDTO:
        estoque = self.estoque_repo.buscar_por_produto(produto_id)

        if not estoque:
            raise EstoqueNaoEncontradoException("Estoque não encontrado")
        
        return EstoqueOutputDTO(
            id=estoque.id,
            produto_id = estoque.produto_id,
            quantidade = estoque.quantidade,
            produto= estoque.produto
        )