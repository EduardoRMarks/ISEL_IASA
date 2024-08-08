"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from math import sqrt
from src.lib.pee.melhor_prim.heuristica import Heuristica

"""
Classe HeurEuclidiana (Heuristica Distância) que implementa a interface Heuristica.

Trata-se de uma heurística admissível.
"""

class HeurEuclidiana(Heuristica):

    """
    Método construtor da classe HeurEuclidiana.

    Recebe como parâmetro o estado final, ou seja, o objectivo do problema, com o qual
    vão ser calculadas as distâncias, distancias essas onde a heuristica se baseia.

    @:param estado_final
    """
    
    def __init__(self, estado_final):
        self._estado_final = estado_final

    """
    Método h da classe HeurEuclidiana implementado a partir da interface Heuristica.

    Irá ser devolvida a distância Euclidiana entre o estado final e o estado atual do
    agente. Essa distância é calculada a partir da raiz quadrada da soma dos quadrados
    da diferença entre as posições x e y do agente e do estado final. Ou seja:

                        h(n) = √((xn – xobj)2 + (yn – yobj)2)

                Fazer a conta desta maneira seria igual a utilizar a função dist(),
                assim, podemos comparar a classe HeurDist criada há umas aulas atrás, que utiliza
                a função dist() com a classe onde nos encontramos com a conta feita por extenso.
                Podemos confirmar que ambas as heuristica contêm o mesmo output.
    
    @:param estado
    @:return distancia de Manhattan
    """

    def h(self, estado):
        return sqrt((estado.posicao[0] - self._estado_final.posicao[0])**2 
                    + (estado.posicao[1] - self._estado_final.posicao[1])**2)