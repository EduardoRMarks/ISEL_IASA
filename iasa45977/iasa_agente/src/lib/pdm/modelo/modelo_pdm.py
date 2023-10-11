"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface ModeloPDM.

Esta interface será implementada no processo de decisão de Markov, que é uma
representação do problema. A propriedade de Markov diz que o estados futuros
dependem apenas do estado atual, descartando assim os estados anterioires.

Este processo de decisão tem informação sobre estados, ações, transições e 
recompensas, tendo assim o modelo mundo deste tipo de problema.
"""

class ModeloPDM(ABC):

    """
    Método abstracto S (Conjunto de estados).

    Na sua implementação, irá retornar o conjuntos de estados no contexto
    do problema.
    """

    @abstractmethod
    def S(self):
        pass
    
    """
    Método abstracto A (Conjunto de ações possíveis num estado).

    Na sua implementação, irá receber um conjunto de ações e irá devolver as
    ações possíveis para o estado atual.
    """

    @abstractmethod
    def A(self, s):
        pass

    """
    Método abstracto S (Modelo de transição).

    Na sua implementação, recebe o estado atual e o estado seguinte. Irá retornar
    uma lista de transição que tem associado o estado seguinte e a respectiva probabilidade.
    """

    @abstractmethod
    def T(self, s, a, sl):
        pass

    """
    Método abstracto S (Modelo de recompensa).

    Na sua implementação, recebe o estado atual, a ação e o estado seguinte. Irá depois ser
    devolvido a recompensa da ação em concreto, visto que os parâmetros recebidos têm em conta
    um movimento específico.
    """

    @abstractmethod
    def R(self, s, a, sl):
        pass