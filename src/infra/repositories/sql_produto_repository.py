from src.infra.db import db
from src.infra.models.produto_sql import ProdutoSQL

from src.domain.produto import Produto
from src.domain.exceptions import ProdutoNaoEncontradoException, ProdutoInvalidoException

from src.domain.repositories.produto_repository import ProdutoRepository

class SQLProdutoRepository(ProdutoRepository):

    def salvar(self, produto):
        p_sql = ProdutoSQL(
            nome=produto.nome, 
            preco=produto.preco
        )
        db.session.add(p_sql)
        db.session.commit()
        
        produto.id = p_sql.id

        return produto
    
    def editar(self, produto):
        p_sql = ProdutoSQL.query.get(produto.id)

        if not p_sql:
            raise ProdutoNaoEncontradoException("Produto não encontrado!")
        
        campos = ["nome", "preco"]

        alterou = False
        for campo in campos:
            valor = getattr(produto, campo)
            if valor is not None and valor is not "":
                setattr(p_sql, campo, valor)
                alterou = True
                
        if not alterou:
            raise ProdutoInvalidoException("Nenhum campo foi atualizado")
        
        db.session.commit()

        return Produto(id=p_sql.id, nome=p_sql.nome, preco=p_sql.preco)
    
    def excluir(self, id):
        p_sql = ProdutoSQL.query.get(id)
        if not p_sql:
            raise ProdutoNaoEncontradoException("Produto não encontrado!")
        db.session.delete(p_sql)
        db.session.commit()
    
    def buscar(self, id):
        p_sql = ProdutoSQL.query.get(id)
        if not p_sql:
            raise ProdutoNaoEncontradoException("Produto não encontrado!")
        
        return Produto(id=p_sql.id, nome=p_sql.nome, preco=p_sql.preco)
    
    def listar(self):
        produtos_sql = ProdutoSQL.query.all()

        return [
            Produto(id=p.id, nome=p.nome, preco=p.preco) for p in produtos_sql 
        ]