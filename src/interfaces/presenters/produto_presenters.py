from flask import jsonify

class ProdutoPresenters:
    """Presenter para serialização de Produto DTOs"""
    @staticmethod
    def apresentar_produto(produto_output_dto):
        return {
            "id": produto_output_dto.id,
            "nome": produto_output_dto.nome,
            "preco": produto_output_dto.preco
        }
    @staticmethod
    def apresentar_lista_produtos(produtos_output_dto):
        return [
            {
                "item": item+1,
                "produto": ProdutoPresenters.apresentar_produto(p)
            } for item, p in enumerate(produtos_output_dto)
        ]
    @staticmethod
    def apresentar_erro(mensagem: str, status_code: int = 400):
        return jsonify({"erro": mensagem}), status_code

    @staticmethod
    def apresentar_mensagem(mensagem: str):
        return {"mensagem": mensagem}