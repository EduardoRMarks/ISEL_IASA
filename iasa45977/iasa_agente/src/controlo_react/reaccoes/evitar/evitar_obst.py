"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

"""
Classe EvitarObst

É uma classe que irá permitir evitar obstaculos por parte do agente. Os obstáculos, neste caso, são as paredes
que se encontram no nosso mapa.

Chamamos a classe EvitarDir, que estende de Reaccao, para cada direção no nosso enumerado Direccao. Ficamos assim com
um comportamento composto com 4 instancias da classe EvitarDir.

Para o movimento ser efetuado iremos recorrer à classe RespostaEvitar que herda da classe RespostaMover, assim iremos conseguir
controlar os movimentos do agente, o que fará com que não haja colisão com os obstáculos. 
"""


class EvitarObst(Hierarquia):
    """
    Método construtor da classe EvitarObst, que irá criar uma lista com instancias da classe EvitarDir, ou seja,
    uma lista com 4 direções distintas. Com a lista criada, irá ser chamado o super() da classe à qual herda.
    """

    def __init__(self):
        resposta = RespostaEvitar()
        listResp = []

        for dir in Direccao:
            listResp.append(EvitarDir(dir, resposta))

        super().__init__(listResp)
