from src.infra.db.db import db 

from src.infra.models.estoque_sql import EstoqueSQL

from src.domain.entities.estoque import Estoque
from src.domain.entities.produto import Produto
from src.domain.repositories.estoque_repository import EstoqueRepository

class SQLEstoqueRepository(EstoqueRepository):
    def buscar_por_produto(self, produto_id):
        est_sql = db.session.query(EstoqueSQL).filter_by(produto_id=produto_id).first()
        if not est_sql:
            return None
        
        produto = Produto(
            id=est_sql.produto.id,
            nome = est_sql.produto.nome,
            preco = est_sql.produto.preco
        )

        estoque = Estoque(
            produto=produto, 
            produto_id=est_sql.produto_id, 
            quantidade=est_sql.quantidade,
            id=est_sql.id
        )

        return estoque

    def salvar(self, estoque):
        e_sql = EstoqueSQL(
            quantidade = estoque.quantidade,
            produto_id = estoque.produto_id
        )

        db.session.add(e_sql)
        db.session.commit()
        return Estoque(
            produto = None,
            quantidade= e_sql.quantidade,
            produto_id=e_sql.produto_id,
            id=e_sql.id
        )


    def adicionar(self, produto_id, quantidade):
        est_sql = db.session.query(EstoqueSQL).filter_by(produto_id=produto_id).first()
        if not est_sql:
            return None
        
        estoque = Estoque(
            produto = None,
            produto_id= est_sql.produto_id,
            quantidade= est_sql.quantidade,
            id=est_sql.id
        )
        estoque.adicionar(quantidade)

        est_sql.quatidade = estoque.quantidade
        db.session.commit()

        return estoque

    def baixar(self, produto_id, quantidade):
        est_sql = db.session.query(EstoqueSQL).filter_by(produto_id=produto_id).first()
        if not est_sql:
            return None
        
        estoque = Estoque(
            produto=None,
            produto_id=est_sql.produto_id,
            quantidade=est_sql.quantidade,
            id=est_sql.id
        )
        estoque.baixar(quantidade)

        est_sql.quantidade = estoque.quantidade
        db.session.commit()

        return estoque