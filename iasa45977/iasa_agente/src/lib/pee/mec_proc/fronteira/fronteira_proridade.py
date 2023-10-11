"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from heapq import heappush, heappop
from pee.mec_proc.fronteira.fronteira import Fronteira

"""
Classe FronteiraPrioridade

É uma classe utilizada no método "procura melhor-primeiro", ou seja, há um prioridade nos
nós que são inseridos.

Esta classe extende da classe Fronteira pois, como o nome indica, é um tipo de fronteira
e irá implementar o método abstracto inserir da mesma.
"""

class FronteiraPrioridade(Fronteira):

    """
    Método construtor da classe FronteiraPrioridade.

    Este construtor chama o construtor da classe Fronteira e guarda numa variável privada
    o avaliador de prioridades, ou seja, f(n) presente na primeira página dos slides 
    "PROCURA EM ESPAÇOS DE ESTADOS".

    @:param avaliador
    """

    def __init__(self, avaliador):
        super().__init__()
        self._avaliador = avaliador

    """
    Método inserir da classe FronteiraPrioridade implementado a partir do método abstrato
    da classe Fronteira.

    Este método irá irá avaliar a prioridade do nó recebido. Com a sua prioridade, podemos
    então inserir o nó na sua respetiva posição, utilizando  o heapq, que organiza a lista.

    @:param no
    """

    def inserir(self, no):
        prio = self._avaliador.prioridade(no)
        heappush(self._nos, (prio, no))


    """
    Método remover da classe FronteiraPrioridade.

    Irá remover o nó com a sua respectiva prioridade.

    @:return no
    """

    def remover(self):
        _, no = heappop(self._nos)
        return no