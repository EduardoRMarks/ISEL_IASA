"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface Estimulo
Permitirá obter a intensidade de dada caraterística do ambiente.
"""


class Estimulo(ABC):
    """
    Método da classe Estimulo que dependendo de uma percepção
    detetada retorna uma intensidade em float

    @:param percepcao
    @:return intensidade
    """
    @abstractmethod
    def detectar(self, percepcao):
        "Deteta um estímulo numa percepção"
