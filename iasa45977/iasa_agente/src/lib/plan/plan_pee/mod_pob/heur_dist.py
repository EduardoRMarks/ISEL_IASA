"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from math import dist
from src.lib.pee.melhor_prim.heuristica import Heuristica

"""
Classe HeurDist (Heuristica Distância) que implementa a interface Heuristica.

Representa uma estimatica do custo do percurso do nó n até ao nó objectivo.
Por este motivo, tem conhecimento do estado final, ou seja, do objectivo.
"""

class HeurDist(Heuristica):

    """
    Método construtor da classe HeurDist.

    Recebe como parâmetro o estado final, ou seja, o objectivo do problema, com o qual
    vão ser calculadas as distâncias, distancias essas onde a heuristica se baseia.

    @:param estado_final
    """

    def __init__(self, estado_final):
        self._estado_final = estado_final

    """
    Método h da classe HeurDist implementado a partir da interface Heuristica.

    Irá ser devolvido a estimativa de custo entre o estado recebido e o estado final, custo
    esse que irá ser calculado a partir da distância entre as posições.

    @:param estado
    @:return dist
    """

    def h(self, estado):
        return dist(self._estado_final.posicao, estado.posicao)
