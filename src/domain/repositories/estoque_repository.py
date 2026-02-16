from abc import ABC, abstractmethod

class EstoqueRepository(ABC):
    @abstractmethod
    def buscar_por_produto(self, produto_id):
        pass

    @abstractmethod
    def salvar(self, estoque):
        pass

    @abstractmethod
    def adicionar(self, produto_id, quantidade):
        pass

    @abstractmethod
    def baixar(self, produto_id, quantidade):
        pass