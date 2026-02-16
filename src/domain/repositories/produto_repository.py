from abc import ABC, abstractmethod

class ProdutoRepository(ABC):
    @abstractmethod
    def salvar(self, produto):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def excluir(self, id):
        pass

    @abstractmethod
    def listar(self):
        pass