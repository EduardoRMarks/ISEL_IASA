"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from ecr.comportamento import Comportamento
from abc import ABC, abstractmethod

"""
Classe ComportComp
"""


class ComportComp(Comportamento, ABC):
    """
    Método construtor da classe ComportComp
    Recebe uma lista de comporatamentos

    @:param comporatementos
    """

    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

        """
        Método que irá criar uma lista de ações. Uma ação só é 
        adicionada de não for nem 0 nem Null. Depois chama o método da 
        própria Classe para selecionar uma ação, faz isto caso a lista não
        esteja vazia, por fim retorna uma ação
        
        @:param percepcao
        @:return Accao
        """

    def activar(self, percepcao):
        accoes = []

        for comp in self.__comportamentos:
            accao = comp.activar(percepcao)
            if accao:
                accoes.append(accao)
        
        if accoes:
            return self.seleccionar_accao(accoes)

    """
    Método que seleciona uma ação a partir de uma lista
    de ações recebida
    
    @:param accoes
    """
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        Método que permitirá selecionar uma ação face ao mecanismo de reação
        (hierarquia ou prioridade no projeto em estudo) ~
        """