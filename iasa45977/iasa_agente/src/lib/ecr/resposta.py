"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

"""
Classe Resposta
"""


class Resposta:

    """
    Método construtor da classe Resposta que atribui o valor da accao
    recebida a uma variável estática

    @:param estimulo
    @:param resposta
    """
    def __init__(self, accao):
        self._accao = accao

        """
        Método que ativar da classe Resposta. Este método recebe uma percepção e uma intensidade
        que irá fazer com que retorne uma ação da classe Accao do package sae
        """

    def activar(self, percepcao, intensidade):
        self._accao.prioridade = intensidade
        return self._accao
