from src.domain.produto import Produto

class ExcluirProdutoUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo
    
    def execute(self, id) -> None:
        self.produto_repo.excluir(id)
        