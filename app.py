from flask import Flask

from src.infra.db.db import db, migrate

from src.interfaces.routes.produto_route import criar_produto_controller
from src.interfaces.routes.estoque_route import criar_estoque_controller

from src.infra.repositories.sql_produto_repository import SQLProdutoRepository
from src.infra.repositories.sql_estoque_repository import SQLEstoqueRepository

from src.use_cases.produto.salvar_produto import SalvarProdutoUseCase
from src.use_cases.produto.editar_produto import EditarProdutoUseCase
from src.use_cases.produto.buscar_produto import BuscarProdutoUseCase
from src.use_cases.produto.listar_produto import ListarProdutosUseCases
from src.use_cases.produto.excluir_produto import ExcluirProdutoUseCase

from src.use_cases.estoque.buscar_estoque import BuscarEstoqueUseCase
from src.use_cases.estoque.adicionar_estoque import AdicionarEstoqueUseCase
from src.use_cases.estoque.baixar_estoque import BaixarEstoqueUseCase

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///loja.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["TESTING"] = True

    db.init_app(app)
    migrate.init_app(app, db)

    produto_repo = SQLProdutoRepository()
    estoque_repo = SQLEstoqueRepository()

    salvar_produto = SalvarProdutoUseCase(produto_repo, estoque_repo)
    editar_produto = EditarProdutoUseCase(produto_repo)
    buscar_produto = BuscarProdutoUseCase(produto_repo)
    listar_produtos = ListarProdutosUseCases(produto_repo)
    excluir_produto = ExcluirProdutoUseCase(produto_repo)

    produto_controller = criar_produto_controller(
        salvar_produto,
        editar_produto,
        buscar_produto,
        listar_produtos,
        excluir_produto
    )

    buscar_estoque = BuscarEstoqueUseCase(estoque_repo)
    adicionar_estoque = AdicionarEstoqueUseCase(estoque_repo)
    baixar_estoque = BaixarEstoqueUseCase(estoque_repo)
    
    estoque_controller = criar_estoque_controller(
        buscar_estoque,
        adicionar_estoque,
        baixar_estoque
    )

    app.register_blueprint(produto_controller)
    app.register_blueprint(estoque_controller)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)