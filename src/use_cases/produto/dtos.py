from dataclasses import dataclass
from typing import Optional

@dataclass
class ProdutoOutputDTO:
    """DTO de saída para um produto"""
    id: int
    nome: str
    preco: float
    
@dataclass
class CadastrarProdutoDTO:
    nome: str
    preco: float

@dataclass
class EditarProdutoDTO:
    id: int
    nome: Optional[str] = None
    preco: Optional[float] = None