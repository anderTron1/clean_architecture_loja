
class Estoque:
    def __init__(self,  produto, quantidade):
        if quantidade < 0:
            raise Exception("Quantidade inicial inválida")
        self._produto = produto
        self._quantidade = quantidade
    
    @property
    def produto(self):
        return self._produto
    
    @property
    def quantidade(self):
        return self._quantidade

    def adicionar(self, qtd):
        if qtd <= 0:
            raise Exception("Quantidade inválida")
        self._quantidade += qtd

    def baixar(self, qtd):
        if qtd <= 0:
            raise Exception("Quantidade inválida")
        
        if qtd > self._quantidade:
            raise Exception("Estoque insuficiente")
        self._quantidade -= qtd