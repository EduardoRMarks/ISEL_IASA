"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from src.lib.mod.estado import Estado

"""
Classe EstadoAgente que é um tipo de estado.

Esta classe representa a posição onde o agente se encontra a partir de um tuplo, tuplo
esse que representa as posições x e y (coordenadas do espaço vectorial). Como esta classe
herda da classe Estado, sabemos que cada estado tem que ser único para existir diferenciação,
diferenciação essa que é possível através de hash values.
"""

class EstadoAgente(Estado):

    """
    Propriedade read only que retorna a posição de um agente.
    """

    @property
    def posicao(self):
        return self._posicao
    
    """
    Método construtor da classe EstadoAgente.

    Este método recebe uma posição e guarda-a.

    @:param posicao
    """

    def __init__(self, posicao):
        self._posicao = posicao

    """
    Método id_valor da classe EstadoAgente.

    Método implementado a partir do método abstrato presente na classe pai Estado.

    O método retorna um hash value, o que permite que seja feita a distinção de cada estado
    do mesmo tipo.

    @:return hash value
    """

    def id_valor(self):
        return self._posicao.__hash__()