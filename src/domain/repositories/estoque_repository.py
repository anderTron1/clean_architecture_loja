from abc import ABC, abstractmethod

class EstoqueRepository(ABC):
    @abstractmethod
    def salvar(self, produto):
        pass
    
    @abstractmethod
    def editar(self, produto):
        pass

    @abstractmethod
    def excluir(self, id):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def listar(self):
        pass   