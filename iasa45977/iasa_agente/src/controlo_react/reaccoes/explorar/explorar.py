"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

import random
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae.ambiente.direccao import Direccao

"""
Classe Explorar

Classe que permite que o agente faça movimentos aleatóriamente.

Nesta classe tratar-se-á do último sub-objectivos estudado em aula sobre o agente prospector,
o sub-objectico Explorar, sendo os outros subobjectivos o Aproximar alvo e Evitar obstáculos.
Neste sub-objectivo o agente deverá mover-se aleatóriamente no espaço, sem querer recolher alvos
nem evitar obstáculos.

Como este sub-objectivo não reage com nada, irá herdar Comportamento e não Reaccao.
"""


class Explorar(Comportamento):
    """
    Método da classe Explorar concretizado a partir do método abstratato "activar" da classe Comportamento.

    Este método retorna uma açao que resulta a partir de uma resposta que resulta a partir de uma direção random.

    Para termos a direção iremos utilizar a classe enumerado Direccao. Começamos por ver o seu tamanho e guardamos o mesmo
    numa variável auxiliar, também subtraímos uma unidade para o ponto seguinte. Com a variável auxiliar irá ser feito um 
    random dentro de um intervalo de valores (0 a 3), por isso é que temos que subtrair uma unidade ao valor auxiliar anterior
    pois o metodo randint(x, y) retorna um valor >=x e <=y. Com o valor random, adquirimos a direção na posição random na classe
    enumerada, obtendo assim a direção que o agente irá ter.

    Depois, é obtido uma resposta a partir da RespostaMover, passando a direção. Com esta resposta pordemos chamar o método
    activar() da classe resposta, que irá tornar uma ação, ação essa que irá ser retornada para que o agente de mova.

    @:param percepcao
    @:return accao
    """

    def activar(self, percepcao):
        num = len(Direccao) - 1
        rand = random.randint(0, num)
        direc = list(Direccao)[rand]

        resposta = RespostaMover(direc)

        accao = resposta.activar(percepcao, 0.0)

        return accao
