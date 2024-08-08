"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
from src.lib.pee.mec_proc.procura_grafo import ProcuraGrafo

"""
Classe ProcurarLargura que extende da classe ProcuraGarfo.

Este tipo de procura é óptimo e completo.

Na procura em largura, a procura decorre explorando primeiro os nós mais antigos
(primeiros a ser gerados), levando à exploração exaustiva de cada nível de procura
antes da exploração de nós a um nível de maior profundidade.

Como a procura decorre como uma fila, então usamos a fronteira FIFO (First In First Out).
"""

class ProcurarLargura(ProcuraGrafo):

    """
    Método construtor da classe ProcurarLargura.

    O construtor inicializa a FrontreiraFIFO.
    """

    def __init__(self):
        super().__init__(FronteiraFIFO())

    