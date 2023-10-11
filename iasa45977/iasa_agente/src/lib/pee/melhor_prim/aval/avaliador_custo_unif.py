"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from pee.mec_proc.fronteira.avaliador import Avaliador

"""
Classe AvaliadorCustoUnif (Avaliador de custo uniforme).

Classe que implementa a interface Avaliador. Este avaliador é utilizado na pesquisa
de custo uniforme.
"""

class AvaliadorCustoUnif(Avaliador):

    """
    Método prioridade da classe AvaliadorCustoUnif implementado a partir do método abstrato
    da interface Avaliador.

    A prioridade depende do custo de cada nó, assim este método retorna o custo do nó recebido.

    @:param no
    @:return custo
    """

    def prioridade(self, no):
        return no.custo