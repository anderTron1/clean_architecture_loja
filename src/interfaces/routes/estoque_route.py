from flask import Blueprint, request, jsonify

from src.use_cases.estoque.dtos import AdicionarEstoqueDTO, BaixarEstoqueDTO
from src.interfaces.presenters.estoque_presenters import EstoquePresenters
from src.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoException, EstoqueInvalidoException

def criar_estoque_controller(buscar_estoque, adicionar_estoque, baixar_estoque):
    estoque_db = Blueprint("estoque", __name__)

    @estoque_db.route("/estoque/<int:produto_id>", methods=["GET"])
    def buscar(produto_id):
        try:
            estoque = buscar_estoque.execute(produto_id)
            return jsonify(EstoquePresenters.apresentar_estoque(estoque)), 200
        except (EstoqueNaoEncontradoException, KeyError) as e:
            return EstoquePresenters.apresentar_erro(str(e), 404)
    
    @estoque_db.route("/estoque/<int:produto_id>", methods=["PUT"])
    def adicionar(produto_id):
        try:
            data = request.json
            estoque_dto = AdicionarEstoqueDTO(
                quantidade=data.get("quantidade")
            )
            estoque = adicionar_estoque.execute(produto_id, quantidade=estoque_dto.quantidade)
            return jsonify(EstoquePresenters.apresentar_estoque(estoque)), 200
        except (EstoqueNaoEncontradoException, EstoqueInvalidoException, KeyError) as e:
            return EstoquePresenters.apresentar_erro(str(e), 404)
    
    @estoque_db.route("/estoque/<int:produto_id>", methods=["PATCH"])
    def baixar(produto_id):
        try:
            data = request.json
            estoque_db = BaixarEstoqueDTO(
                quantiddae=data.get("quantidade")
            )
            estoque = baixar_estoque.execute(produto_id, quantidade=estoque_db.quantiddae)
            return jsonify(EstoquePresenters.apresentar_estoque(estoque)), 200
        except (EstoqueNaoEncontradoException, EstoqueInvalidoException, KeyError) as e:
            return EstoquePresenters.apresentar_erro(str(e), 404)
            
    return estoque_db