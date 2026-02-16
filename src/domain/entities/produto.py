
from src.domain.exceptions.produto_exceptions import ProdutoInvalidoException

class Produto:
    def __init__(self, nome, preco, id=None):
        self.nome = nome
        self.preco = preco
        self.id = id
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ProdutoInvalidoException("Nome não pode ser vazio")
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        if preco <= 0 or preco == None:
            raise ProdutoInvalidoException("Preço inválido")
        self._preco = preco
    
    def editar(self, nome=None, preco=None):
        if nome is not None:
            self.nome = nome  # usa o setter e valida
        if preco is not None:
            self.preco = preco  # usa o setter e valida