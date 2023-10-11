"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface Avaliador.

Esta interface define o contrato funcional de avaliação da prioridade de um nó para ordenação
da fronteira por prioridade. É concretizado de acordo com o tipo da procura.
"""

class Avaliador(ABC):

    """
    Método abstrato prioridade da interface Avaliador. Este método será implementado a partir
    da classe que herdar esta interface.

    Irá retornar a prioridade de um nó.

    @:param no
    @:return prioridade
    """

    @abstractmethod
    def prioridade(self, no):
        pass