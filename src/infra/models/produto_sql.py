from src.infra.db.db import db

class ProdutoSQL(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(180), nullable=False)
    preco = db.Column(db.Float, nullable=False, default=0)

    # IMPORTANTE: cascade remove automaticamente o estoque quando o produto for deletado
    estoque = db.relationship("EstoqueSQL", back_populates="produto", uselist=False, cascade="all, delete-orphan")
