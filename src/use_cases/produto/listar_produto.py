from src.domain.produto import Produto
from src.use_cases.produto.dtos import ListarProdutosOutputDTO, ProdutoOutputDTO


class ListarProdutosUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo
    
    def execute(self) -> ListarProdutosOutputDTO:
        produtos = self.produto_repo.listar()
        
        produtos_output = [
            ProdutoOutputDTO(
                id=p.id,
                nome=p.nome,
                preco=p.preco
            ) for p in produtos
        ]
        
        return ListarProdutosOutputDTO(
            produtos=produtos_output,
            total=len(produtos_output)
        )
