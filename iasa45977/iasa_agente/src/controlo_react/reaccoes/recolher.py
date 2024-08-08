"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from src.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from src.controlo_react.reaccoes.explorar.explorar import Explorar
from src.lib.ecr.hierarquia import Hierarquia

"""
Classe Recolher

É uma classe que herda da classe Hierarquia. Esta classe irá instanciar os 3 comportamentos do agente,
criados nas partes 4 e 5 do projecto (aulas das entregas 3 e 4 respetivamente).
"""


class Recolher(Hierarquia):
    """
    Método construtor da classe Recolher que implementa o construtor da classe pai, ou seja, classe ComportComp,
    onde cria uma lista com as 3 instâncias, onde a sua hierarquia é organizada pela ordem pela qual são
    instanciadas, ou seja, em primeiro está o comportamento AproximarAlvo, seguido pelo comportamento EvitarObst
    e, por último, o comportamento Explorar
    """

    def __init__(self):
        super().__init__([AproximarAlvo(), EvitarObst(), Explorar()])
