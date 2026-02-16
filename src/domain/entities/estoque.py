
from src.domain.exceptions.estoque_exceptions import EstoqueInvalidoException
class Estoque:
    def __init__(self, produto, produto_id, quantidade, id=None):
        self.produto = produto
        self.produto_id = produto_id
        self.__quantidade  = quantidade
        self.id = id
    
    @property
    def quantidade(self):
        return self.__quantidade  
    
    @quantidade.setter
    def quantidade(self, qtd):
        raise EstoqueInvalidoException("Não pode ser editada diretamente. Use métodos específicos para alterar.")

    def adicionar(self, qtd):
        if qtd is None or qtd <= 0:
            raise EstoqueInvalidoException("Valor inálido para adicionar ao estoque")
        self.__quantidade  += qtd
    
    def baixar(self, qtd):
        if qtd is None or qtd <= 0:
            raise EstoqueInvalidoException("Valor inválido para remover do estoque")
        
        if qtd > self.__quantidade :
            raise EstoqueInvalidoException("Quantidade insuficiente no estoque")
        self.__quantidade  -= qtd