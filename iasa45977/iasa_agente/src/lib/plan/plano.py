"""
IASA 22/23

Trabalho realizado por:
Eduardo Marques 45977

Docente Paulo Vieira
"""

from abc import ABC, abstractmethod

"""
Interface Plano.

Esta interface tem, dois métodos abstractos sendo eles obter_accao e mostrar que iram ser
implementados pela classe que implementar a interface.
"""

class Plano(ABC):

    """
    Método abstrato obter_accao. Na implementação, o método receberá um estado e irá
    devolver um operador.
    """

    @abstractmethod
    def obter_accao(self, estado):
        pass

    """
    Método abstracto mostrar. Na implementação, este método receberá um tipo de vista 
    proveniente do package vistas da lib sae.
    """

    @abstractmethod
    def mostrar(self, vista):
        pass