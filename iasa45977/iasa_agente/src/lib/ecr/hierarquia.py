"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.ecr.comportComp import ComportComp

"""
Classe Hierarquia

Permite a seleção de uma ação segundo uma hierarquia fixa.

É um dos mecanismos de seleção de ação estudados durante a aula, os comportamentos estão organizados
numa hierarquia fixa de subsunção (supressão e substituição)
"""


class Hierarquia(ComportComp):
    """
    Método da classe Hierarquia concretizado a partir do método abstratato "seleccionar_accao" da classe
    ComportComp. Recebe um lista de ações já organizada com uma certa prioridade e assim retorna a ação
    que se encontra na primeira posição, ou seja, em primeiro lugar na hierarquia, caso a lista de
    ações não esteja vazia.

    @:param accoes
    @:return accao (primeira ação da lista)
    """

    def seleccionar_accao(self, accoes):
        if accoes:
            return accoes[0]
