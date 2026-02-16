from src.infra.db.db import db

from src.infra.models.produto_sql import ProdutoSQL

class EstoqueSQL(db.Model):
    __tablename__ = "estoque"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer, nullable=False, default=0)
    produto_id = db.Column(db.Integer, db.ForeignKey("produto.id"), nullable=False, unique=True)

    produto = db.relationship("ProdutoSQL", back_populates="estoque")