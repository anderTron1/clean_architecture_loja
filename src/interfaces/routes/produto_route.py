from flask import Blueprint,  request, jsonify

from src.use_cases.produto.dtos import CadastrarProdutoDTO, EditarProdutoDTO
from src.interfaces.presenters.produto_presenters import ProdutoPresenters
from src.domain.exceptions.produto_exceptions import ProdutoInvalidoException, ProdutoNaoEncontradoException

def criar_produto_controller(salvar_produto, editar_produto, buscar_produto, listar_produtos, excluir_produto):
    produto_db = Blueprint("produto", __name__)

    @produto_db.route("/produto", methods=["POST"])
    def salvar():
        try:
            data = request.json
            produto_dto = CadastrarProdutoDTO(
                nome=data["nome"],
                preco=data["preco"]
            )
            produto_salvo = salvar_produto.execute(produto_dto)
            return jsonify(ProdutoPresenters.apresentar_produto(produto_salvo)), 201
        except (ProdutoInvalidoException, KeyError) as e:
            return ProdutoPresenters.apresentar_erro(str(e), 400)
    
    @produto_db.route("/produto/<int:id>", methods=["PUT"])
    def editar(id):
        try:
            data = request.json
            produto_dto = EditarProdutoDTO(
                id=id,
                nome=data.get("nome"),
                preco=data.get("preco")
            )
            produto_editado = editar_produto.execute(produto_dto)
            return jsonify(ProdutoPresenters.apresentar_produto(produto_editado)), 200
        except (ProdutoInvalidoException, ProdutoNaoEncontradoException, KeyError) as e:
            return ProdutoPresenters.apresentar_erro(str(e), 400)

    @produto_db.route("/produto/<int:id>", methods=["GET"])
    def buscar(id):
        try:
            produto = buscar_produto.execute(id)
            return jsonify(ProdutoPresenters.apresentar_produto(produto)), 200
        except (ProdutoNaoEncontradoException, KeyError) as e:
            return ProdutoPresenters.apresentar_erro(str(e), 404)

    @produto_db.route("/produtos", methods=["GET"])
    def listar():
        produtos = listar_produtos.execute()
        return jsonify(ProdutoPresenters.apresentar_lista_produtos(produtos)), 200

    @produto_db.route("/produto/<int:id>", methods=["DELETE"])
    def excluir(id):
        try:
            saida = excluir_produto.execute(id)
            return jsonify(ProdutoPresenters.apresentar_mensagem("Produto excluído com sucesso")), 200
        except ProdutoNaoEncontradoException as e:
            return ProdutoPresenters.apresentar_erro(str(e), 404)

    return produto_db