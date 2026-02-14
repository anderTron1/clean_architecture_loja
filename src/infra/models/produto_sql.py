from src.infra.db import db

class ProdutoSQL(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String(250), nullable=False)
    preco = db.Column(db.Float, nullable=False)