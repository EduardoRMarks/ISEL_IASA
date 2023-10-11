"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""


from ecr.resposta import Resposta
from sae import Accao

"""
Classe RespostaMover

É um tipo de Resposta que extende da classe Resposta que permite a movimentação do agente.
Esta classe permite tratar de respostas que irão gerar uma determinada ação, neste caso, o tipo
de movimento do agente.
Estes movimentos são descritos por uma direção, que faz parte do enumerado Direccao. Assim, o agente
tem um total de 4 movientos sendo eles Norte, Sul, Este e Oeste (nunca tem as direções todas ao mesmo tempo)

"""


class RespostaMover(Resposta):
    """
    Método construtor da classe RespostaMover, que chama o construtor da classe pai (Resposta).
    Envia para o contrutor uma Ação baseada na direção recebida.

    @:param direccao
    """

    def __init__(self, direccao):
        super().__init__(Accao(direccao))
