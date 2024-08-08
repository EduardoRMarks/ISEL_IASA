"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from src.lib.pee.melhor_prim.procura_informada import ProcuraInformada

"""
Classe ProcuraSofrega, é um tipo de procura informada.

Esta pesquisa baseia-se na minimização da estimativa de custo para atingir o objectivo. Não tem em
conta o custo do percurso explorado. Assim, é uma procura completa mas nem sempre encontra o 
resultado optimo.
"""

class ProcuraSofrega(ProcuraInformada):

    """
    Método construtor da classe ProcuraSofrega.

    Este construtor inicializa o avaliador que irá ser utilizado para a organização da fronteira.
    """

    def __init__(self):
        super().__init__(AvaliadorSof(self._heuristica))