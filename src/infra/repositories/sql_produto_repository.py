from src.infra.db.db import db

from src.infra.models.produto_sql import ProdutoSQL

from src.domain.entities.produto import Produto

from src.domain.repositories.produto_repository import ProdutoRepository

class SQLProdutoRepository(ProdutoRepository):
    def salvar(self, produto):
        p_sql = None

        if produto.id is not None:
            p_sql = db.session.get(ProdutoSQL, produto.id)

        if not p_sql:
            #Cadastrando produto
            p_sql = ProdutoSQL(
                nome=produto.nome,
                preco=produto.preco
            )
            db.session.add(p_sql)
        else:
            # Atualizando produto existente
            if produto.nome is not None:
                p_sql.nome = produto.nome
            if produto.preco is not None:
                p_sql.preco = produto.preco
            
        db.session.commit()
        produto.id = p_sql.id
        return produto

    def buscar(self, id):
        p_sql = db.session.get(ProdutoSQL, id)

        if not p_sql:
            return None
        
        produto = Produto(id=p_sql.id, nome=p_sql.nome, preco = p_sql.preco)

        return produto

    def excluir(self, id):
        p_sql = db.session.get(ProdutoSQL, id)

        if not p_sql:
            return None
        
        db.session.delete(p_sql)
        db.session.commit()

    def listar(self):
        p_sql = db.session.query(ProdutoSQL).all()

        return [
            Produto(id=p.id, nome=p.nome, preco=p.preco) for p in p_sql
        ]