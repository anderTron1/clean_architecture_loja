from flask import jsonify


class ProdutoPresenter:
    """Presenter para serialização de Produto DTOs"""
    
    @staticmethod
    def apresentar_produto(produto_output_dto):
        """Converte ProdutoOutputDTO em JSON"""
        return {
            "id": produto_output_dto.id,
            "nome": produto_output_dto.nome,
            "preco": produto_output_dto.preco
        }
    
    @staticmethod
    def apresentar_lista_produtos(lista_output_dto):
        """Converte ListarProdutosOutputDTO em JSON"""
        return {
            "total": lista_output_dto.total,
            "produtos": [
                ProdutoPresenter.apresentar_produto(p) for p in lista_output_dto.produtos
            ]
        }
    
    @staticmethod
    def apresentar_erro(mensagem: str, status_code: int = 400):
        """Formata resposta de erro"""
        return jsonify({"erro": mensagem}), status_code
