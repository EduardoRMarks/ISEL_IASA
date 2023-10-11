"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.prof.procura_prof_lim import ProcuraProfLim

"""
Classe ProcuraProfIter que extende da classe ProcuraProfLim.

Este tipo de procura é óptimo e completo.

Esta classe é um tipo de procura em profundidade. Este tipo de procura é um mecanismo
óptimo e completo.

Para um limite de profundidade crescente, realiza a procura com o limite atual e se existe
uma solução, retornara a mesma.
"""

class ProcuraProfIter(ProcuraProfLim):

    """
    Método procurar da classe ProcuraProfIter.

    Este método irá procurar até uma profundidade crescente, modificanto a profundidade
    máxima para o valor da profundidade maxima atual e chama o método procurar da classe pai,
    neste caso, o método procurar da classe mecanismo de procura.

    Esta procura devolve uma solução, e caso essa solução não seja None, retornamos a solução
    e a procura acaba, caso contrário incrimentamos com uma unidade a profundidade máxima.

    @:param problema
    @:param inc_prof
    @:param limite_prof
    @:return solucao
    """

    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        for i in range(1, limite_prof, inc_prof):
            self.prof_max = i
            solucao  = super().procurar(problema)
            if solucao:
                return solucao