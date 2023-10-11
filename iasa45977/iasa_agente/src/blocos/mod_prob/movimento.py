"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from dataclasses import dataclass
from tokenize import String

@dataclass
class Movimento():
    movimento : String
    posicao : int