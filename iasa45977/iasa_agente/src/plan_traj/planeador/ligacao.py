"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from dataclasses import dataclass
from tokenize import String

"""
Dataclasse Ligacao.

Cada elemento da lista de ligações do nosso problema é composta por duas localidade
e o respectivo custo. O espaço de estados, assim, identifica o estado de origem, o estado
de destino e por fim o custo da transição (transição essa que é feita do primeiro parâmetro
para o segundo).

Neste caso, tanto a origem como o destino são Strings e o custo é um inteiro.
"""

@dataclass
class Ligacao():
    origem : String
    destino : String
    custo : int

