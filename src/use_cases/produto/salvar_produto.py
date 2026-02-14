from src.domain.produto import Produto
from src.use_cases.produto.dtos import CriarProdutoInputDTO, ProdutoOutputDTO


class SalvarProdutoUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo
    
    def execute(self, input_dto: CriarProdutoInputDTO) -> ProdutoOutputDTO:
        produto = Produto(nome=input_dto.nome, preco=input_dto.preco)
        produto_salvo = self.produto_repo.salvar(produto)
        
        return ProdutoOutputDTO(
            id=produto_salvo.id,
            nome=produto_salvo.nome,
            preco=produto_salvo.preco
        )