class ProdutoException(Exception):
    """Exceção base para erros relacionados a Produto"""
    pass


class ProdutoNaoEncontradoException(ProdutoException):
    """Exceção lançada quando um produto não é encontrado"""
    pass


class ProdutoInvalidoException(ProdutoException):
    """Exceção lançada quando um produto tem dados inválidos"""
    pass
