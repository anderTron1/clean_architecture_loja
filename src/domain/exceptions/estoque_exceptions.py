
class EstoqueException(Exception):
    pass

class EstoqueInvalidoException(EstoqueException):
    pass

class EstoqueNaoEncontradoException(EstoqueException):
    pass