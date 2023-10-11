"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
Classe ProcuraCustoUnif, é um tipo de Procura Melhor-Primeiro.

Este tipo de procura é optimo e completo.

Tem como objectivo a inicialização de um avaliador que toma decisões a partir do custo. Assim,
neste caso, f(n) será a estimativa do custo da solução através do nó n.
"""

class ProcuraCustoUnif(ProcuraMelhorPrim):

    """
    Contrutor da classe ProcuraCustoUnif.

    Este construtor inicializa a classe AvaliadorCustoUnif que é o tipo de avaliador de custo
    utilizado na procura onde estamos inseridos.
    """

    def __init__(self):
        super().__init__(AvaliadorCustoUnif())