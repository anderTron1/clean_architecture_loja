from src.domain.entities.produto import Produto

from src.use_cases.produto.dtos import CadastrarProdutoDTO, ProdutoOutputDTO

class SalvarProdutoUseCase:
    def __init__(self, produto_repo):
        self.produto_repo = produto_repo
    
    def execute(self, produtoDTO: CadastrarProdutoDTO) -> ProdutoOutputDTO:
        produto = Produto(nome=produtoDTO.nome, preco=produtoDTO.preco)
        produto_salvo = self.produto_repo.salvar(produto)

        return ProdutoOutputDTO(
            id=produto_salvo.id,
            nome=produto_salvo.nome,
            preco=produto_salvo.preco
        )