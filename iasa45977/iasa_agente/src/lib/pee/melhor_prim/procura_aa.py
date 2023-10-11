"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from pee.melhor_prim.procura_informada import ProcuraInformada

"""
Classe ProcuraAA (procura a*), é um tipo de procura informada.

Esta procura tem uma heurística admissível, ou seja, o custo do nó n será o mínimo
até ao objectivo. Este tipo de heurística é optimista, o que quer dizer que a estimativa
de custo é sempre inferior ou igual ao custo efectivo.

Podemos então afirmal que este tipo de procura é completo e optimo.
"""

class ProcuraAA(ProcuraInformada):
    
    """
    Método construtor da classe ProcuraAA.

    Este construtor inicializa o avaliador que irá ser utilizado para a organização da fronteira.
    """

    def __init__(self):
        self._avaliador = AvaliadorAA()
        super().__init__(self._avaliador)