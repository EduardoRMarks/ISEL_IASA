"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.ecr.comportComp import ComportComp

"""
Classe Prioridade

Seleciona uma ação por uma hierarquia.

É um dos outros mecânismos de seleção de ação estudados durante a aula, sendo o terceiro a Fusão. As respostas
são selecionadas de acordo com uma prioridade associada que varia ao longo da execução.
"""


class Prioridade(ComportComp):
    """
    Método da classe Prioridade concretizado a partir do método abstratato "seleccionar_accao" da classe
    ComportComp. Recebe um lista de ações e retorna a ação com a prioridade mais elevada caso a lista de
    ações não esteja vazia.

    @:param accoes
    @:return accao (ação com a maior prioridade)
    """

    def seleccionar_accao(self, accoes):
        if accoes:
            return max(accoes, key=lambda accao: accao.prioridade)
