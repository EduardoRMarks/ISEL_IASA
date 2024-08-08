"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""
from src.lib.sae import Controlo

"""
Classe ControloReact (Trabalha o controlo Reativo do agente)

Faz a agragação de um comportamento ao agente. Através de uma precepção recebida, processa, obtendo
e retornando a ativação de um comportamento resultante da percepção.
"""


class ControloReact(Controlo):
    """
    Método construtor da classe ControloReact.

    Recebe um comportamento que é um objecto da Classe comportamento que irá ter a finalidade de ser
    ativado a partir de uma percepção recebida quando é feito o processamento da classe ControloReact.

    Ativamos também uma flag para mostrar a visão direcional do agente

    @:param comportamento
    """

    def __init__(self, comportamento):
        self.__comportamento = comportamento
        self.mostrar_per_dir = True

    """
    Método da classe ControloReact concretizado a partir do método abstratato "processar" da classe Controlo.
    Recebe um objecto da classe Percepção e tem como objectivo retornar uma ação que resulte da ativação do comportamento
    recebido no construtor com a percepção recebida.

    @:param percepcao
    @:return accao (acção a realizar)
    """

    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)
