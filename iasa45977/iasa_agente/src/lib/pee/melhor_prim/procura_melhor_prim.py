"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


from src.lib.pee.mec_proc.fronteira.fronteira_proridade import FronteiraPrioridade
from src.lib.pee.mec_proc.procura_grafo import ProcuraGrafo

"""
Classe ProcuraMelhorPrim (PROCURA MELHOR-PRIMEIRO). É um mecanismo de procura do tipo de
procura em grafo.

Utiliza uma função f para avaliação de cada nó n gerado. Tipicamente f(n) representa uma 
estimativa do custo da solução através do nó n, quanto menor o valor de f(n) mais promissor 
é o nó n. 

A fronteira de exploração (Fringe / Abertos) é ordenada por ordem crescente de f(n).
"""

class ProcuraMelhorPrim(ProcuraGrafo):

    """
    Método construtor da classe ProcuraMelhorPrim.

    O método inicializa a fronteira de exploração com o parâmetro avaliador recebido.

    @:param avaliador
    """

    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador))
    
    """
    Método manter da classe ProcuraMelhorPrim.

    Este método irá chamar o método do mesmo nome da super classe. Irá depois verificar, se o
    custo do nó recebido é menor do que o custo do nó com o mesmo estado.

    @:param no
    @:return true/false
    """

    def _manter(self, no):
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo
