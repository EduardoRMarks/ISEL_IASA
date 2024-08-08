"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.pee.melhor_prim.heuristica import Heuristica

"""
Classe HeurBloco, é um tipo de heurística, logo implemente a interface Heuristica.

A heuristica, neste caso, será o número de blocos que diferem na primeira pilha, ou seja, caso a primeira pilha do
estado atual tenha os valores [1, 3], apenas comparamos as primeiras duas posições do estado final, ou seja, a
heuristica teria o valor de 1, mas como o tamanho das duas pilhas tabém difere, sabemos que a última posição do estado
atual não está em conformidade com o estado final, então, é adicionado o valor da diferença de tamanhos das duas
pilhas, o que faria com que a heuristica final, neste caso, fosse 2.
"""

class HeurBloco(Heuristica):

    """
    Método construtor da classe HeurBloco.

    Rebe o estado final e inicializando uma variável com o mesmo valor.

    @bloco_final
    """

    def __init__(self, pilha_final):
        self._pilha_final = pilha_final

    """
    Método h da classe HeurBloco implementada a partir da interface Heuristica.

    Recebe o estado atual das pilhas e compara, como foi mencionado no incio da classe.

    @:estado
    @:diferenca
    """

    def h(self, estado):
        dif = 0

        for i in range(len(estado[0])):
            if(estado[0][i] != self._pilha_final[0][i]):
                dif += 1

        return dif + len(self._pilha_final[0]) - len(estado[0])