from src.domain.produto import Produto
from src.use_cases.produto.dtos import AtualizarProdutoInputDTO, ProdutoOutputDTO

class EditarProdutoUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo
    
    def execute(self, input_dto: AtualizarProdutoInputDTO) -> ProdutoOutputDTO:
        produto = Produto(id=input_dto.id, nome=input_dto.nome, preco=input_dto.preco)
        produto_editado = self.produto_repo.editar(produto)
        
        return ProdutoOutputDTO(
            id=produto_editado.id,
            nome=produto_editado.nome,
            preco=produto_editado.preco
        )