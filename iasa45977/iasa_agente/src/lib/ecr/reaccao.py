"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from ecr.comportamento import Comportamento

"""
Classe Reaccao
"""


class Reaccao(Comportamento):
    """
    Método construtor da classe Reaccao que atribui os valores de estimulo e resposta
    recebidos a variáveis privadas

    @:param estimulo
    @:param resposta
    """

    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

        """
        Método ativar da classe Reaccao. Este método recebe uma percepção que irá ser utilizada
        para chegar o método detectar da classe Estimulo, assim temos uma intensidade detetada e caso
        essa intensidade seja maior que 0 irá retornar a Ação provinda do método activar da classe Resposta
        caso contrário não faz nada
        
        @:param percepcao
        @:return accao
        """

    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if intensidade > 0:
            return self.__resposta.activar(percepcao, intensidade)
