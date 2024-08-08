"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from src.lib.pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Clase ProcuraProfundidade que extende da classe MecanismoProcura.

Este tipo de procura não é óptimo nem completo.

Na procura em profundidade, a procura decorre explorando primeiro os nós mais recentes
(últimos a ser gerados), aumentando por isso a profundidade do ramo corrente de procura.

Como a procura decorre procurando o último a ser inserido em primeiro lugar, então usamos 
a fronteira LIFO (Last In First Out).
"""

class ProcuraProfundidade(MecanismoProcura):

    """
    Método construtor da classe ProcuraProfundidade.

    O construtor inicializa a FrontreiraLIFO.
    """
    
    def __init__(self):
        super().__init__(FronteiraLIFO())

    """
    Método memorizar da classe ProcuraProfundidade implementada a partir do método abstrato
    da classe MecanismoProcura da qual estende.

    Esta classe irá inserir o nó procurado à fronteira.

    @:param no
    """

    def _memorizar(self, no):
        self._fronteira.inserir(no)
        self._maior_mem = max(self._fronteira.numero_nos, self._maior_mem)