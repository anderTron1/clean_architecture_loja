
class Produto:
    def __init__(self, nome, preco, id=None):
        self.id = id
        self._nome = nome
        self._preco = preco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <= 0:
            raise Exception("Preço inválido")
        self._preco = novo_preco
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome == None or novo_nome == "":
            raise Exception("O nome não pode ser vazio")
        self._nome = novo_nome