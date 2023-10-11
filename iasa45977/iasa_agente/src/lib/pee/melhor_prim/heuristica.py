"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface Heurística.

Representa uma estimativa do custo do percurso desde um nó inicial até ao nó final, mas
sendo uma estimativa, pode não corresponder ao valor real. Reflecte conhecimento acerca
do domínio do problema, para guiar a procura.

Esta interface é utilizada e, por sua vez, implementada a partir de tipos de procuras
informadas, onde cada uma terá uma implementação diferente.
"""

class Heuristica(ABC):

    """
    Método h() da interface Heurística.

    Método que devolve um custo de um estado.

    @:param estado
    @:return custo (estimativa)
    """

    @abstractmethod
    def h(self, estado):
        pass