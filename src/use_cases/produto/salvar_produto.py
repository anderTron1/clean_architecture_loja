from src.domain.entities.produto import Produto
from src.domain.entities.estoque import Estoque
from src.use_cases.produto.dtos import CadastrarProdutoDTO, ProdutoOutputDTO

from sqlalchemy.exc import SQLAlchemyError

class SalvarProdutoUseCase:
    def __init__(self, produto_repo, estoque_repo):
        self.produto_repo = produto_repo
        self.estoque_repo = estoque_repo
    
    def execute(self, produtoDTO: CadastrarProdutoDTO) -> ProdutoOutputDTO:
        produto = Produto(nome=produtoDTO.nome, preco=produtoDTO.preco)
        
        produto_salvo = self.produto_repo.salvar(produto)
        
        # Cria um estoque inicial vinculado ao produto cadastrado
        self.estoque_repo.salvar(Estoque(produto=produto_salvo, produto_id=produto_salvo.id, quantidade=0))

        return ProdutoOutputDTO(
            id=produto_salvo.id,
            nome=produto_salvo.nome,
            preco=produto_salvo.preco
        )