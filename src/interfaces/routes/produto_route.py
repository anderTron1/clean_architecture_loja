from flask import Blueprint, request, jsonify

from src.use_cases.produto.dtos import CriarProdutoInputDTO, AtualizarProdutoInputDTO
from src.interfaces.presenters.produto_presenter import ProdutoPresenter
from src.domain.exceptions import ProdutoNaoEncontradoException, ProdutoInvalidoException


def criar_produto_controller(salvar_produto, editar_produto, excluir_produto, buscar_produto, listar_produto):
    produto_db = Blueprint("produto", __name__)

    @produto_db.route("/produto", methods=["POST"])
    def salvar():
        try:
            data = request.json
            input_dto = CriarProdutoInputDTO(
                nome=data["nome"],
                preco=data["preco"]
            )
            produto_output = salvar_produto.execute(input_dto)
            return jsonify(ProdutoPresenter.apresentar_produto(produto_output)), 201
        except (ProdutoInvalidoException, KeyError) as e:
            return ProdutoPresenter.apresentar_erro(str(e), 400)
    
    @produto_db.route("/produto/<int:id>", methods=["PUT"])
    def editar(id):
        try:
            data = request.json
            input_dto = AtualizarProdutoInputDTO(
                id=id,
                nome=data.get("nome"),
                preco=data.get("preco")
            )
            produto_output = editar_produto.execute(input_dto)
            return jsonify(ProdutoPresenter.apresentar_produto(produto_output)), 200
        except ProdutoNaoEncontradoException as e:
            return ProdutoPresenter.apresentar_erro(str(e), 404)
        except ProdutoInvalidoException as e:
            return ProdutoPresenter.apresentar_erro(str(e), 400)
    
    @produto_db.route("/produto/<int:id>", methods=["DELETE"])
    def excluir(id):
        try:
            excluir_produto.execute(id)
            return "", 204
        except ProdutoNaoEncontradoException as e:
            return ProdutoPresenter.apresentar_erro(str(e), 404)
    
    @produto_db.route("/produto/<int:id>", methods=["GET"])
    def buscar(id):
        try:
            produto_output = buscar_produto.execute(id)
            return jsonify(ProdutoPresenter.apresentar_produto(produto_output)), 200
        except ProdutoNaoEncontradoException as e:
            return ProdutoPresenter.apresentar_erro(str(e), 404)
    
    @produto_db.route("/produto", methods=["GET"])
    def listar():
        lista_output = listar_produto.execute()
        return jsonify(ProdutoPresenter.apresentar_lista_produtos(lista_output)), 200
    
    return produto_db