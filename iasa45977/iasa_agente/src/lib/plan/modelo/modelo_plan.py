"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface ModeloPlan.

Esta interface é implementada pela classe ModeloMundo, ou seja, é uma representação
do dos planos e ações do agente, havendo necessidade de informação sobre o estado atual
no espaço de estados, bem como a lista de estados e os operados do problema.
"""

class ModeloPlan(ABC):

    """
    Método obter_estado.

    Na sua implementação, o método irá devolver o estado atual do agente.
    """

    @abstractmethod
    def obter_estado(self):
        pass

    """
    Método obter_estados.

    Na sua implementação, o método irá devolver uma lista de estados.
    """

    @abstractmethod
    def obter_estados(self):
        pass

    """
    Método obter_operadores.

    Na sua implementação, o método irá devolver o conjunto de operadores no
    domínio do mundo.
    """

    @abstractmethod
    def obter_operadores(self):
        pass