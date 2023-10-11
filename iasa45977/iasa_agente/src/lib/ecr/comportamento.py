"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Classe Comportamento
"""


class Comportamento(ABC):
    """
    Método da classe Comportamento que irá
    ativar um comportamento em relação à percepção que recebe

    @:param percepcao
    @:return Accao
    """

    @abstractmethod
    def activar(self, percepcao):
        "Ativa um dado comportamento"
