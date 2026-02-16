from dataclasses import dataclass
from typing import Optional
from src.domain.entities.produto import Produto

@dataclass
class EstoqueOutputDTO:
    """DTO de saída para um produto"""
    id: int
    produto_id: int
    quantidade: int
    produto: Produto

@dataclass
class AdicionarEstoqueDTO:
    quantidade: int

@dataclass
class BaixarEstoqueDTO:
    quantidade: int