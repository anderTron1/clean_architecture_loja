from flask import jsonify

from src.interfaces.presenters.produto_presenters import ProdutoPresenters

class EstoquePresenters:
    """Presenter para serialização de Estoque DTOs"""

    @staticmethod
    def apresentar_estoque(estoque_output_dto):
        return {
            "id": estoque_output_dto.id,
            "produto_id": estoque_output_dto.produto_id,
            "quantidade": estoque_output_dto.quantidade,
            "produto": ProdutoPresenters.apresentar_produto(estoque_output_dto.produto)
               if estoque_output_dto.produto is not None
               else None
        }
    
    @staticmethod
    def apresentar_erro(mensagem: str, status_code: int = 400):
        return jsonify({"erro": mensagem}), status_code