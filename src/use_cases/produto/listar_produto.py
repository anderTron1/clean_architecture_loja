from src.domain.entities.produto import Produto
from src.use_cases.produto.dtos import ProdutoOutputDTO
from typing import List

class ListarProdutosUseCases:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo

    def execute(self) -> List[ProdutoOutputDTO]:
        produtos = self.produto_repo.listar()

        return [
            ProdutoOutputDTO(id=p.id, nome=p.nome, preco=p.preco) 
            for p in produtos
        ]