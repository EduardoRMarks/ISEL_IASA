"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.melhor_prim.heuristica import Heuristica

"""
Classe HeurManhattan (Heuristica Distância) que implementa a interface Heuristica.

Trata-se de uma heurística admissível caso não sejam possíveis movimentos diagonais que,
no caso do nosso problema, não são possíveis.
"""

class HeurManhattan(Heuristica):

    """
    Método construtor da classe HeurManhattan.

    Recebe como parâmetro o estado final, ou seja, o objectivo do problema, com o qual
    vão ser calculadas as distâncias, distancias essas onde a heuristica se baseia.

    @:param estado_final
    """
    
    def __init__(self, estado_final):
        self._estado_final = estado_final
    
    """
    Método h da classe HeurManhattan implementado a partir da interface Heuristica.

    Irá ser devolvida a distância de Manhattan entre o estado final e o estado atual do
    agente. Essa distância é calculada a partir da soma dos módulos da diferença das 
    posições x e y do agente e do estado final. Ou seja:

                        h(n) = |xn – xobj| + |yn – yobj|
    
    @:param estado
    @:return distancia de Manhattan
    """

    def h(self, estado):
        return (abs(estado.posicao[0] - self._estado_final.posicao[0])
                + abs(estado.posicao[1] - self._estado_final.posicao[1]))