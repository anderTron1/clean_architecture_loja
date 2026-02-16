from src.domain.entities.produto import Produto
from src.use_cases.produto.dtos import EditarProdutoDTO, ProdutoOutputDTO

from src.domain.exceptions.produto_exceptions import ProdutoNaoEncontradoException

class EditarProdutoUseCase:
    def __init__(self, produto_repo) -> None:
        self.produto_repo = produto_repo
    
    def execute(self, produto_dto: EditarProdutoDTO) -> ProdutoOutputDTO:

        produto_existente = self.produto_repo.buscar(produto_dto.id)

        if not produto_existente:
            raise ProdutoNaoEncontradoException("Produto não encontrado")

        produto_existente.editar(
            nome=produto_dto.nome,
            preco=produto_dto.preco
        )

        produto_editado = self.produto_repo.salvar(produto_existente)

        return ProdutoOutputDTO(
            id=produto_editado.id,
            nome=produto_editado.nome,
            preco=produto_editado.preco
        )