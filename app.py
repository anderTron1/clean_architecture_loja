from flask import Flask

from src.infra.db import db, migrate

from src.infra.repositories.sql_produto_repository import SQLProdutoRepository

from src.use_cases.produto.salvar_produto import SalvarProdutoUseCase
from src.use_cases.produto.editar_produto import EditarProdutoUseCase
from src.use_cases.produto.excluir_produto import ExcluirProdutoUseCase
from src.use_cases.produto.buscar_produto import BuscarProdutoUseCase
from src.use_cases.produto.listar_produto import ListarProdutosUseCase

from src.interfaces.routes.produto_route import criar_produto_controller

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///loja.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    produto_repo = SQLProdutoRepository()
    salvar_produto = SalvarProdutoUseCase(produto_repo)
    editar_produto = EditarProdutoUseCase(produto_repo)
    excluir_produto = ExcluirProdutoUseCase(produto_repo)
    buscar_produto = BuscarProdutoUseCase(produto_repo)
    listar_produto = ListarProdutosUseCase(produto_repo)

    produto_controller = criar_produto_controller(
        salvar_produto, 
        editar_produto, 
        excluir_produto, 
        buscar_produto, 
        listar_produto
    )

    app.register_blueprint(produto_controller)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)