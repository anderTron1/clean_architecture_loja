
class ProdutoException(Exception):
    pass

class ProdutoInvalidoException(ProdutoException):
    pass

class ProdutoNaoEncontradoException(ProdutoException):
    pass