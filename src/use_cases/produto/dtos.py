from dataclasses import dataclass
from typing import Optional


@dataclass
class CriarProdutoInputDTO:
    """DTO de entrada para criar um produto"""
    nome: str
    preco: float


@dataclass
class AtualizarProdutoInputDTO:
    """DTO de entrada para atualizar um produto"""
    id: int
    nome: Optional[str] = None
    preco: Optional[float] = None


@dataclass
class ProdutoOutputDTO:
    """DTO de saída para um produto"""
    id: int
    nome: str
    preco: float


@dataclass
class ListarProdutosOutputDTO:
    """DTO de saída para lista de produtos"""
    produtos: list[ProdutoOutputDTO]
    total: int
